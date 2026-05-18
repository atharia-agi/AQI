"""
Nass-Based Causal Discovery (NBCD)

Extends standard causal graphs with a latent "Divine Will" node that can
intervene in natural causal chains based on hadith descriptions of miracles.

We use a structural causal model (SCM) where:
    X ←Natural Causes → Y
    X ←Divine Will → Y  (possible intervention)

The Divine Will node is unobserved but its intervention probability is
calibrated from textual sources: hadith give prior odds that certain
actions (e.g., prayer) can cause otherwise impossible outcomes.
"""

import numpy as np
import networkx as nx
from scipy import stats
from typing import Dict, List, Tuple, Optional


class DivineInterventionPrior:
    """
    Stores prior probabilities for divine intervention on edges.
    Derived from hadith reliability (mutawatir > ahad > da'if) and
    semantic proximity to worship/righteousness.
    """

    def __init__(self):
        # Default intervention prior (log-odds) per edge type
        self.base_prior = -3.0  # log(0.05) — rare but possible
        self.edge_boost = {
            "prayer": 2.0,      # Salat can change decree
            "dhikr": 1.5,
            "charity": 1.0,
            "dua": 1.8,
            "righteous": 0.5,
        }

    def get_log_odds(self, edge_type: str) -> float:
        boost = self.edge_boost.get(edge_type, 0.0)
        return self.base_prior + boost

    def sample_intervention(self, edge_type: str) -> bool:
        log_odds = self.get_log_odds(edge_type)
        p = 1.0 / (1.0 + np.exp(-log_odds))
        return np.random.random() < p


class NBCDGraph:
    """
    Causal graph with latent Divine Will interventions.
    """

    def __init__(self):
        self.G = nx.DiGraph()
        self.divine_prior = DivineInterventionPrior()
        # Track which edges have possible divine intervention
        self.divine_edges = {}  # (u,v) -> edge_type

    def add_edge(self, u: str, v: str, natural_strength: float, edge_type: str = "default"):
        """Add a natural causal edge with strength."""
        self.G.add_edge(u, v, strength=natural_strength, type="natural")
        self.divine_edges[(u, v)] = edge_type

    def intervene(self, intervention_node: str) -> Dict[Tuple[str, str], float]:
        """
        Simulate divine intervention. For each edge where intervention_node is
        parent, there is a chance to strengthen/modify the causal effect.
        Returns a dict of edge → modified strength.
        """
        modifications = {}
        outgoing = list(self.G.out_edges(intervention_node, data=True))
        for u, v, data in outgoing:
            edge_type = self.divine_edges.get((u, v), "default")
            if self.divine_prior.sample_intervention(edge_type):
                # Miracle: boost strength dramatically
                modifications[(u, v)] = data["strength"] * 10.0
        return modifications

    def sample_observation(
        self,
        intervention_node: Optional[str] = None,
        noise_std: float = 0.1
    ) -> Dict[str, float]:
        """
        Sample a data point from the SCM. If intervention_node is provided,
        apply divine intervention with calibrated probability.
        Returns dict of node values.
        """
        # Topological order
        order = list(nx.topological_sort(self.G))
        values = {}

        # Apply intervention effects first
        intervention_mods = {}
        if intervention_node:
            intervention_mods = self.intervene(intervention_node)

        for node in order:
            # Find parents
            parents = list(self.G.predecessors(node))
            if not parents:
                # Exogenous
                values[node] = np.random.randn()
            else:
                # Weighted sum of parent values plus natural strength
                incoming = 0.0
                for p in parents:
                    edge_data = self.G.get_edge_data(p, node)
                    strength = edge_data["strength"]
                    # Check if this edge got modified by divine intervention
                    if (p, node) in intervention_mods:
                        strength = intervention_mods[(p, node)]
                    incoming += strength * values[p]
                # Add noise
                noise = np.random.randn() * noise_std
                values[node] = incoming + noise

        return values

    def estimate_divine_probability(
        self,
        data: List[Dict[str, float]],
        intervention_node: str,
        target_node: str,
        threshold: float = 3.0
    ) -> float:
        """
        Given observational data, estimate posterior probability that
        divine intervention occurred on edges from intervention_node to target_node.
        Uses simple outlier detection: if target values are > threshold SD above
        predicted by natural graph, attribute to divine intervention.
        """
        predictions = []
        for obs in data:
            # Predict target from natural graph only (no intervention)
            # For demo: simply compute linear predictor ignoring intervention
            parents = list(self.G.predecessors(target_node))
            pred = sum(self.G[p][target_node]['strength'] * obs.get(p, 0) for p in parents)
            predictions.append(pred)

        residuals = np.array([obs[target_node] - pred for obs, pred in zip(data, predictions)])
        outlier_count = (np.abs(residuals) > threshold).sum()
        p_est = outlier_count / len(data)
        return p_est
