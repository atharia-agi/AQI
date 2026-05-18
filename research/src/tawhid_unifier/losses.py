"""
Loss functions for Tawhid-AI: Consistency and Ontology Alignment.

These losses operationalize the principles of Tawhid (unity) and Mizan (balance).
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict


class ConsistencyLoss(nn.Module):
    """
    Enforces consistency across modalities by minimizing variance of their
    representations. Inspired by the Quranic emphasis on unity (Tawhid).

    Formula: L_cons = Var( [f_m]_{m in modalities} )
    where f_m is the feature vector for modality m.
    """

    def __init__(self, reduction: str = "mean"):
        super().__init__()
        self.reduction = reduction

    def forward(self, modality_features: Dict[str, torch.Tensor]) -> torch.Tensor:
        """
        Args:
            modality_features: dict mapping modality -> (batch, dim) features
        Returns:
            scalar consistency loss (lower = more consistent)
        """
        # Stack features: (batch, num_modalities, dim)
        stacked = torch.stack(list(modality_features.values()), dim=1)  # (B, M, D)
        # Compute variance across modalities per batch/dim
        var_per_batch = stacked.var(dim=1, unbiased=False).mean(dim=1)  # (B,)
        if self.reduction == "mean":
            return var_per_batch.mean()
        elif self.reduction == "sum":
            return var_per_batch.sum()
        else:
            return var_per_batch  # (B,)


class OntologyAlignmentLoss(nn.Module):
    """
    Aligns modality-specific embeddings to the shared ontological slots.
    Minimizes L2 distance between modality features and their assigned slots.
    """

    def __init__(self, temperature: float = 1.0):
        super().__init__()
        self.temperature = temperature

    def forward(
        self,
        modality_features: Dict[str, torch.Tensor],
        slot_embeddings: torch.Tensor,
        attention_weights: torch.Tensor,
    ) -> torch.Tensor:
        """
        Args:
            modality_features: dict of (B, D)
            slot_embeddings: (num_slots, D)
            attention_weights: (B, num_slots, num_modalities) from slot attention
        Returns:
            alignment loss scalar
        """
        # For each modality, compute weighted sum of slots
        # attention_weights: (B, S, M)
        # slot_embeddings: (S, D)
        # We want sum_m (weight_m * slot_embeddings) ≈ modality_features
        loss = 0.0
        num_modalities = len(modality_features)
        for i, (mod, feat) in enumerate(modality_features.items()):
            # Weighted combination of slots for this modality
            weights = attention_weights[:, :, i]  # (B, S)
            weighted_slots = torch.einsum("bs,sd->bd", weights, slot_embeddings)
            loss = loss + F.mse_loss(weighted_slots, feat)
        return loss / num_modalities


class MizanRegularizer(nn.Module):
    """
    Regularizer for multi-objective learning that enforces balance (mizan).
    Penalizes extreme weight distributions across objectives.

    Given per-objective losses L_i, and weights w_i (softmax of raw logits z_i),
    we add penalty: λ * (1/n) Σ (w_i - avg)^2 + γ * KL(Uniform || w)
    """

    def __init__(
        self,
        num_objectives: int,
        lambda_balance: float = 0.1,
        gamma_uniform: float = 0.01,
        epsilon: float = 1e-8,
    ):
        super().__init__()
        self.num_objectives = num_objectives
        self.lambda_balance = lambda_balance
        self.gamma_uniform = gamma_uniform
        self.epsilon = epsilon
        # Learnable raw weights (logits) for each objective
        self.raw_weights = nn.Parameter(torch.zeros(num_objectives))

    def forward(self, losses: torch.Tensor) -> torch.Tensor:
        """
        Args:
            losses: tensor of shape (batch, num_objectives) or (num_objectives,)
        Returns:
            regularized total loss (scalar)
        """
        # Normalize losses to [0,1] via min‑max across objectives (simple version)
        if losses.dim() == 2:
            losses = losses.mean(dim=0)  # (num_objectives,)
        # Compute weight distribution via softmax
        weights = F.softmax(self.raw_weights, dim=0)  # (num_objectives,)
        # Weighted sum of losses
        weighted_loss = (weights * losses).sum()
        # Balance penalty: variance of weights
        mean_w = weights.mean()
        balance_penalty = ((weights - mean_w) ** 2).mean()
        # Uniformity penalty: KL(Uniform || weights)
        uniform = torch.ones_like(weights) / self.num_objectives
        kl_uniform = F.kl_div(
            F.log_softmax(self.raw_weights, dim=0),
            uniform,
            reduction="sum",
        )
        total_penalty = self.lambda_balance * balance_penalty + self.gamma_uniform * kl_uniform
        return weighted_loss + total_penalty
