"""Unit tests for DNO - Divine Names Ontology."""

import sys
import pytest
import torch

sys.path.insert(0, '3.DNO/src')
from names_optimizer import DivineNamesOptimizer, DEFAULT_ATTRIBUTES


@pytest.fixture
def dno():
    return DivineNamesOptimizer(
        attributes_config=DEFAULT_ATTRIBUTES,
        init_weights=[1.0, 1.0, 1.0, 0.8, 0.5, 0.3],
        learn_weights=True,
    )


class TestDivineNamesOptimizer:
    """Tests for DivineNamesOptimizer class."""

    def test_initialization(self, dno):
        assert dno is not None
        assert len(dno.attr_names) == 6

    def test_forward_returns_tuple(self, dno):
        logits = torch.randn(32, 2)
        labels = torch.randint(0, 2, (32,))
        result = dno.forward(logits, labels)
        assert isinstance(result, tuple)
        assert len(result) == 3

    def test_forward_loss_is_scalar(self, dno):
        logits = torch.randn(32, 2)
        labels = torch.randint(0, 2, (32,))
        total_loss, weights, losses = dno.forward(logits, labels)
        assert total_loss.dim() == 0

    def test_get_weights_returns_dict(self, dno):
        weights = dno.get_weights()
        assert isinstance(weights, dict)
        assert len(weights) == 6

    def test_weights_sum_to_one(self, dno):
        weights = dno.get_weights()
        total = sum(weights.values())
        assert abs(total - 1.0) < 1e-5
