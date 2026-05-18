"""
Fairness metrics and hypervolume evaluation for mizan‑balanced models.
"""

import numpy as np
from typing import List, Tuple


def fairness_utility_hypervolume(
    utility: np.ndarray,
    fairness: np.ndarray,
    ref_point: Tuple[float, float] = (0.0, 1.0),
) -> float:
    """
    Compute the hypervolume under the Pareto front of (utility, fairness).

    Args:
        utility: 1D array (higher is better)
        fairness: 1D array (lower disparity is better, so we use 1 - disparity)
        ref_point: worst acceptable point (utility_min, fairness_min)
    Returns:
        hypervolume (larger = better Pareto front)
    """
    # Convert to minimization problem: we minimize ( -utility, fairness )
    points = np.column_stack([-utility, fairness])
    # Simple Monte‑Carlo hypervolume (exact for small sets)
    # Sort by first objective
    sorted_idx = np.argsort(points[:, 0])
    points = points[sorted_idx]
    hv = 0.0
    x_ref, y_ref = ref_point
    for i in range(len(points)):
        x_i, y_i = points[i]
        x_next = points[i + 1][0] if i + 1 < len(points) else x_ref
        width = x_next - x_i
        height = y_i - y_ref
        if height > 0:
            hv += width * height
    return max(0.0, hv)


def mizan_score(
    utility: float,
    fairness: float,
    alpha: float = 0.5,
) -> float:
    """
    Composite score combining utility and fairness into a single mizan‑balanced metric.
    Score = α * utility_norm + (1‑α) * (1 − fairness_norm)
    """
    # Simple linear combination; assume inputs already normalized [0,1]
    return alpha * utility + (1 - alpha) * (1 - fairness)
