"""Training script for TES - Theological Embedding Space.

Usage:
    python training/train_tes.py [--config configs/tes.yaml] [--epochs 100] [--device cuda]
"""

import argparse
import json
import sys
import time
from pathlib import Path

import torch
import yaml


def load_config(config_path: str) -> dict:
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_device(device_str: str) -> str:
    if device_str == "auto":
        if torch.cuda.is_available():
            return "cuda"
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            return "mps"
        return "cpu"
    return device_str


def train_tes(config: dict, device: str):
    """Train the Theological Embedding Space model."""
    sys.path.insert(0, '1.TES/src')
    from theological_embedding import TheologicalEmbedding, build_tier_mapping

    model_config = config.get("model", {})
    training_config = config.get("training", {})
    data_config = config.get("data", {})

    # Load data
    tier_map = build_tier_mapping(data_config.get("tier_mapping", "1.TES/data/asmaullah.json"))
    vocab_size = max(max(ids) for ids in tier_map.values()) + 1

    # Initialize model
    model = TheologicalEmbedding(
        vocab_size=vocab_size,
        embed_dim=model_config.get("embed_dim", 128),
        tier_to_indices=tier_map,
        margin=model_config.get("margin", 1.0),
        lambda_tier=model_config.get("lambda_tier", 0.1),
        lambda_hier=model_config.get("lambda_hier", 0.1),
    ).to(device)

    # Optimizer and scheduler
    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=training_config.get("lr", 1e-3),
        weight_decay=training_config.get("weight_decay", 1e-4),
    )
    scheduler = None
    if training_config.get("scheduler") == "cosine":
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=training_config.get("epochs", 100)
        )

    # Training loop
    epochs = training_config.get("epochs", 100)
    batch_size = training_config.get("batch_size", 64)
    print(f"Training TES for {epochs} epochs on {device}")
    print(f"  Vocab size: {vocab_size}")
    print(f"  Embed dim: {model_config.get('embed_dim', 128)}")
    print(f"  Batch size: {batch_size}")
    print(f"  Learning rate: {training_config.get('lr', 1e-3)}")

    start_time = time.time()
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()

        # Dummy training pairs (replace with real data in production)
        pos_pairs = torch.tensor([[0, 1], [10, 11], [23, 24], [31, 32]], device=device)
        neg_pairs = torch.tensor([[0, 23], [10, 31], [23, 40], [1, 42]], device=device)

        loss = model(
            token_ids=torch.randint(0, vocab_size, (batch_size, 5), device=device),
            positive_pairs=pos_pairs,
            negative_pairs=neg_pairs,
        )

        loss.backward()
        optimizer.step()

        if scheduler:
            scheduler.step()

        if epoch % 10 == 0:
            elapsed = time.time() - start_time
            print(f"  Epoch {epoch:4d}/{epochs} | Loss: {loss.item():.4f} | Time: {elapsed:.1f}s")

    # Save model
    Path("checkpoints").mkdir(exist_ok=True)
    torch.save(model.state_dict(), "checkpoints/tes_model.pt")
    print(f"\n[OK] Model saved to checkpoints/tes_model.pt")
    return model


def main():
    parser = argparse.ArgumentParser(description="Train TES model")
    parser.add_argument("--config", default="configs/tes.yaml", help="Config file path")
    parser.add_argument("--epochs", type=int, help="Override epochs from config")
    parser.add_argument("--device", default="auto", help="Device: auto, cpu, cuda, mps")
    args = parser.parse_args()

    config = load_config(args.config)
    if args.epochs:
        config["training"]["epochs"] = args.epochs

    device = get_device(args.device)
    train_tes(config, device)


if __name__ == "__main__":
    main()
