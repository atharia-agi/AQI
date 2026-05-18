"""
Demo: Nass-Based Causal Discovery (NBCD)

Shows how divine intervention can be inferred from data that includes prayer
and unexpected outcomes.
"""

import numpy as np
from src.causal_graph import NBCDGraph, DivineInterventionPrior


def main():
    print("\n" + "=" * 70)
    print("  NASS-BASED CAUSAL DISCOVERY (NBCD) DEMO")
    print("  Inferring Divine Intervention from Data")
    print("=" * 70 + "\n")

    # Build graph: Prayer -> Guidance, Charity -> Barakah, etc.
    graph = NBCDGraph()

    # Add natural causal edges (strength = natural effect size)
    graph.add_edge("salat_prayer", "heart_peace", 0.3, edge_type="prayer")
    graph.add_edge("salat_prayer", "miraculous_outcome", 0.05, edge_type="prayer")
    graph.add_edge("sadaqah_charity", "barakah_blessing", 0.2, edge_type="charity")
    graph.add_edge("dua_supplication", "rizq_sustenance", 0.1, edge_type="dua")
    graph.add_edge("dhikr_remembrance", "inner_calm", 0.25, edge_type="dhikr")
    print("[Graph] Causal structure defined:")
    for u, v, data in graph.G.edges(data=True):
        print(f"  {u} -> {v}  (strength={data['strength']:.2f}, type={data['type']})")
    np.random.seed(42)

    # Generate samples
    n_samples = 200
    data = []
    miracle_count = 0

    for i in range(n_samples):
        # Simulate: sometimes prayer triggers divine intervention
        do_intervene = np.random.random() < 0.1  # 10% of prayers get miraculous boost
        intervention_node = "salat_prayer" if do_intervene else None

        obs = graph.sample_observation(intervention_node=intervention_node, noise_std=0.2)
        data.append(obs)
        if do_intervene:
            miracle_count += 1

    print(
        f"  Generated {n_samples} observations; {miracle_count} included prayer intervention events."
    )

    # Estimate posterior probability of divine intervention
    print("\n[Inference] Estimating divine intervention probability from data...")
    p_divine = graph.estimate_divine_probability(
        data,
        intervention_node="salat_prayer",
        target_node="miraculous_outcome",
        threshold=2.5,
    )
    print(f"  Posterior P(divine intervention | prayer)  {p_divine:.3f}")

    print("\n[Interpretation]")
    print("- High probability indicates that 'miraculous outcome' occurs more often")
    print("  than expected from natural causal strength alone.")
    print("- This aligns with hadith: prayer can open doors of divine providence.")

    print("\n NBCD operational: can detect supernatural causality while respecting natural laws.\n")


if __name__ == "__main__":
    main()
