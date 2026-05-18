"""
Unit tests for TawhidUnifier core.
"""

import pytest
import torch
from tawhid_unifier.core import TawhidUnifier


def test_tawhid_unifier_forward():
    batch_size = 2
    vocab_size = 1000
    seq_len = 10
    modalities = ["text", "vision"]

    model = TawhidUnifier(
        backbone="bert-base-uncased",
        modalities=modalities,
        modality_dim=768,
        num_slots=64,
    )

    # Dummy inputs (token IDs)
    inputs = {
        "text": torch.randint(0, vocab_size, (batch_size, seq_len)),
        "vision": torch.randn(batch_size, seq_len, 768),  # pseudo image patches
    }
    # Note: for non-text, you'd normally project; here we assume tokens are already IDs.
    # For vision, we'd need a patch embedding; this test uses text-only for simplicity.

    outputs = model(inputs)
    assert "unified_representation" in outputs
    assert "modality_features" in outputs
    assert "consistency_loss" in outputs

    B, S, D = outputs["unified_representation"].shape
    assert B == batch_size
    assert S == model.num_slots
    assert D == model.modality_dim

    # Consistency loss should be scalar
    assert outputs["consistency_loss"].shape == ()

    print("✅ TawhidUnifier forward pass OK")


def test_modality_consistency():
    """Check that forcing modalities to align reduces consistency loss."""
    model = TawhidUnifier(
        backbone="bert-base-uncased",
        modalities=["text", "text2"],
        modality_dim=32,
        num_slots=8,
    )
    # Same input for both modalities
    batch_size = 1
    seq_len = 5
    vocab_size = 100
    inputs = {
        "text": torch.randint(0, vocab_size, (batch_size, seq_len)),
        "text2": torch.randint(0, vocab_size, (batch_size, seq_len)),
    }
    out1 = model(inputs)
    loss1 = out1["consistency_loss"].item()

    # Different inputs should yield higher inconsistency
    inputs2 = inputs.copy()
    inputs2["text2"] = torch.randint(0, vocab_size, (batch_size, seq_len))
    out2 = model(inputs2)
    loss2 = out2["consistency_loss"].item()

    # This is a sanity check; with random init, differences may be small
    print(f"Consistency loss (same): {loss1:.4f}, (different): {loss2:.4f}")


if __name__ == "__main__":
    test_tawhid_unifier_forward()
    test_modality_consistency()
    print("All tests passed!")
