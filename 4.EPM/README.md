# Eschatological Predictive Modeling (EPM)

Bayesian tracking system that monitors contemporary events against Islamic eschatological signs.

## Overview

EPM provides an early warning system for civilizational risks by updating probabilities of eschatological events based on real-world observations.

## Architecture

- **Sign Ontology**: Hierarchical representation of minor and major signs
- **Evidence Collector**: Gathers and preprocesses data from various sources
- **Bayesian Updater**: Core algorithm that updates sign probabilities using Bayes theorem
- **Alert System**: Triggers notifications when probabilities cross defined thresholds

## Usage

```python
from src.prophecy_tracker import ProphecyBayesNet, SignNode

net = ProphecyBayesNet()
node = SignNode(name="sign_name", category="minor", prior_p_manifest=0.01)
net.add_node(node)
p_end = net.update_posterior(observations, n_particles=5000)
```

## Run Demo

```bash
cd 4.EPM && python demo.py
```

## Files

- `src/prophecy_tracker.py` - Core Bayesian network implementation
- `data/signatures_of_the_hour.json` - Signs database
- `demo.py` - Interactive demonstration
