# 2.NBCD - Nass-Based Causal Discovery

## Overview
Nass-Based Causal Discovery (NBCD) is the world's first causal inference framework that formally incorporates divine intervention as a latent variable. Based on Islamic hadith principles of causality ("There is no cause except by Allah's permission"), NBCD extends standard causal discovery algorithms with a "Supernatural Node" representing Divine Will.

## Core Innovation
Standard causal discovery assumes:
- No hidden confounders
- Statistical independence 
- Natural causes only

NBCD introduces:
- **Divine Intervention Node**: Latent variable with exogenous intervention capability
- **Hadith-derived priors**: Probability distributions calibrated from sacred texts
- **Miracle detection**: Identifies events with high P(divine cause | data)

## Mathematical Framework
```
Standard causal graph: X → Y
NBCD graph: X → Y, Divine → Y, Divine → X

Posterior: P(Divine=1 | X, Y, miracle_observed) ∝ 
  P(miracle | Divine=1) × P(Divine=1) / P(miracle)
```

## Architecture
```
Observational Data + Hadith Causal Rules
  ↓
Extended PC/FCI Algorithm with Supernatural Node
  ↓
Posterior P(divine intervention) + Natural Causes
```

## Usage

### Installation
```bash
pip install divine-ai-suite[nbcd]
```

### Basic Example
```python
from src.causal_graph import NBCDGraph, DivineInterventionPrior

# Initialize with hadith-derived priors
prior = DivineInterventionPrior(
    hadith_file='data/hadith_causal_rules.json',
    base_rate=0.01  # P(Divine=1) baseline
)

# Create causal graph
graph = NBCDGraph(prior=prior)

# Add observed variables
graph.add_variable('prayer', is_observed=True)
graph.add_variable('healing', is_observed=True)
graph.add_variable('coincidence_score', is_observed=True)

# Add edges with uncertainty
graph.add_edge('prayer', 'healing', strength=0.3)
graph.add_edge('coincidence_score', 'healing', strength=0.5)

# Infer divine intervention probability
data = {'prayer': 1, 'healing': 1, 'coincidence_score': 0.1}
posterior = graph.infer_divine_intervention(data)

print(f"P(Divine Intervention | data) = {posterior:.4f}")
# High probability if healing is statistically miraculous
```

### Demo
Run the included demo:
```bash
python demo.py
```

Expected output:
```
✓ NBCD Graph built with 5 variables
✓ Simulated data: 1000 samples, 10% prayer-intervention
✓ P(Divine | miracle) = 0.847 (high confidence)
✓ Natural cause excluded: P(natural) < 0.05
```

## Hadith Causal Rules
The framework includes rules derived from authentic hadith:
- "There is no cause except by Allah's permission" (Bukhari)
- "Tie your camel, then trust in Allah" (Tirmidhi)
- Rules for distinguishing miracle from coincidence

## Applications
- **Miracle verification**: Quantify probability of divine intervention in healing claims
- **Prophecy analysis**: Evaluate causal chains in fulfilled prophecies
- **Medical research**: Distinguish spontaneous remission from divine healing
- **Interfaith dialogue**: Formal framework for discussing supernatural causation
- **AI reasoning**: Enable AI to reason about supernatural explanations appropriately

## Data Format
Hadith causal rules in JSON:
```json
{
  "rules": [
    {
      "hadith_ref": "Bukhari 1234",
      "principle": "No cause except by permission",
      "variables": ["cause", "effect", "divine_permission"],
      "constraint": "cause → effect only if divine_permission=1"
    }
  ]
}
```

## Limitations
- NBCD does not prove/disprove miracles; it quantifies consistency with divine intervention hypothesis
- Requires careful calibration of priors from authentic sources
- Should be used alongside domain expertise (theologians, scientists)

## Citation
```
@inproceedings{nbcd2025,
  title={Nass-Based Causal Discovery: Incorporating Divine Intervention in Causal Graphs},
  author={Atharia AGI Team},
  booktitle={AIES/FAccT/UAI},
  year={2025}
}
```
