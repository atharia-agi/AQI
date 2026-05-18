"""
Theological Embedding Space (TES)

Learn embeddings where vector geometry reflects ontological hierarchy:
Allah > malaikat > insan > haiwan > nabat > jamad.

Method: Contrastive learning with tier‑based negative sampling.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import json
from typing import List, Tuple, Dict


class TheologicalEmbedding(nn.Module):
    """
    Embedding layer where each token gets a vector whose norm encodes its
    ontological tier (higher tier = larger norm), and cosine similarity
    reflects “closeness in nature”.

    Tiers (higher = more fundamental/exalted):
        0 — Allah ( supra‑existent )
        1 — Malaikat (immaterial agents)
        2 — Ruh (spirits)
        3 — Insan (rational embodied)
        4 — Haiwan (living)
        5 — Nabat (growing)
        6 — Jamad (inanimate)

    Loss:
        L = L_contrastive + λ₁ * L_tier_norm + λ₂ * L_hierarchy
    """

    def __init__(
        self,
        vocab_size: int,
        embed_dim: int = 768,
        tier_to_indices: Dict[int, List[int]] = None,
        margin: float = 1.0,
        lambda_tier: float = 0.1,
        lambda_hier: float = 0.1,
    ):
        super().__init__()
        self.embed_dim = embed_dim
        self.margin = margin
        self.lambda_tier = lambda_tier
        self.lambda_hier = lambda_hier

        # Token embeddings
        self.embeddings = nn.Embedding(vocab_size, embed_dim)

        # Ontological tier for each token (0–6). Initialize all to tier 3 (human) by default.
        self.register_buffer("token_tiers", torch.full((vocab_size,), 3, dtype=torch.long))
        # Update tiers from provided mapping
        if tier_to_indices:
            for tier, indices in tier_to_indices.items():
                self.token_tiers[indices] = tier

        # Tier‑specific bias: higher tiers get larger norm
        self.tier_norm_scales = nn.Parameter(torch.ones(7))  # learned scale per tier

    def forward(
        self,
        token_ids: torch.LongTensor,
        positive_pairs: torch.LongTensor = None,
        negative_pairs: torch.LongTensor = None,
    ) -> torch.Tensor:
        """
        Args:
            token_ids: (batch, seq_len)
            positive_pairs: (batch, 2) — indices of tokens that should be similar
            negative_pairs: (batch, 2) — indices of tokens that should be dissimilar

        Returns:
            total loss (if pairs provided) or just embeddings
        """
        emb = self.embeddings(token_ids)  # (B, L, D)

        if positive_pairs is None or negative_pairs is None:
            return emb

        # Contrastive loss
        pos_emb = self.embeddings(positive_pairs[:, 0])
        pos_target = self.embeddings(positive_pairs[:, 1])
        neg_emb = self.embeddings(negative_pairs[:, 0])
        neg_target = self.embeddings(negative_pairs[:, 1])

        pos_sim = torch.cosine_similarity(pos_emb, pos_target, dim=-1)
        neg_sim = torch.cosine_similarity(neg_emb, neg_target, dim=-1)

        L_contrastive = torch.relu(self.margin - pos_sim + neg_sim).mean()

        # Tier norm loss: encourage norms to increase with tier
        all_emb = self.embeddings.weight  # (V, D)
        norms = all_emb.norm(dim=1)  # (V,)
        tier_mask = self.token_tiers.unsqueeze(1)  # (V, 1)
        # We want: for t1 > t2, E[norm|t1] > E[norm|t2]
        tier_norms = []
        for t in range(7):
            mask = self.token_tiers == t
            if mask.any():
                tier_norms.append(norms[mask].mean())
            else:
                tier_norms.append(torch.tensor(0.0, device=norms.device))
        tier_norms = torch.stack(tier_norms)  # (7,)

        # Penalize if higher tier has lower norm than lower tier
        L_tier = 0.0
        for t in range(6):
            for t2 in range(t + 1, 7):
                if tier_norms[t2] < tier_norms[t]:
                    L_tier += (tier_norms[t] - tier_norms[t2]) ** 2
        L_tier = self.lambda_tier * L_tier

        # Hierarchy loss: within‑tier items should be closer than cross‑tier items (by tier gap)
        # Simplified: encourage norms to correlate with tier index
        desired_norms = torch.arange(7, device=self.token_tiers.device).float() + 1
        L_hier = self.lambda_hier * F.mse_loss(tier_norms, desired_norms)

        total = L_contrastive + L_tier + L_hier

        return total

    def get_ontological_position(self, token_id: int) -> Dict[str, torch.Tensor]:
        """Return embedding, tier, and norm for analysis."""
        emb = self.embeddings(torch.tensor([token_id]))
        tier = self.token_tiers[token_id].item()
        norm = emb.norm().item()
        return {
            "embedding": emb.squeeze(0),
            "tier": tier,
            "norm": norm,
        }

    def query_similarity(self, token_a: int, token_b: int) -> float:
        """Cosine similarity between two tokens."""
        with torch.no_grad():
            emb_a = self.embeddings(torch.tensor([token_a]))
            emb_b = self.embeddings(torch.tensor([token_b]))
            return torch.cosine_similarity(emb_a, emb_b, dim=-1).item()


# Utility to build tier mapping from JSON data file
def build_tier_mapping(data_path: str) -> Dict[int, List[int]]:
    """
    Expect JSON:
    {
        "tiers": {
            "0": ["allah", "entity_allah", ...],
            "1": ["malaikat_jibril", "malaikat_mikail", ...],
            ...
        }
    }
    """
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    tiers = {}
    for tier_str, tokens in data["tiers"].items():
        tier = int(tier_str)
        # We'll need token IDs from tokenizer; for now, assume tokens are already IDs
        # In practice, integrate with tokenizer
        tiers[tier] = tokens  # list of int IDs
    return tiers
