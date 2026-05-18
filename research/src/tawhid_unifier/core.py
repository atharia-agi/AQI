"""
Core TawhidUnifier: a single transformer backbone that ingests multimodal inputs
and produces unified representations with a shared ontological space.
"""

import torch
import torch.nn as nn
from transformers import AutoModel, AutoConfig
from typing import Dict, Optional, Tuple


class TawhidUnifier(nn.Module):
    """
    Unified world model inspired by Tawhid (Oneness).

    Instead of separate encoders per modality, we use a single transformer
    with modality-specific embeddings, but all data flows through the same
    attention matrix, enforcing coherence by construction.

    Args:
        backbone: HuggingFace model name (default: bert-base-uncased)
        modalities: list of modality strings (e.g., ['text', 'vision', 'audio'])
        modality_dim: embedding dim per modality (default: 768)
        max_len: max sequence length per modality
        num_slots: number of latent "concept slots" for shared ontology
    """

    def __init__(
        self,
        backbone: str = "bert-base-uncased",
        modalities: list = None,
        modality_dim: int = 768,
        max_len: int = 512,
        num_slots: int = 256,
    ):
        super().__init__()
        self.modalities = modalities or ["text"]
        self.modality_dim = modality_dim
        self.max_len = max_len
        self.num_slots = num_slots

        # Shared transformer backbone
        self.backbone_cfg = AutoConfig.from_pretrained(backbone)
        self.backbone = AutoModel.from_pretrained(backbone, config=self.backbone_cfg)

        # Modality-specific input embeddings (as adapters)
        self.modality_embeddings = nn.ModuleDict(
            {mod: nn.Embedding(1, modality_dim) for mod in self.modalities}
        )

        # Shared ontological slots (learnable)
        self.slot_embeddings = nn.Parameter(torch.randn(num_slots, modality_dim))

        # Output projection to shared space
        self.output_proj = nn.Linear(modality_dim, modality_dim)

        # Slot attention: assign input tokens to ontology slots
        self.slot_attention = nn.MultiheadAttention(
            embed_dim=modality_dim,
            num_heads=8,
            batch_first=True,
        )

    def forward(
        self,
        inputs: Dict[str, torch.Tensor],
        attention_mask: Optional[Dict[str, torch.Tensor]] = None,
    ) -> Dict[str, torch.Tensor]:
        """
        Forward pass for multimodal inputs.

        Args:
            inputs: dict mapping modality -> (batch, seq_len) token IDs or features
            attention_mask: optional dict of masks per modality

        Returns:
            dict with:
                - unified_representation: (batch, slots, dim)
                - modality_features: dict of (batch, seq_len, dim) per modality
                - consistency_loss: scalar tensor (encourages cross-modal alignment)
        """
        modality_features = {}
        all_features = []
        batch_size = next(iter(inputs.values())).size(0)

        # Encode each modality through shared backbone with modality embedding
        for mod, tokens in inputs.items():
            # Add modality embedding to input embeddings
            input_embeds = self.backbone.embeddings(tokens)
            mod_emb = self.modality_embeddings[mod](torch.zeros(batch_size, 1, dtype=torch.long, device=tokens.device))
            input_embeds = input_embeds + mod_emb

            if attention_mask and mod in attention_mask:
                outputs = self.backbone(
                    inputs_embeds=input_embeds,
                    attention_mask=attention_mask[mod],
                    return_dict=True,
                )
            else:
                outputs = self.backbone(
                    inputs_embeds=input_embeds,
                    return_dict=True,
                )
            # Use [CLS] token representation
            cls_repr = outputs.last_hidden_state[:, 0, :]  # (B, D)
            modality_features[mod] = cls_repr
            all_features.append(cls_repr)

        # Stack modality features: (B, M, D)
        stacked = torch.stack(all_features, dim=1)

        # Enforce coherence: minimize variance across modalities (Tawhid consistency)
        # This is a simple consistency loss; more sophisticated versions could use
        # covariance matrices, contrastive learning, or adversarial training.
        consistency_loss = stacked.var(dim=1).mean()

        # Aggregate into shared ontological slots
        # Repeat slot embeddings for batch
        slots = self.slot_embeddings.unsqueeze(0).expand(batch_size, -1, -1)  # (B, S, D)

        # Cross-attention: slots query from concatenated modality features
        query = slots
        key = torch.cat(all_features, dim=1).unsqueeze(1)  # (B, 1, D) -> will broadcast
        value = torch.cat(all_features, dim=1).unsqueeze(1)

        # Actually we need proper key/value: stack as sequence
        key = torch.stack(all_features, dim=1)  # (B, M, D)
        value = key

        unified, attn_weights = self.slot_attention(
            query=slots,
            key=key,
            value=value,
        )  # unified: (B, S, D)

        # Project to shared space
        unified = self.output_proj(unified)

        return {
            "unified_representation": unified,  # (B, S, D)
            "modality_features": modality_features,
            "consistency_loss": consistency_loss,
        }

    def get_ontological_slot_embeddings(self) -> torch.Tensor:
        """Return the learned ontological slots (num_slots, dim)."""
        return self.slot_embeddings.detach().cpu()
