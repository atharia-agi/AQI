"""
Fusion components for TawhidUnifier: MultimodalFusion and StreamProcessor.
"""

import torch
import torch.nn as nn
from typing import List, Dict, Optional


class StreamProcessor(nn.Module):
    """
    Preprocesses raw modality data into token sequences ready for the shared backbone.
    Each modality may have its own tokenization/embedding strategy.
    """

    def __init__(
        self,
        modality_dims: Dict[str, int],
        shared_dim: int = 768,
        max_len: int = 512,
    ):
        super().__init__()
        self.modality_dims = modality_dims
        self.shared_dim = shared_dim
        self.max_len = max_len

        # Project each modality to shared dimension
        self.projections = nn.ModuleDict(
            {
                mod: nn.Linear(dim, shared_dim)
                for mod, dim in modality_dims.items()
            }
        )

        # Optional: modality type embeddings (like BERT's token type)
        self.modality_type_embeddings = nn.Embedding(
            num_embeddings=len(modality_dims),
            embedding_dim=shared_dim,
        )

    def forward(
        self,
        batch: Dict[str, torch.Tensor],
    ) -> Dict[str, torch.Tensor]:
        """
        Args:
            batch: dict mapping modality -> (batch, seq_len, mod_dim) or (batch, mod_dim)
        Returns:
            dict mapping modality -> (batch, seq_len, shared_dim) ready for backbone
        """
        processed = {}
        for mod, tensor in batch.items():
            if tensor.dim() == 2:  # (B, D) single vector per sample
                tensor = tensor.unsqueeze(1)  # (B, 1, D)
            # Project to shared dimension
            projected = self.projections[mod](tensor)  # (B, L, D_shared)
            # Add modality type embedding
            mod_id = list(self.modality_dims.keys()).index(mod)
            type_emb = self.modality_type_embeddings(
                torch.tensor(mod_id, device=tensor.device)
            )  # (D_shared,)
            projected = projected + type_emb.view(1, 1, -1)
            processed[mod] = projected
        return processed


class MultimodalFusion(nn.Module):
    """
    Fuses modality-specific features into a single representation.
    Multiple strategies: concat+proj, attention pooling, or gated fusion.
    """

    def __init__(
        self,
        modality_dims: Dict[str, int],
        shared_dim: int = 768,
        fusion_type: str = "attention",
    ):
        super().__init__()
        self.modality_dims = modality_dims
        self.shared_dim = shared_dim
        self.fusion_type = fusion_type

        if fusion_type == "concat":
            total_dim = sum(modality_dims.values())
            self.proj = nn.Linear(total_dim, shared_dim)
        elif fusion_type == "attention":
            # Residual‑style attention fusion
            self.norms = nn.ModuleDict(
                {mod: nn.LayerNorm(dim) for mod, dim in modality_dims.items()}
            )
            self.attention = nn.MultiheadAttention(
                embed_dim=shared_dim,
                num_heads=8,
                batch_first=True,
            )
            self.output_proj = nn.Linear(shared_dim, shared_dim)
        elif fusion_type == "gated":
            self.gates = nn.ParameterDict(
                {mod: nn.Parameter(torch.ones(1)) for mod in modality_dims}
            )
            self.proj = nn.Linear(shared_dim, shared_dim)
        else:
            raise ValueError(f"Unknown fusion_type: {fusion_type}")

    def forward(
        self,
        features: Dict[str, torch.Tensor],
    ) -> torch.Tensor:
        """
        Args:
            features: dict mapping modality -> (batch, dim) or (batch, seq, dim)
        Returns:
            fused representation (batch, shared_dim)
        """
        # Extract [CLS]‑like representations; if seq, mean pool
        reps = []
        for mod, feat in features.items():
            if feat.dim() == 3:
                feat = feat.mean(dim=1)  # simple mean pooling
            reps.append(feat)

        if self.fusion_type == "concat":
            combined = torch.cat(reps, dim=1)  # (B, sum dims)
            fused = self.proj(combined)
            return fused

        elif self.fusion_type == "attention":
            # Treat each modality rep as a "token"
            stacked = torch.stack(reps, dim=1)  # (B, M, D)
            # Self‑attention over modalities
            attn_out, _ = self.attention(stacked, stacked, stacked)
            # Mean over modalities
            fused = attn_out.mean(dim=1)
            fused = self.output_proj(fused)
            return fused

        elif self.fusion_type == "gated":
            # Weighted sum with learned gates
            weighted = []
            for mod, feat in zip(features.keys(), reps):
                weight = torch.sigmoid(self.gates[mod])
                weighted.append(weight * feat)
            fused = torch.stack(weighted, dim=0).sum(dim=0)
            fused = self.proj(fused)
            return fused
