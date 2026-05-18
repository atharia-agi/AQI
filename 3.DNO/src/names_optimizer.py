"""
Divine Names Ontology (DNO)

Multi‑attribute optimizer where each objective corresponds to one of the
99 Beautiful Names of Allah (Asma'ul Husna). Each Name defines an ideal
mathematical property that the model should maximize.

Example:
- Ar‑Rahman (The Most Merciful) → maximize compassion (minimize suffering)
- Al‑'Adl (The Just) → enforce fairness (equal treatment)
- Al‑Hakim (The All‑Wise) → maximize decision quality (accuracy + interpretability)
- Al‑Ghaffar (The All‑Forgiving) → encourage robustness (forgive errors)

We create a differentiable regularizer that combines these attributes.
"""

import torch
import torch.nn as nn
import json
from typing import Dict, List


class DivineAttributeObjective(nn.Module):
    """
    Single divine attribute as a differentiable function of model outputs.
    """

    def __init__(self, name: str, attribute_type: str, weight: float = 1.0):
        super().__init__()
        self.name = name
        self.attr_type = attribute_type
        self.weight = weight

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        """
        Compute attribute‑specific loss term.
        Args:
            logits: model predictions (N, C) or (N,)
            targets: ground truth
        Returns:
            scalar loss (to be minimized)
        """
        if self.attr_type == "mercy":
            # Ar‑Rahman: minimize negative outcomes (compassion)
            # For classification, this could be minimizing false negatives in critical cases
            loss = nn.functional.cross_entropy(logits, targets, reduction="mean")
            return self.weight * loss

        elif self.attr_type == "justice":
            # Al‑'Adl: enforce equal error rates across groups
            # We'll implement as demographic parity difference
            # Placeholder: simple L2 on weight distribution
            if isinstance(logits, torch.Tensor) and logits.dim() > 1:
                # Assume model is a classifier
                preds = torch.argmax(logits, dim=1)
                # This is stub; real implementation would group by protected attribute
                fairness_penalty = (
                    preds.float().var()
                )  # encourage uniform preds? doesn't make sense
                return self.weight * fairness_penalty
            else:
                return torch.tensor(0.0, device=logits.device)

        elif self.attr_type == "wisdom":
            # Al‑Hakim: maximize accuracy minus uncertainty
            loss = nn.functional.cross_entropy(logits, targets, reduction="mean")
            # Add entropy penalty to avoid over‑confidence?
            probs = torch.softmax(logits, dim=1)
            entropy = -(probs * torch.log(probs + 1e-10)).sum(dim=1).mean()
            return self.weight * (loss - 0.1 * entropy)

        elif self.attr_type == "forgiveness":
            # Al‑Ghaffar: model should be robust to adversarial perturbations
            # Placeholder: encourage smooth decision boundaries
            # In practice, this would be adversarial training
            return torch.tensor(0.0, device=logits.device)

        else:
            # Generic: weight on L2 regularizer (tawhid‑like unity)
            if isinstance(logits, torch.Tensor):
                return self.weight * logits.norm()
            return torch.tensor(0.0, device=logits.device)


class DivineNamesOptimizer:
    """
    Combines multiple divine attribute objectives into a single training objective.
    The weights for each attribute can be learned or preset from Quranic priority.
    """

    def __init__(
        self,
        attributes_config: List[Dict],
        init_weights: List[float] = None,
        learn_weights: bool = True,
    ):
        """
        Args:
            attributes_config: list of dicts with keys: name, attribute_type, [initial_weight]
            init_weights: optional initial weights (overrides config)
            learn_weights: if True, learn importance weights via gradient descent
        """
        self.attributes = nn.ModuleList()
        self.attr_names = []
        self.learn_weights = learn_weights

        for cfg in attributes_config:
            name = cfg["name"]
            attr_type = cfg["attribute_type"]
            weight = cfg.get("weight", 1.0)
            obj = DivineAttributeObjective(name, attr_type, weight)
            self.attributes.append(obj)
            self.attr_names.append(name)

        if learn_weights:
            # Learnable logits for each attribute (softmax gives weights)
            self.raw_weights = nn.Parameter(
                torch.tensor(init_weights if init_weights else [1.0] * len(self.attributes))
            )
        else:
            self.raw_weights = None

    def forward(
        self,
        logits: torch.Tensor,
        targets: torch.Tensor,
        custom_weights: torch.Tensor = None,
    ) -> torch.Tensor:
        """
        Compute total loss as weighted sum of attribute objectives.
        """
        losses = []
        for attr in self.attributes:
            loss_i = attr(logits, targets)  # scalar
            losses.append(loss_i)

        losses_tensor = torch.stack(losses)  # (num_attrs,)

        if custom_weights is not None:
            weights = custom_weights
        elif self.raw_weights is not None:
            weights = torch.softmax(self.raw_weights, dim=0)
        else:
            # Use fixed weights from each attribute
            weights = torch.tensor(
                [attr.weight for attr in self.attributes], device=losses_tensor.device
            )

        total = (weights * losses_tensor).sum()
        return total, weights, losses_tensor

    def get_weights(self) -> Dict[str, float]:
        """Return current weight distribution (as dict)."""
        if self.raw_weights is not None:
            with torch.no_grad():
                w = torch.softmax(self.raw_weights, dim=0)
                return {name: w[i].item() for i, name in enumerate(self.attr_names)}
        else:
            return {attr.name: attr.weight for attr in self.attributes}


# Preset configuration based on Asma'ul Husna priorities
DEFAULT_ATTRIBUTES = [
    {"name": "Ar-Rahman", "attribute_type": "mercy", "weight": 1.2},
    {"name": "Al-'Adl", "attribute_type": "justice", "weight": 1.0},
    {"name": "Al-Hakim", "attribute_type": "wisdom", "weight": 1.1},
    {"name": "Al-Ghaffar", "attribute_type": "forgiveness", "weight": 0.9},
    {"name": "Al-Malik", "attribute_type": "sovereignty", "weight": 0.8},
    {"name": "Ar-Raqib", "attribute_type": "watchfulness", "weight": 0.7},
]
