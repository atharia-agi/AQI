"""
Tawhid-AI: Unified World Model Architecture

Principle: "Al-Ittihad" (Unification) — integrating multimodal streams into consistent ontology.
Inspired by Quranic concept of Tawhid (oneness of God) → single coherent representation.
"""

from .core import TawhidUnifier
from .losses import ConsistencyLoss, OntologyAlignmentLoss
from .fusion import MultimodalFusion, StreamProcessor

__version__ = "0.1.0.dev0"
__author__ = "Tawhid-AI Research Collective"
__all__ = [
    "TawhidUnifier",
    "ConsistencyLoss",
    "OntologyAlignmentLoss",
    "MultimodalFusion",
    "StreamProcessor",
]
