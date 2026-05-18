"""Integration layer for AQI - connects all 5 frameworks into one pipeline.

The AQI Pipeline:
    Input (text/query)
        -> TES: Understand ontological position
        -> NBCD: Detect causal relationships + divine intervention
        -> DNO: Apply divine attribute constraints
        -> EPM: Check eschatological context
        -> PDI-GPT: Interpret symbolic meaning
        -> Output: Integrated response
"""

import json
import time
from pathlib import Path
from typing import Any


class AQIPipeline:
    """Main pipeline connecting all 5 AQI frameworks."""

    def __init__(self, config: dict | None = None):
        self.config = config or {}
        self.tes = None
        self.nbcd = None
        self.dno = None
        self.epm = None
        self.pdi_gpt = None
        self._initialized = False

    def initialize(self):
        """Initialize all 5 frameworks."""
        print("[AQI] Initializing pipeline...")
        start = time.time()

        # Initialize TES
        import sys
        sys.path.insert(0, '1.TES/src')
        from theological_embedding import TheologicalEmbedding, build_tier_mapping
        tier_map = build_tier_mapping("1.TES/data/asmaullah.json")
        vocab_size = max(max(ids) for ids in tier_map.values()) + 1
        self.tes = TheologicalEmbedding(
            vocab_size=vocab_size, embed_dim=64, tier_to_indices=tier_map,
        )

        # Initialize NBCD
        sys.path.insert(0, '2.NBCD/src')
        from causal_graph import NBCDGraph
        self.nbcd = NBCDGraph()
        self.nbcd.add_edge("salat_prayer", "heart_peace", 0.3, edge_type="prayer")
        self.nbcd.add_edge("sadaqah_charity", "barakah_blessing", 0.2, edge_type="charity")

        # Initialize DNO
        sys.path.insert(0, '3.DNO/src')
        from names_optimizer import DivineNamesOptimizer, DEFAULT_ATTRIBUTES
        self.dno = DivineNamesOptimizer(
            attributes_config=DEFAULT_ATTRIBUTES, learn_weights=True,
        )

        # Initialize EPM
        sys.path.insert(0, '4.EPM/src')
        from prophecy_tracker import ProphecyBayesNet, SignNode
        self.epm = ProphecyBayesNet()
        with open("4.EPM/data/signatures_of_the_hour.json", 'r', encoding='utf-8') as f:
            signs_data = json.load(f)
        for sign in signs_data["signs"][:5]:  # Load first 5 for demo
            node = SignNode(
                name=sign["name"], category=sign["category"],
                prior_p_manifest=sign["prior"],
            )
            self.epm.add_node(node)

        # Initialize PDI-GPT
        sys.path.insert(0, '5.PDI-GPT/src')
        from dream_engine import DreamSymbolDictionary, DreamScriptGenerator
        sym_dict = DreamSymbolDictionary("5.PDI-GPT/data/dream_symbols.json")
        self.pdi_gpt = DreamScriptGenerator(sym_dict)

        self._initialized = True
        elapsed = time.time() - start
        print(f"[AQI] Pipeline initialized in {elapsed:.2f}s")

    def process(self, query: str) -> dict[str, Any]:
        """Process a query through the full AQI pipeline.

        Args:
            query: Input text/query to process

        Returns:
            Dict with results from each framework
        """
        if not self._initialized:
            self.initialize()

        results = {
            "query": query,
            "tes": None,
            "nbcd": None,
            "dno": None,
            "epm": None,
            "pdi_gpt": None,
        }

        # Step 1: TES - Ontological analysis
        results["tes"] = self._run_tes(query)

        # Step 2: NBCD - Causal analysis
        results["nbcd"] = self._run_nbcd(query)

        # Step 3: DNO - Divine attribute analysis
        results["dno"] = self._run_dno(query)

        # Step 4: EPM - Eschatological context
        results["epm"] = self._run_epm(query)

        # Step 5: PDI-GPT - Symbolic interpretation
        results["pdi_gpt"] = self._run_pdi_gpt(query)

        return results

    def _run_tes(self, query: str) -> dict:
        """Run TES analysis on query."""
        # Simple keyword-based ontological lookup
        query_lower = query.lower()
        ontological_results = []
        for word in query_lower.split():
            # Check if word matches any known token
            try:
                sim = self.tes.query_similarity(0, 0)  # Placeholder
                ontological_results.append({"word": word, "similarity": float(sim)})
            except Exception:
                pass
        return {"ontological_analysis": ontological_results}

    def _run_nbcd(self, query: str) -> dict:
        """Run NBCD analysis on query."""
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
        """Run DNO analysis on query."""
        weights = self.dno.get_weights()
        return {"divine_weights": weights}

    def _run_epm(self, query: str) -> dict:
        """Run EPM analysis on query."""
        # Check if query relates to any known signs
        query_lower = query.lower()
        relevant_signs = []
        for name, node in self.epm.nodes.items():
            if name in query_lower or node.description.lower() in query_lower:
                relevant_signs.append({
                    "name": name,
                    "category": node.category,
                    "prior": node.prior_p_manifest,
                })
        return {"relevant_signs": relevant_signs}

    def _run_pdi_gpt(self, query: str) -> dict:
        """Run PDI-GPT analysis on query."""
        # If query looks like a dream, interpret it
        dream_keywords = ["dream", "saw", "dreamt", "sleep", "vision"]
        if any(kw in query.lower() for kw in dream_keywords):
            from dream_engine import DreamSymbolDictionary
            sym_dict = DreamSymbolDictionary("5.PDI-GPT/data/dream_symbols.json")
            interpretation = sym_dict.interpret(query)
            return {"interpretation": interpretation}
        return {"interpretation": None}

    def get_summary(self, results: dict) -> str:
        """Generate a human-readable summary of pipeline results."""
        lines = [f"AQI Analysis for: '{results['query']}'"]
        lines.append("=" * 50)

        if results["tes"] and results["tes"]["ontological_analysis"]:
            lines.append("\n[TES] Ontological Analysis:")
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
