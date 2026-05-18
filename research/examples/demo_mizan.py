"""
Demo: MizanRegularizer for multi‑objective optimization.
Run: python demo_mizan.py
"""

import torch
from mizan_fairness.regularizer import MizanRegularizer


def main():
    print("=== Mizan‑Fair Demo ===")
    # Simulate 3 objectives: accuracy, fairness, privacy
    num_objectives = 3
    reg = MizanRegularizer(num_objectives, lambda_balance=0.2, gamma_uniform=0.05)

    # Simulated batch of losses (batch, objectives)
    batch = torch.tensor([
        [0.3, 0.4, 0.2],  # sample 1
        [0.25, 0.35, 0.15],  # sample 2
    ])

    total_loss = reg(batch)
    weights = reg.get_weights()

    print(f"Regularized total loss: {total_loss.item():.4f}")
    print(f"Learned weights distribution: {weights.cpu().numpy()}")
    print("Expected: balanced weights if losses are similar")

    # Try with one objective dominating
    batch2 = torch.tensor([
        [0.7, 0.3, 0.2],  # high loss on accuracy
    ])
    total2 = reg(batch2)
    print(f"\nWhen accuracy loss is high, total loss becomes: {total2.item():.4f}")
    print("Regularizer will push optimizer to improve accuracy relative to others.")


if __name__ == "__main__":
    main()
