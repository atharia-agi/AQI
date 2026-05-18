"""
MizanRegularizer: Enforces dynamic equilibrium among multiple objectives.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class MizanRegularizer(nn.Module):
    """
    Implements the principle of mizan (balance) as a differentiable regularizer.

    Given a vector of losses L = [l1, ..., ln], we learn a weight distribution
    w = softmax(z) that balances them. The regularizer penalizes:
      - Variance of w (to avoid dominance)
      - KL divergence from uniform (to avoid collapse to uniform when tasks differ)

    Total loss: L_total = Σ w_i l_i + λ * (1/n Σ (w_i - μ)^2) + γ * KL(Uniform || w)

    This operationalizes the Quranic verse: "He has set up the balance (mizan) to
    prevent you from transgressing the limits." (55:7-9)
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
            losses: Tensor of shape (num_objectives,) or (batch, num_objectives)
        Returns:
            regularized scalar loss
        """
        if losses.dim() == 2:
            losses = losses.mean(dim=0)  # Average over batch → (num_objectives,)
        # Softmax weights
        weights = F.softmax(self.raw_weights, dim=0)
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

    def get_weights(self) -> torch.Tensor:
        """Return current weight distribution (softmax)."""
        return F.softmax(self.raw_weights, dim=0).detach()
