"""Unit tests for NBCD - Nass-Based Causal Discovery."""

import sys
import pytest
import numpy as np

sys.path.insert(0, '2.NBCD/src')
from causal_graph import NBCDGraph, DivineInterventionPrior


@pytest.fixture
def graph():
    g = NBCDGraph()
    g.add_edge("salat_prayer", "heart_peace", 0.3, edge_type="prayer")
    g.add_edge("sadaqah_charity", "barakah_blessing", 0.2, edge_type="charity")
    return g


@pytest.fixture
def prior():
    return DivineInterventionPrior()


class TestNBCDGraph:
    """Tests for NBCDGraph class."""

    def test_add_edge(self, graph):
        assert graph.G.number_of_edges() == 2

    def test_sample_observation(self, graph):
        obs = graph.sample_observation(noise_std=0.1)
        assert isinstance(obs, dict)
        assert len(obs) > 0

    def test_sample_with_intervention(self, graph):
        obs = graph.sample_observation(
            intervention_node="salat_prayer", noise_std=0.1,
        )
        assert isinstance(obs, dict)

    def test_estimate_divine_probability(self, graph):
        data = [graph.sample_observation() for _ in range(50)]
        p = graph.estimate_divine_probability(
            data, intervention_node="salat_prayer",
            target_node="heart_peace", threshold=2.0,
        )
        assert 0.0 <= p <= 1.0


class TestDivineInterventionPrior:
    """Tests for DivineInterventionPrior class."""

    def test_prior_has_base_prior(self, prior):
        assert hasattr(prior, "base_prior")

    def test_get_log_odds(self, prior):
        log_odds = prior.get_log_odds("prayer")
        assert isinstance(log_odds, float)
