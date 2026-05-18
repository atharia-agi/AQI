"""
Demo: Divine Names Ontology (DNO)

Shows how training with divine attribute objectives shapes model behavior.
We simulate a simple classification task where we care about accuracy (wisdom),
fairness (justice), and compassion (mercy).
"""

import sys
sys.path.insert(0, 'src')
import torch
import torch.nn as nn
import json
from names_optimizer import DivineNamesOptimizer, DEFAULT_ATTRIBUTES

def synthetic_data(n=1000):
    """Create binary classification with sensitive attribute."""
    X = torch.randn(n, 10)
    logits = X @ torch.randn(10, 2)
    y = torch.argmax(logits, dim=1)
    sensitive = (X[:, 0] > 0).long()
    return X, y, sensitive

class SimpleClassifier(nn.Module):
    def __init__(self, input_dim=10, num_classes=2):
        super().__init__()
        self.fc = nn.Linear(input_dim, num_classes)
    def forward(self, x):
        return self.fc(x)

def fairness_loss(logits, sensitive, y):
    """
    Compute demographic parity difference as fairness metric.
    We want P(y_hat=1 | group=0) ~ P(y_hat=1 | group=1)
    """
    preds = torch.argmax(logits, dim=1)
    prob_0 = (preds[sensitive == 0] == 1).float().mean()
    prob_1 = (preds[sensitive == 1] == 1).float().mean()
    dp_diff = torch.abs(prob_0 - prob_1)
    return dp_diff

def main():
    print("\n" + "=" * 70)
    print("  DIVINE NAMES ONTOLOGY (DNO) DEMO")
    print("  Optimizing with Multiple Divine Attributes")
    print("=" * 70 + "\n")

    X, y, sensitive = synthetic_data(500)
    dataset = torch.utils.data.TensorDataset(X, y, sensitive)
    loader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True)

    model = SimpleClassifier()
    dno = DivineNamesOptimizer(
        attributes_config=DEFAULT_ATTRIBUTES,
        init_weights=[1.0, 1.0, 1.0, 0.8, 0.5, 0.3],
        learn_weights=True,
    )
    params = list(model.parameters())
    if dno.learn_weights and dno.raw_weights is not None:
        params.append(dno.raw_weights)
    optimizer = torch.optim.Adam(params, lr=1e-2)

    print("[Attributes]")
    for i, name in enumerate(dno.attr_names):
        print(f"  {i + 1}. {name} (type: {DEFAULT_ATTRIBUTES[i]['attribute_type']})")

    print("\n[Training] 50 epochs with divine attribute balancing...")
    for epoch in range(50):
        epoch_loss = 0.0
        for batch_X, batch_y, batch_s in loader:
            optimizer.zero_grad()
            logits = model(batch_X)
            total_loss, weights, losses = dno.forward(logits, batch_y)
            fair_loss = fairness_loss(logits, batch_s, batch_y)
            total_loss = total_loss + 0.5 * fair_loss

            total_loss.backward()
            optimizer.step()
            epoch_loss += total_loss.item()

        if epoch % 10 == 0:
            with torch.no_grad():
                current_weights = dno.get_weights()
                print(
                    f"  Epoch {epoch:3d} | Loss: {epoch_loss:.4f} | Weights: "
                    + ", ".join(f"{name[:3]}={w:.2f}" for name, w in current_weights.items())
                )

    print("\n[Evaluation]")
    model.eval()
    with torch.no_grad():
        logits_all = model(X)
        preds = torch.argmax(logits_all, dim=1)
        acc = (preds == y).float().mean()
        fair = fairness_loss(logits_all, sensitive, y)
        print(f"  Accuracy: {acc.item():.3f}")
        print(f"  Fairness (DP diff): {fair.item():.3f} (lower is better)")

    print("\n[Divine Weight Distribution]")
    final_weights = dno.get_weights()
    for name, w in final_weights.items():
        print(f"  {name}: {w:.3f}")

    print("\n[OK] DNO complete: model trained under multi-divine-attribute constraints.")
    print("   Compare weights with expected priorities (Ar-Rahman, Al-Adl highest).\n")


if __name__ == "__main__":
    main()
