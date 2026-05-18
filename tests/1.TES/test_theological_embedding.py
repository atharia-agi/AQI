"""Unit tests for TES - Theological Embedding Space."""

import sys
import pytest
import torch

sys.path.insert(0, '1.TES/src')
from theological_embedding import TheologicalEmbedding, build_tier_mapping


@pytest.fixture
def tier_map():
    return build_tier_mapping("1.TES/data/asmaullah.json")


@pytest.fixture
def model(tier_map):
    vocab_size = max(max(ids) for ids in tier_map.values()) + 1
    return TheologicalEmbedding(
        vocab_size=vocab_size, embed_dim=64, tier_to_indices=tier_map,
    )


class TestTheologicalEmbedding:
    """Tests for TheologicalEmbedding class."""

    def test_model_initialization(self, model):
        assert model is not None
        assert model.embed_dim == 64

    def test_forward_pass(self, model, tier_map):
        vocab_size = max(max(ids) for ids in tier_map.values()) + 1
        pos_pairs = torch.tensor([[0, 1], [10, 11]])
        neg_pairs = torch.tensor([[0, 23], [10, 31]])
        loss = model(
            token_ids=torch.randint(0, vocab_size, (4, 5)),
            positive_pairs=pos_pairs,
            negative_pairs=neg_pairs,
        )
        assert loss.item() >= 0
        assert loss.requires_grad

    def test_get_ontological_position(self, model):
        pos = model.get_ontological_position(0)
        assert "tier" in pos
        assert "norm" in pos
        assert pos["norm"] > 0

    def test_query_similarity(self, model):
        sim = model.query_similarity(0, 0)
        assert abs(sim - 1.0) < 1e-5

    def test_similarity_different_tokens(self, model):
        sim = model.query_similarity(0, 10)
        assert -1.0 <= sim <= 1.0


class TestBuildTierMapping:
    """Tests for build_tier_mapping function."""

    def test_returns_dict(self, tier_map):
        assert isinstance(tier_map, dict)

    def test_has_multiple_tiers(self, tier_map):
        assert len(tier_map) > 1

    def test_tier_values_are_lists(self, tier_map):
        for tier, indices in tier_map.items():
            assert isinstance(indices, list)
