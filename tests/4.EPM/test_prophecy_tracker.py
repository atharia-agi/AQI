"""Unit tests for EPM - Eschatological Predictive Modeling."""

import sys
import pytest

sys.path.insert(0, '4.EPM/src')
from prophecy_tracker import ProphecyBayesNet, SignNode


@pytest.fixture
def bayes_net():
    n = ProphecyBayesNet()
    n.add_node(SignNode(
        name="trust_liar", category="minor",
        prior_p_manifest=0.01,
    ))
    n.add_node(SignNode(
        name="muslims_fight", category="minor",
        prior_p_manifest=0.005,
    ))
    return n


class TestProphecyBayesNet:
    """Tests for ProphecyBayesNet class."""

    def test_add_node(self, bayes_net):
        assert len(bayes_net.nodes) == 2

    def test_update_posterior_returns_probability(self, bayes_net):
        observations = {"trust_liar": True}
        p = bayes_net.update_posterior(observations, n_particles=1000)
        assert isinstance(p, float)
        assert 0.0 <= p <= 1.0

    def test_update_posterior_with_multiple_observations(self, bayes_net):
        observations = {"trust_liar": True, "muslims_fight": False}
        p = bayes_net.update_posterior(observations, n_particles=1000)
        assert 0.0 <= p <= 1.0


class TestSignNode:
    """Tests for SignNode class."""

    def test_creation(self):
        node = SignNode(
            name="test_sign", category="major",
            prior_p_manifest=0.5,
            description="A test sign",
        )
        assert node.name == "test_sign"
        assert node.category == "major"
        assert node.prior == 0.5
