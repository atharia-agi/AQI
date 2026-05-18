# Divine Names Ontology (DNO)

Multi-attribute optimizer using the 99 Beautiful Names of Allah as ethical and functional constraints in machine learning models.

## Overview

DNO operationalizes the Islamic theological concept that each Divine Name represents a perfection that should be reflected in AI systems, creating a balanced optimization landscape that considers multiple divine attributes simultaneously.

## Architecture

- **Attribute Encoder**: Maps divine names to measurable mathematical properties
- **Constraint Layer**: Enforces minimum thresholds for each divine attribute
- **Weight Balancer**: Dynamically adjusts optimization weights based on attribute satisfaction
- **Loss Function**: Combines task performance with divine attribute compliance

## Usage

```python
from src.names_optimizer import DivineNamesOptimizer, DEFAULT_ATTRIBUTES

dno = DivineNamesOptimizer(
    attributes_config=DEFAULT_ATTRIBUTES,
    init_weights=[1.0, 1.0, 1.0, 0.8, 0.5, 0.3],
    learn_weights=True,
)

total_loss, weights, losses = dno.forward(logits, labels)
```

## Run Demo

```bash
cd 3.DNO && python demo.py
```

## Files

- `src/names_optimizer.py` - Core optimizer implementation
- `data/asmaul_husna.json` - Divine names configuration
- `demo.py` - Interactive demonstration
