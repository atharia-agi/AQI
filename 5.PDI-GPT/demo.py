"""
Demo: Prophetic Dream Interpreter (PDIâ€‘GPT)

Uses a knowledge base of dream symbols from Hadith (Ibn Sirin etc.) to:
- Interpret userâ€‘described dreams
- Generate "prescribed" dream scripts to achieve desired outcomes
"""

import sys
sys.path.insert(0, 'src')
from dream_engine import DreamSymbolDictionary, DreamScriptGenerator

def main():
    print("\n" + "="*70)
    print("  PROPHETIC DREAM INTERPRETER (PDIâ€‘GPT) DEMO")
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

    print("\nâœ… PDIâ€‘GPT running: merge prophetic symbolism with AI generation.\n")

if __name__ == "__main__":
    main()



