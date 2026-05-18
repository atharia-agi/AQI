"""
Quick demo: TawhidUnifier with dummy multimodal inputs.
Run: python demo_tawhid.py
Requires: torch, transformers
"""

import torch
from tawhid_unifier.core import TawhidUnifier


def main():
    print("=== Tawhid‑AI Demo ===")
    # Hyper‑parameters (small for demo)
    modalities = ["text", "vision"]
    batch_size = 2
    seq_len = 8
    vocab_size = 5000

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Initialize model
    model = TawhidUnifier(
        backbone="bert-base-uncased",
        modalities=modalities,
        modality_dim=768,
        num_slots=32,
    ).to(device)

    # Dummy batch
    text_ids = torch.randint(0, vocab_size, (batch_size, seq_len), device=device)
    vision_patches = torch.randn(batch_size, seq_len, 768, device=device)  # pretend visual tokens

    inputs = {
        "text": text_ids,
        "vision": vision_patches,  # note: in real use, vision tokens need separate patch embedder
    }

    # Forward pass
    with torch.no_grad():
        outputs = model(inputs)

    print(f"Unified representation shape: {outputs['unified_representation'].shape}")
    print(f"Consistency loss: {outputs['consistency_loss'].item():.4f}")
    print(
        f"Modality features: "
        + ", ".join(f"{k}: {v.shape}" for k, v in outputs["modality_features"].items())
    )
    print("\n✅ Demo complete. Ready for integration.")


if __name__ == "__main__":
    main()
