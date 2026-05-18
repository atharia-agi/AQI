"""
Eschatological Predictive Modeling (EPM)

Tracks signs of the Hour (أشراط الساعة) using Bayesian inference.
We maintain a probability distribution over “remaining time” given observed
events that match prophetic descriptions.

Key references:
- Hadith on “ten signs of the Hour” (Sahih Bukhari, Muslim)
- Minor signs (over 100) from various collections
- Major signs (al‑malhamah, Dajjal, descent of Isa, etc.)

We treat each sign as a binary variable that may be “manifest” or not.
Conditional probabilities encode which signs are expected to precede others.
Given observations (e.g., “people trust the liar”), we update posterior P(T < t).
"""

import numpy as np
from typing import Dict, List, Set, Tuple
import json
import datetime

class SignNode:
    """Represents a single eschatological sign."""

    def __init__(
        self,
        name: str,
        category: str,
        prior_p_manifest: float,
        parents: List[str] = None,
        description: str = "",
        hadith_ref: str = ""
    ):
        self.name = name
        self.category = category  # 'minor' or 'major'
        self.prior = prior_p_manifest  # prior probability it will manifest before Judgment
        self.parents = parents or []  # signs that must occur before this one
        self.description = description
        self.hadith_ref = hadith_ref
        self.observed = False

    def __repr__(self):
        return f"<Sign {self.name} (parents={self.parents})>"

class ProphecyBayesNet:
    """
    Bayesian network over signs. Structure: parents → child.
    Parameters:
      - P(sign=True | parents) computed via noisy‑OR or logistic.
      - Prior P(remaining time) uniform over some large horizon.
    """

    def __init__(self):
        self.nodes: Dict[str, SignNode] = {}
        self.adjacency: Dict[str, List[str]] = {}
        self.reverse_adj: Dict[str, List[str]] = {}

    def add_node(self, node: SignNode):
        self.nodes[node.name] = node
        self.adjacency[node.name] = []
        self.reverse_adj.setdefault(node.name, [])
        for p in node.parents:
            self.adjacency[p].append(node.name)
            self.reverse_adj[node.name].append(p)

    def topological_order(self) -> List[str]:
        return list(self.nodes.keys())  # simplified; should do proper toposort

    def sample_topology(self) -> Dict[str, bool]:
        """
        Sample a full assignment of signs given the graph and priors.
        Uses topological ordering, sampling each node conditional on parents.
        """
        order = self.topological_order()
        assignment = {}
        for name in order:
            node = self.nodes[name]
            if not node.parents:
                p_true = node.prior
            else:
                # Noisy‑OR: if any parent is true, increase chance
                parent_vals = [assignment[p] for p in node.parents]
                p_base = node.prior
                # Simple: if any parent true, boost = 0.3
                if any(parent_vals):
                    p_true = min(1.0, p_base + 0.3)
                else:
                    p_true = p_base
            assignment[name] = np.random.random() < p_true
        return assignment

    def update_posterior(
        self,
        observations: Dict[str, bool],
        n_particles: int = 10000
    ) -> float:
        """
        Given observed signs (some True, some False), estimate the posterior
        probability that we are within the “last X years”. For demo, we compute
        the fraction of particles where all major signs manifest.
        """
        # Count how many samples match observations AND have all major signs True
        matches = 0
        total = 0

        major_signs = [n for n, node in self.nodes.items() if node.category == 'major']

        for _ in range(n_particles):
            sample = self.sample_topology()
            # Check if sample matches observations
            ok = True
            for sign, val in observations.items():
                if sign not in sample:
                    continue
                if sample[sign] != val:
                    ok = False
                    break
            if not ok:
                continue
            total += 1
            # If all major signs are True in sample, count as “end is near”
            if all(sample.get(s, False) for s in major_signs):
                matches += 1

        if total == 0:
            return 0.0
        return matches / total

def build_current_events_mapper() -> Dict[str, callable]:
    """
    Returns a dict of sign → boolean function that checks current data.
    In a real implementation, these would query news APIs, social media stats, etc.
    For demo, we simulate deterministic functions or random.
    """
    def fake_check_trust_liars():
        # Simulate: “people will trust the liar” — just random for demo
        return np.random.random() < 0.3

    def fake_check_muslims_fight():
        return np.random.random() < 0.2

    def fake_check_occult():
        return np.random.random() < 0.1

    return {
        "trust_liar": fake_check_trust_liars,
        "muslims_fight": fake_check_muslims_fight,
        "occult_widespread": fake_check_occult,
    }

def main():
    print("\n" + "="*70)
    print("  ESCHATOLOGICAL PREDICTIVE MODELING (EPM) DEMO")
    print("  Bayesian Tracking of the Signs of the Hour")
    print("="*70 + "\n")

    # Build network from data file
    with open("data/signatures_of_the_hour.json", 'r', encoding='utf-8') as f:
        data = json.load(f)

    net = ProphecyBayesNet()

    # Add nodes
    for sign in data["signs"]:
        node = SignNode(
            name=sign["name"],
            category=sign["category"],
            prior_p_manifest=sign["prior"],
            parents=sign.get("parents", []),
            description=sign["description"],
            hadith_ref=sign["hadith_ref"]
        )
        net.add_node(node)

    print(f"[Network] Built with {len(net.nodes)} signs (minor + major).")

    # Simulate current observations from real‑world data proxies
    print("\n[Data Ingestion] Checking current events against sign definitions...")
    mappers = build_current_events_mapper()
    observations = {}
    for sign_name in ["trust_liar", "muslims_fight", "occult_widespread"]:
        if sign_name in mappers:
            val = mappers[sign_name]()
            observations[sign_name] = val
            print(f"  {sign_name}: {'MANIFEST' if val else 'not yet'}")

    # Compute posterior probability that we are “in the last hour”
    print("\n[Inference] Updating posterior...")
    p_end = net.update_posterior(observations, n_particles=5000)
    print(f"  P(all major signs will manifest | current obs) ≈ {p_end:.3f}")

    print("\n[Interpretation]")
    if p_end > 0.7:
        print("  ⚠️  High probability that we are approaching the end times.")
        print("      Recommend: urgent ethical AI alignment review.")
    elif p_end > 0.3:
        print("  ⚠️  Moderate probability; monitor signs closely.")
    else:
        print("  ✅ Probability still low; continue normal operations.")

    print("\n✅ EPM operational: early warning system for civilizational risks.\n")

if __name__ == "__main__":
    main()
