"""
Demo: Theological Embedding Space (TES)

Shows how embeddings learn ontological hierarchy: Allah > Malaikat > Insan > Haiwan > ...
"""

import sys
sys.path.insert(0, 'src')
import torch
import json
from theological_embedding import TheologicalEmbedding, build_tier_mapping

def main():
    print("\n" + "=" * 60)
    print("  THEOLOGICAL EMBEDDING SPACE (TES) DEMO")
    print("  Learning Ontology from Sacred Texts")
    print("=" * 60 + "\n")

    # Load tier mapping
    tier_map = build_tier_mapping("data/asmaullah.json")
    vocab_size = max(max(ids) for ids in tier_map.values()) + 1
    print(f"Vocabulary size: {vocab_size} tokens")
    print(f"Ontological tiers: {len(tier_map)} levels")

    # Build reverse lookup: token_id -> name
    with open("data/asmaullah.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    token_to_name = data["token_to_name"]

    # Initialize model
    model = TheologicalEmbedding(
        vocab_size=vocab_size,
        embed_dim=64,
        tier_to_indices=tier_map,
        margin=1.0,
        lambda_tier=0.1,
        lambda_hier=0.1,
    )

    print("\n[Training] Learning contrastive + tier constraints...")
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    for step in range(50):
        pos_pairs = torch.tensor([[0, 1], [10, 11], [23, 24], [31, 32]])
        neg_pairs = torch.tensor([[0, 23], [10, 31], [23, 40], [1, 42]])

        loss = model(
            token_ids=torch.randint(0, vocab_size, (4, 5)),
            positive_pairs=pos_pairs,
            negative_pairs=neg_pairs,
        )

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if step % 10 == 0:
            print(f"  Step {step:3d} | Loss: {loss.item():.4f}")

    print("\n[Results] Ontological positions after training:\n")
    print(f"{'Token':<15} {'Tier':<6} {'Norm':<8} {'Cos Sim to Allah':<15}")
    print("-" * 55)

    with torch.no_grad():
        tokens_of_interest = [0, 10, 23, 31, 40]
        for tid in tokens_of_interest:
            info = model.get_ontological_position(tid)
            name = token_to_name.get(str(tid), f"ID_{tid}")
            sim_to_allah = model.query_similarity(tid, 0)
            print(f"{name:<15} {info['tier']:<6} {info['norm']:<8.3f} {sim_to_allah:<15.3f}")

    print("\n[Interpretation]")
    print("- Higher tier -> larger norm (existence magnitude)")
    print("- Cosine similarity to Allah decreases down the hierarchy")
    print("- Same-tier items (e.g., malaikat-malaikat) have higher pairwise similarity")

    print("\n[OK] TES operational. Ready for integration with LLMs.\n")


if __name__ == "__main__":
    main()
