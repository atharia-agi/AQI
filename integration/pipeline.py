"""AQI Integration Layer - connects all frameworks with Quranic Principles as foundation.

The AQI Pipeline:
    Quranic Principles (Foundation)
        -> TES: Understand ontological position
        -> NBCD: Detect causal relationships + divine intervention
        -> DNO: Apply divine attribute constraints
        -> EPM: Check eschatological context
        -> PDI-GPT: Interpret symbolic meaning
        -> Output: Integrated response guided by Quranic principles
"""

import json
import time
from pathlib import Path
from typing import Any


class AQIPipeline:
    """Main pipeline connecting Quranic Principles + all 5 frameworks."""

    def __init__(self, config: dict | None = None):
        self.config = config or {}
        self.quranic_principles = None
        self.tes = None
        self.nbcd = None
        self.dno = None
        self.epm = None
        self.pdi_gpt = None
        self._initialized = False

    def initialize(self):
        """Initialize Quranic Principles + all 5 frameworks."""
        print("[AQI] Initializing pipeline...")
        start = time.time()

        # Initialize Quranic Principles (FOUNDATION)
        from quranic_principles.mathematical_codes import QuranicMathematicalCodes
        from quranic_principles.scientific_references import QuranicScientificReferences
        from quranic_principles.hidden_patterns import QuranicHiddenPatterns
        from quranic_principles.literary_devices import QuranicLiteraryDevices
        from quranic_principles.ontological_hierarchy import QuranicOntologicalHierarchy

        self.quranic_principles = {
            "mathematical_codes": QuranicMathematicalCodes(),
            "scientific_references": QuranicScientificReferences(),
            "hidden_patterns": QuranicHiddenPatterns(),
            "literary_devices": QuranicLiteraryDevices(),
            "ontological_hierarchy": QuranicOntologicalHierarchy(),
        }
        print("  [OK] Quranic Principles initialized (5 modules)")

        # Initialize TES
        import sys
        sys.path.insert(0, '1.TES/src')
        from theological_embedding import TheologicalEmbedding, build_tier_mapping
        tier_map = build_tier_mapping("1.TES/data/asmaullah.json")
        vocab_size = max(max(ids) for ids in tier_map.values()) + 1
        self.tes = TheologicalEmbedding(
            vocab_size=vocab_size, embed_dim=64, tier_to_indices=tier_map,
        )
        print("  [OK] TES initialized")

        # Initialize NBCD
        sys.path.insert(0, '2.NBCD/src')
        from causal_graph import NBCDGraph
        self.nbcd = NBCDGraph()
        self.nbcd.add_edge("salat_prayer", "heart_peace", 0.3, edge_type="prayer")
        self.nbcd.add_edge("sadaqah_charity", "barakah_blessing", 0.2, edge_type="charity")
        print("  [OK] NBCD initialized")

        # Initialize DNO
        sys.path.insert(0, '3.DNO/src')
        from names_optimizer import DivineNamesOptimizer, DEFAULT_ATTRIBUTES
        self.dno = DivineNamesOptimizer(
            attributes_config=DEFAULT_ATTRIBUTES, learn_weights=True,
        )
        print("  [OK] DNO initialized")

        # Initialize EPM
        sys.path.insert(0, '4.EPM/src')
        from prophecy_tracker import ProphecyBayesNet, SignNode
        self.epm = ProphecyBayesNet()
        with open("4.EPM/data/signatures_of_the_hour.json", 'r', encoding='utf-8') as f:
            signs_data = json.load(f)
        for sign in signs_data["signs"][:5]:
            node = SignNode(
                name=sign["name"], category=sign["category"],
                prior_p_manifest=sign["prior"],
            )
            self.epm.add_node(node)
        print("  [OK] EPM initialized")

        # Initialize PDI-GPT
        sys.path.insert(0, '5.PDI-GPT/src')
        from dream_engine import DreamSymbolDictionary, DreamScriptGenerator
        sym_dict = DreamSymbolDictionary("5.PDI-GPT/data/dream_symbols.json")
        self.pdi_gpt = DreamScriptGenerator(sym_dict)
        print("  [OK] PDI-GPT initialized")

        self._initialized = True
        elapsed = time.time() - start
        print(f"[AQI] Pipeline initialized in {elapsed:.2f}s")

    def process(self, query: str) -> dict[str, Any]:
        """Process a query through the full AQI pipeline.

        Step 0: Quranic Principles analysis (foundation)
        Step 1: TES - Ontological analysis
        Step 2: NBCD - Causal analysis
        Step 3: DNO - Divine attribute analysis
        Step 4: EPM - Eschatological context
        Step 5: PDI-GPT - Symbolic interpretation
        """
        if not self._initialized:
            self.initialize()

        results = {
            "query": query,
            "quranic_principles": None,
            "tes": None,
            "nbcd": None,
            "dno": None,
            "epm": None,
            "pdi_gpt": None,
        }

        # Step 0: Quranic Principles (FOUNDATION)
        results["quranic_principles"] = self._run_quranic_principles(query)

        # Steps 1-5: Framework analysis
        results["tes"] = self._run_tes(query)
        results["nbcd"] = self._run_nbcd(query)
        results["dno"] = self._run_dno(query)
        results["epm"] = self._run_epm(query)
        results["pdi_gpt"] = self._run_pdi_gpt(query)

        return results

    def _run_quranic_principles(self, query: str) -> dict[str, Any]:
        """Run Quranic Principles analysis on query."""
        results = {}

        # Check for mathematical patterns
        mc = self.quranic_principles["mathematical_codes"]
        results["sea_land_ratio"] = mc.get_sea_land_ratio()
        results["word_symmetries"] = mc.get_all_symmetries()[:3]  # Top 3

        # Check for scientific references
        sr = self.quranic_principles["scientific_references"]
        results["total_scientific_refs"] = sr.count_total_references()

        # Check ontological hierarchy
        oh = self.quranic_principles["ontological_hierarchy"]
        results["ontological_levels"] = len(oh.get_all_levels())

        return results

    def _run_tes(self, query: str) -> dict:
        query_lower = query.lower()
        ontological_results = []
        for word in query_lower.split():
            try:
                sim = self.tes.query_similarity(0, 0)
                ontological_results.append({"word": word, "similarity": float(sim)})
            except Exception:
                pass
        return {"ontological_analysis": ontological_results}

    def _run_nbcd(self, query: str) -> dict:
        query_lower = query.lower()
        causal_links = []
        for u, v, data in self.nbcd.G.edges(data=True):
            if u in query_lower or v in query_lower:
                causal_links.append({
                    "source": u, "target": v,
                    "strength": data["strength"],
                    "type": data.get("type", "natural"),
                })
        return {"causal_links": causal_links}

    def _run_dno(self, query: str) -> dict:
        weights = self.dno.get_weights()
        return {"divine_weights": weights}

    def _run_epm(self, query: str) -> dict:
        query_lower = query.lower()
        relevant_signs = []
        for name, node in self.epm.nodes.items():
            if name in query_lower or node.description.lower() in query_lower:
                relevant_signs.append({
                    "name": name, "category": node.category,
                    "prior": node.prior_p_manifest,
                })
        return {"relevant_signs": relevant_signs}

    def _run_pdi_gpt(self, query: str) -> dict:
        dream_keywords = ["dream", "saw", "dreamt", "sleep", "vision"]
        if any(kw in query.lower() for kw in dream_keywords):
            from dream_engine import DreamSymbolDictionary
            sym_dict = DreamSymbolDictionary("5.PDI-GPT/data/dream_symbols.json")
            interpretation = sym_dict.interpret(query)
            return {"interpretation": interpretation}
        return {"interpretation": None}

    def get_summary(self, results: dict) -> str:
        """Generate a human-readable summary."""
        lines = [
            "AQI Analysis",
            "=" * 50,
            f"Query: '{results['query']}'",
            "",
        ]

        if results["quranic_principles"]:
            qp = results["quranic_principles"]
            lines.append("[QURANIC PRINCIPLES]")
            lines.append(f"  Scientific references: {qp['total_scientific_refs']}")
            lines.append(f"  Ontological levels: {qp['ontological_levels']}")
            slr = qp["sea_land_ratio"]
            lines.append(f"  Sea/Land ratio: {slr['sea_percentage']}% / {slr['land_percentage']}%")
            lines.append("")

        if results["tes"] and results["tes"]["ontological_analysis"]:
            lines.append("[TES] Ontological Analysis:")
            for item in results["tes"]["ontological_analysis"]:
                lines.append(f"  - {item['word']}: similarity={item['similarity']:.3f}")

        if results["nbcd"] and results["nbcd"]["causal_links"]:
            lines.append("\n[NBCD] Causal Links Found:")
            for link in results["nbcd"]["causal_links"]:
                lines.append(f"  - {link['source']} -> {link['target']} ({link['strength']:.2f})")

        if results["dno"] and results["dno"]["divine_weights"]:
            lines.append("\n[DNO] Divine Attribute Weights:")
            for name, w in results["dno"]["divine_weights"].items():
                lines.append(f"  - {name}: {w:.3f}")

        if results["epm"] and results["epm"]["relevant_signs"]:
            lines.append("\n[EPM] Relevant Eschatological Signs:")
            for sign in results["epm"]["relevant_signs"]:
                lines.append(f"  - {sign['name']} ({sign['category']})")

        if results["pdi_gpt"] and results["pdi_gpt"]["interpretation"]:
            interp = results["pdi_gpt"]["interpretation"]
            lines.append(f"\n[PDI-GPT] Dream Interpretation:")
            lines.append(f"  Verdict: {interp.get('verdict', 'N/A')}")

        return "\n".join(lines)


def main():
    """Demo the AQI pipeline."""
    pipeline = AQIPipeline()
    pipeline.initialize()

    queries = [
        "I dreamt of water and felt peace",
        "How does prayer affect the heart?",
        "What are the signs of the Hour?",
    ]

    for query in queries:
        print()
        results = pipeline.process(query)
        print(pipeline.get_summary(results))
        print()


if __name__ == "__main__":
    main()
