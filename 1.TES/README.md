# 1.TES - Theological Embedding Space

## Overview
Theological Embedding Space (TES) is a revolutionary approach to embedding sacred concepts into vector space while preserving ontological hierarchy. Unlike traditional word embeddings that cluster semantically similar terms, TES creates embeddings where distance reflects theological and ontological relationships derived from sacred texts.

## Core Concept
Traditional embeddings: `token → vector` (semantic similarity)  
TES embeddings: `token → ontological vector` (position in hierarchy of being)

Example ontological tiers:
- **Allah**: Vector with infinite magnitude (transcendent)
- **Malaikat** (Angels): Immaterial agency vectors
- **Insan** (Humans): Composite vectors (physical + spiritual + intellect)
- **Haiwan** (Animals): Physical + life force vectors
- **Nabat** (Plants): Life force vectors
- **Jamad** (Stones): Physical matter vectors

## Architecture
```
Input: Sacred text (Quran, Hadith) + Ontological constraints
  ↓
Contrastive Learning with Tier Preservation Loss
  ↓
Output: Embedding space where distance ~ ontological difference
```

## Key Features
- **Ontological Tier Mapping**: Encodes hierarchical relationships from sacred texts
- **Contrastive Loss**: Preserves theological distances during training
- **Sacred Constraint Calibration**: Aligns vectors using hadith-derived relationships
- **Multi-modal Support**: Can embed concepts from multiple sacred traditions

## Usage

### Installation
```bash
pip install divine-ai-suite[tes]
```

### Basic Example
```python
from src.theological_embedding import TheologicalEmbedding, build_tier_mapping

# Build tier mapping from sacred data
tier_map = build_tier_mapping('data/asmaullah.json')

# Create and train embedding model
model = TheologicalEmbedding(tier_map=tier_map, embed_dim=128)
model.train(epochs=100)

# Query embeddings
embedding_allah = model.embed("Allah")
embedding_malaikat = model.embed("Malaikat")
embedding_insan = model.embed("Insan")

# Check ontological distances
dist_allah_malaikat = model.distance(embedding_allah, embedding_malaikat)
dist_malaikat_insan = model.distance(embedding_malaikat, embedding_insan)

print(f"Allah → Malaikat distance: {dist_allah_malaikat}")
print(f"Malaikat → Insan distance: {dist_malaikat_insan}")
# Expected: dist_allah_malaikat > dist_malaikat_insan (hierarchy preserved)
```

### Demo
Run the included demo:
```bash
python demo.py
```

Expected output:
```
✓ TES Training: Loss decreased from 2.341 to 0.127
✓ Ontological tiers formed: Allah(7.82) > Malaikat(6.54) > Insan(5.21) > ...
✓ Similarity to Allah decreases with tier distance
```

## Mathematical Foundation
The TES loss function combines contrastive learning with ontological constraints:

```
L_total = L_contrastive + λ₁·L_tier + λ₂·L_sacred

where:
L_contrastive = -log(exp(sim(pos)/τ) / Σ exp(sim(neg)/τ))
L_tier = Σ |dist(anchor, pos) - expected_tier_distance|²
L_sacred = Σ |embedding(relation) - hadith_derived_value|²
```

## Applications
- **Theologically-consistent text generation**: LLMs fine-tuned with TES never contradict ontological hierarchy
- **Sacred text analysis**: Quantify theological distances between concepts
- **Cross-tradition comparison**: Compare ontological structures across religions
- **AI alignment**: Ensure AI systems reason about non-material realities correctly

## Data Format
Input data should be in JSON format with ontological tier information:
```json
{
  "concepts": [
    {"name": "Allah", "tier": 7, "attributes": ["infinite", "transcendent"]},
    {"name": "Malaikat", "tier": 6, "attributes": ["immaterial", "obedient"]},
    {"name": "Insan", "tier": 5, "attributes": ["physical", "spiritual", "intellect"]}
  ],
  "relations": [
    {"from": "Allah", "to": "Malaikat", "type": "created", "strength": 1.0},
    {"from": "Malaikat", "to": "Insan", "type": "serves", "strength": 0.8}
  ]
}
```

## Citation
If you use TES in your research, please cite:
```
@inproceedings{tes2025,
  title={Theological Embedding Space: Learning Ontology from Sacred Texts},
  author={Atharia AGI Team},
  booktitle={AIES/FAccT/NeurIPS ML for Social Good},
  year={2025}
}
```

## License
MIT License - see main repository LICENSE file.
