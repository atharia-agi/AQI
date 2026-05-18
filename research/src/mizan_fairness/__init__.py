"""
Mizan-Fairness: Multi-Objective Fairness Regularizer based on divine balance (mizan).
"""

from .regularizer import MizanRegularizer
from .metrics import fairness_utility_hypervolume, mizan_score

__version__ = "0.1.0.dev0"
__all__ = [
    "MizanRegularizer",
    "fairness_utility_hypervolume",
    "mizan_score",
]
