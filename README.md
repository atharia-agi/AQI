# Divine AI Suite

> Five revolutionary AI frameworks that translate sacred ontological, causal, and eschatological knowledge into computational primitives.

[![CI](https://github.com/atharia-agi/tawhid-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/atharia-agi/tawhid-engine/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

---

## What Is This?

The **Divine AI Suite** is the first AI system that integrates Islamic epistemology directly into machine learning architectures. Instead of training on raw internet data, these five frameworks learn from sacred ontological hierarchies, causal rules derived from prophetic traditions, and eschatological signs — creating AI that reasons with theological coherence.

This is **not** a chatbot. This is a **new paradigm** for AI that respects divine unity (tawhid) as a mathematical principle.

## The Five Frameworks

| # | Framework | What It Does | Status |
|---|-----------|-------------|--------|
| 1 | **TES** — Theological Embedding Space | Learns embeddings where vector magnitude reflects ontological proximity to the Divine | ✅ Working |
| 2 | **NBCD** — Nass-Based Causal Discovery | Causal graphs with a latent Divine Will node; detects supernatural intervention from data | ✅ Working |
| 3 | **DNO** — Divine Names Ontology | Multi-attribute optimizer using the 99 Beautiful Names as ethical constraints | ✅ Working |
| 4 | **EPM** — Eschatological Predictive Modeling | Bayesian tracker of the signs of the Hour; early warning for civilizational risks | ✅ Working |
| 5 | **PDI-GPT** — Prophetic Dream Interpreter | Dream interpretation and generation via hadith symbolism (Ibn Sirin methodology) | ✅ Working |

## Quick Start

### Prerequisites

- Python 3.10+ (3.11+ recommended)
- pip

### Install & Run

```bash
# Clone
git clone https://github.com/atharia-agi/tawhid-engine.git
cd tawhid-engine

# Install dependencies
pip install -r requirements.txt

# Run all 5 demos
python run_all_demos.py
```

### One-Click Start

- **Windows**: Double-click `quickstart.bat`
- **Linux/macOS**: Run `bash quickstart.sh`

### CLI Agent

```bash
python agent.py list        # List all projects
python agent.py demo all    # Run all demos
python agent.py check       # Verify file integrity
python agent.py status      # Print suite status
```

## Architecture

```
tawhid-engine/
├── 1.TES/                    # Theological Embedding Space
│   ├── src/                  #   Core module
│   ├── data/                 #   Asmaullah ontology (JSON)
│   └── demo.py               #   Interactive demo
├── 2.NBCD/                   # Nass-Based Causal Discovery
│   ├── src/                  #   Causal graph engine
│   ├── data/                 #   Hadith causal rules (JSON)
│   └── demo.py
├── 3.DNO/                    # Divine Names Ontology
│   ├── src/                  #   Multi-attribute optimizer
│   ├── data/                 #   99 Names config (JSON)
│   └── demo.py
├── 4.EPM/                    # Eschatological Predictive Modeling
│   ├── src/                  #   Bayesian prophecy tracker
│   ├── data/                 #   Signs of the Hour (JSON)
│   └── demo.py
├── 5.PDI-GPT/                # Prophetic Dream Interpreter
│   ├── src/                  #   Dream interpretation engine
│   ├── data/                 #   Dream symbol dictionary (JSON)
│   └── demo.py
├── docs/                     # Sphinx documentation
├── research/                 # Academic papers & source code
│   ├── paper.tex             #   LaTeX academic paper
│   ├── report.html           #   Executive summary
│   └── src/                  #   Tawhid Unifier + Mizan Fairness
├── agent.py                  # CLI manager
├── run_all_demos.py          # Master demo orchestrator
├── verification.py           # File integrity checker
├── pyproject.toml            # Package configuration
└── .github/workflows/ci.yml  # CI/CD pipeline
```

## How Each Framework Works

### 1. TES — Theological Embedding Space

Standard word embeddings (Word2Vec, BERT) learn from co-occurrence statistics. TES learns from **ontological hierarchy**:

```
Allah (Tier 0) — origin, infinite magnitude
  └── Malaikat (Tier 1) — angels, high magnitude
      └── Insan (Tier 3) — humans, medium magnitude
          └── Haiwan (Tier 4) — animals, lower magnitude
              └── Jamad (Tier 6) — inanimate, lowest magnitude
```

The loss function combines contrastive learning with theological constraints:

```
L = L_contrastive + λ_tier × L_tier + λ_hier × L_hierarchical
```

### 2. NBCD — Nass-Based Causal Discovery

NBCD introduces a **latent Divine Will node** into causal graphs. It distinguishes between:

- **Natural causality**: Salat → Heart peace (strength = 0.3)
- **Divine intervention**: Salat → Miraculous outcome (strength = 0.05, but with supernatural boost)

Using Bayesian inference, NBCD estimates: `P(divine intervention | prayer, data)`

### 3. DNO — Divine Names Ontology

DNO treats the 99 Beautiful Names of Allah as **optimization constraints**. Each name maps to a mathematical property:

| Name | Type | Mathematical Property |
|------|------|----------------------|
| Ar-Rahman | Mercy | Minimize harm to vulnerable groups |
| Al-'Adl | Justice | Demographic parity across groups |
| Al-Hakim | Wisdom | Maximize accuracy + minimize complexity |
| Al-Ghaffar | Forgiveness | Allow model recovery from errors |
| Al-Malik | Sovereignty | Enforce hard constraints |
| Ar-Raqib | Watchfulness | Monitor for distribution shift |

### 4. EPM — Eschatological Predictive Modeling

EPM builds a Bayesian network of minor and major signs of the Hour, updating probabilities as real-world events are observed:

```
P(Sign_i | Evidence) = P(Evidence | Sign_i) × P(Sign_i) / P(Evidence)
```

When probability crosses a threshold, it triggers an alert for ethical AI alignment review.

### 5. PDI-GPT — Prophetic Dream Interpreter

Based on Ibn Sirin's methodology, PDI-GPT:

1. **Interprets** user-described dreams by matching symbols to hadith meanings
2. **Generates** dream narratives for spiritual goals (guidance, healing, peace)

## Research

The `research/` directory contains:

- **paper.tex** — Full academic paper (LaTeX)
- **report.html** — Executive summary
- **10+ framework specifications** — Detailed technical documents
- **src/tawhid_unifier/** — Multi-modal fusion engine
- **src/mizan_fairness/** — Islamic fairness metrics

## Documentation

Full API documentation is built with Sphinx and available at:

- **Local**: `docs/_build/html/index.html` (run `make docs`)
- **Online**: [atharia-agi.github.io/tawhid-engine](https://atharia-agi.github.io/tawhid-engine)

## Contributing

We welcome contributions from:

- **AI Researchers** — Improve the mathematical foundations
- **Islamic Scholars** — Validate theological accuracy
- **Engineers** — Build applications and integrations
- **Data Scientists** — Enrich datasets (Quran, Hadith, Tafsir)

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

- **Code**: MIT License
- **Documentation & Data**: CC-BY-SA 4.0

## Citation

```bibtex
@misc{divine-ai-suite-2026,
  title={Divine AI Suite: Five Revolutionary Frameworks},
  author={Atharia AGI Team},
  year={2026},
  url={https://github.com/atharia-agi/tawhid-engine}
}
```

## Roadmap

### v0.1.0 (Current)
- ✅ Five framework prototypes
- ✅ Working demos for all frameworks
- ✅ Sphinx documentation
- ✅ CI/CD pipeline

### v0.2.0
- [ ] Enrich datasets (full Quran lexicon, 100+ hadith causal rules, all 99 Names)
- [ ] Unit tests (80%+ coverage)
- [ ] PyPI packages
- [ ] Integration layer (frameworks talk to each other)

### v0.3.0
- [ ] Training on real datasets with GPU
- [ ] Academic paper submission (NeurIPS, AIES, FAccT)
- [ ] API server for external use
- [ ] Dashboard visualization

### v1.0.0
- [ ] Full integration: TES → NBCD → DNO → EPM → PDI-GPT pipeline
- [ ] Validation by Islamic scholars + AI researchers
- [ ] Production-ready API
- [ ] Peer-reviewed publication
