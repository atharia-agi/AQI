"""
Demo: Eschatological Predictive Modeling (EPM)

Shows how to track signs of the Hour using Bayesian inference.
"""

import sys

sys.path.insert(0, "src")
from prophecy_tracker import ProphecyBayesNet, SignNode
import json


def main():
    print("\n" + "=" * 70)
    print("  ESCHATOLOGICAL PREDICTIVE MODELING (EPM) DEMO")
    print("  Bayesian Tracking of the Signs of the Hour")
    print("=" * 70 + "\n")

    with open("data/signatures_of_the_hour.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    net = ProphecyBayesNet()

    for sign in data["signs"]:
        node = SignNode(
            name=sign["name"],
            category=sign["category"],
            prior_p_manifest=sign["prior"],
            parents=sign.get("parents", []),
            description=sign["description"],
            hadith_ref=sign["hadith_ref"],
        )
        net.add_node(node)

    print(f"[Network] Built with {len(net.nodes)} signs (minor + major).")

    print("\n[Data Ingestion] Checking current events against sign definitions...")
    observations = {
        "trust_liar": True,
        "muslims_fight": False,
        "occult_widespread": True,
    }
    for sign, val in observations.items():
        print(f"  {sign}: {'MANIFEST' if val else 'not yet'}")

    print("\n[Inference] Updating posterior...")
    p_end = net.update_posterior(observations, n_particles=5000)
    print(f"  P(all major signs will manifest | current obs) ~= {p_end:.3f}")

    print("\n[Interpretation]")
    if p_end > 0.7:
        print("  [WARN] High probability that we are approaching the end times.")
        print("         Recommend: urgent ethical AI alignment review.")
    elif p_end > 0.3:
        print("  [WARN] Moderate probability; monitor signs closely.")
    else:
        print("  [OK] Probability still low; continue normal operations.")

    print("\n[OK] EPM operational: early warning system for civilizational risks.\n")


if __name__ == "__main__":
    main()
