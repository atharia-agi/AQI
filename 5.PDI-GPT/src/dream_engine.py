"""
Prophetic Dream Interpreter (PDI‑GPT)

Uses a knowledge base of dream symbols from Hadith (Ibn Sirin etc.) to:
- Interpret user‑described dreams
- Generate “prescribed” dream scripts to achieve desired outcomes

Based on the hadith: “Dreams are of three types: glad tidings from Allah, what
the self contemplates, and what the devil suggests.” (Sahih Bukhari)

We distinguish between:
- Symbol → meaning (interpretation)
- Goal → symbolic sequence (generation)
"""

import json
import random
from typing import List, Dict, Tuple
import numpy as np

class DreamSymbolDictionary:
    """
    Maps symbols (objects, actions, colors, emotions) to their prophetic meanings.
    Source: Ibn Sirin’s methodology, validated by hadith.
    """

    def __init__(self, data_path: str):
        with open(data_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.symbols = {s['symbol']: s for s in self.data['symbols']}
        self.colors = {c['color']: c for c in self.data.get('colors', [])}
        self.actions = {a['action']: a for a in self.data.get('actions', [])}

    def interpret(self, dream_desc: str) -> Dict:
        """
        Very simple keyword matching for demo.
        Returns a list of interpretations with hadith references.
        """
        tokens = dream_desc.lower().split()
        interpretations = []

        for token in tokens:
            if token in self.symbols:
                interpretations.append({
                    "symbol": token,
                    "meaning": self.symbols[token]["meaning"],
                    "strength": self.symbols[token].get("strength", "medium"),
                    "hadith_ref": self.symbols[token].get("hadith_ref", "")
                })
            if token in self.actions:
                interpretations.append({
                    "action": token,
                    "meaning": self.actions[token]["meaning"],
                    "hadith_ref": self.actions[token].get("hadith_ref", "")
                })

        return {
            "raw_input": dream_desc,
            "interpretations": interpretations,
            "verdict": self.summarize(interpretations)
        }

    def summarize(self, interpretations: List[Dict]) -> str:
        if not interpretations:
            return "No clear symbolic meaning found in the hadith corpus."
        # Take the most significant (first or highest strength)
        top = interpretations[0]
        return f"{top['symbol'] if 'symbol' in top else top['action']} indicates {top['meaning']}."

class DreamScriptGenerator:
    """
    Generates a dream narrative that encodes a desired outcome (e.g., guidance,
    healing, solution to problem) using symbols known to have positive meanings.
    """

    def __init__(self, symbol_dict: DreamSymbolDictionary):
        self.symbol_dict = symbol_dict

        # Positive symbols for various goals
        self.goal_symbols = {
            "guidance": ["light", "path", "water", "mountain", "prophet", "prayer"],
            "healing": ["water", "medicine", "green", "tree", "bird"],
            "solution": ["key", "door", "sunrise", "book"],
            "peace": ["white", "bird", "moon", "calm sea", "smile"],
            "wealth": ["gold", "fruit", "rain", "camel"],
        }

        # Narrative templates
        self.templates = [
            "You see {A} and then {B} appears, guiding you toward {C}.",
            "In a field of {A}, you find {B} and feel {C}.",
            "A {A} calls you to {B}, and you understand {C}.",
        ]

    def generate(self, goal: str, length: int = 3) -> Dict:
        """
        Generate a dream script of given length (number of symbolic elements).
        Returns dict with scene sequence and interpretation.
        """
        if goal not in self.goal_symbols:
            goal = "guidance"

        symbols = self.goal_symbols[goal]
        # Randomly sample without replacement
        chosen = random.sample(symbols, min(len(symbols), length))

        # Build narrative
        scene = []
        for i, sym in enumerate(chosen):
            # Choose template based on position
            t = random.choice(self.templates)
            # Fill slots
            if i == 0:
                fragment = t.format(A=sym, B=random.choice(self.goal_symbols[goal]), C="the truth")
            elif i < length-1:
                fragment = t.format(A=chosen[i-1], B=sym, C="your success")
            else:
                fragment = t.format(A=chosen[i-1], B=sym, C="complete understanding")
            scene.append(fragment)

        narrative = " ".join(scene)

        return {
            "goal": goal,
            "symbols_used": chosen,
            "narrative": narrative,
            "interpretation": f"This dream encodes the desired {goal} through prophetic symbols."
        }

def main():
    print("\n" + "="*70)
    print("  PROPHETIC DREAM INTERPRETER (PDI‑GPT) DEMO")
    print("  Interpreting & Generating Dreams via Hadith Symbolism")
    print("="*70 + "\n")

    # Initialize dictionary
    sym_dict = DreamSymbolDictionary("data/dream_symbols.json")
    print(f"[Symbols loaded] {len(sym_dict.symbols)} items, {len(sym_dict.actions)} actions")

    # Interpretation demo
    print("\n[Interpretation Mode]")
    test_dream = "I saw water and a key and felt peace"
    result = sym_dict.interpret(test_dream)
    print(f"  Dream: \"{test_dream}\"")
    print(f"  Symbols found: {[i['symbol'] for i in result['interpretations']]}")
    print(f"  Verdict: {result['verdict']}")

    # Generation demo
    print("\n[Generation Mode]")
    gen = DreamScriptGenerator(sym_dict)
    generated = gen.generate(goal="guidance", length=3)
    print(f"  Desired outcome: {generated['goal']}")
    print(f"  Symbols used: {generated['symbols_used']}")
    print(f"  Dream script: \"{generated['narrative']}\"")
    print(f"  Interpretation: {generated['interpretation']}")

    print("\n✅ PDI‑GPT running: merge prophetic symbolism with AI generation.\n")

if __name__ == "__main__":
    main()

