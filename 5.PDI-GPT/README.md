# Prophetic Dream Interpreter (PDI-GPT)

System for interpreting and generating dreams based on Islamic dream interpretation traditions.

## Overview

PDI-GPT maps dream symbols to their prophetic meanings and can generate dream narratives that encode desired spiritual outcomes using symbols known to have positive connotations in Islamic tradition.

## Architecture

- **DreamSymbolDictionary**: Maps symbols to prophetic meanings from Ibn Sirin and hadith
- **DreamScriptGenerator**: Generates dream narratives for specific spiritual goals
- **Symbol Database**: Curated collection of dream symbols with hadith references

## Usage

```python
from src.dream_engine import DreamSymbolDictionary, DreamScriptGenerator

sym_dict = DreamSymbolDictionary("data/dream_symbols.json")
result = sym_dict.interpret("I saw water and a key")

gen = DreamScriptGenerator(sym_dict)
dream = gen.generate(goal="guidance", length=3)
```

## Run Demo

```bash
cd 5.PDI-GPT && python demo.py
```

## Files

- `src/dream_engine.py` - Core dream interpretation and generation engine
- `data/dream_symbols.json` - Symbol database with hadith references
- `demo.py` - Interactive demonstration
