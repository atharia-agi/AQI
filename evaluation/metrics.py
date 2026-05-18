"""Evaluation metrics for AQI frameworks."""

import json
from typing import Any


def evaluate_tes(model, tier_map: dict) -> dict[str, float]:
    """Evaluate TES model on ontological consistency metrics."""
    results = {}

    # Tier accuracy: check if higher tier tokens have larger norms
    tier_norms = {}
    with model.no_grad():
        for tier, indices in tier_map.items():
            norms = []
            for idx in indices[:5]:  # Sample first 5
                pos = model.get_ontological_position(idx)
                norms.append(pos["norm"])
            tier_norms[tier] = sum(norms) / len(norms) if norms else 0

    # Check monotonicity (higher tier should have larger norm)
    tiers_sorted = sorted(tier_norms.keys())
    monotonic = all(
        tier_norms[tiers_sorted[i]] <= tier_norms[tiers_sorted[i + 1]]
        for i in range(len(tiers_sorted) - 1)
    )
    results["tier_monotonicity"] = 1.0 if monotonic else 0.0
    results["tier_norms"] = tier_norms

    return results


def evaluate_nbcd(graph, data: list[dict]) -> dict[str, float]:
    """Evaluate NBCD model on causal discovery metrics."""
    results = {}

    # Estimate divine probability
    p_divine = graph.estimate_divine_probability(
        data, intervention_node="salat_prayer",
        target_node="heart_peace", threshold=2.0,
    )
    results["divine_probability"] = p_divine

    # Edge count
    results["n_edges"] = graph.G.number_of_edges()

    return results


def evaluate_dno(dno, logits, labels) -> dict[str, float]:
    """Evaluate DNO model on fairness and accuracy metrics."""
    import torch

    results = {}

    # Get weights
    weights = dno.get_weights()
    results["weights"] = weights

    # Weight entropy (higher = more balanced)
    weight_values = list(weights.values())
    entropy = -sum(w * torch.log(torch.tensor(w + 1e-10)) for w in weight_values)
    results["weight_entropy"] = float(entropy)

    return results


def evaluate_epm(net, observations: dict) -> dict[str, float]:
    """Evaluate EPM model on prediction accuracy."""
    results = {}

    # Posterior probability
    p = net.update_posterior(observations, n_particles=1000)
    results["posterior_probability"] = p
    results["n_signs"] = len(net.nodes)

    return results


def evaluate_pdi_gpt(sym_dict, generator, test_dreams: list[str]) -> dict[str, float]:
    """Evaluate PDI-GPT on symbol matching and narrative quality."""
    results = {}

    total_symbols_found = 0
    for dream in test_dreams:
        interp = sym_dict.interpret(dream)
        total_symbols_found += len(interp.get("interpretations", []))

    results["avg_symbols_per_dream"] = total_symbols_found / len(test_dreams) if test_dreams else 0
    results["n_dreams_tested"] = len(test_dreams)

    return results


def run_full_evaluation(pipeline) -> dict[str, Any]:
    """Run evaluation on the full AQI pipeline."""
    results = {}

    # Test queries
    test_queries = [
        "I dreamt of water and felt peace",
        "How does prayer affect the heart?",
        "What are the signs of the Hour?",
        "I saw a mountain and a bird in my dream",
    ]

    for query in test_queries:
        result = pipeline.process(query)
        results[query] = result

    return results
