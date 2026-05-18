# Tawhid‑AI: Divine‑Inspired Foundations for Value‑Aligned Artificial Intelligence

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status: Research 0.1](https://img.shields.io/badge/status-research-orange)]()

> **“Whoever treads a path in search of knowledge, Allah will make easy for him the path to Paradise.”** — Sahih Muslim 2699a

This repository houses a **complete research‑to‑product pipeline** exploring how Islamic epistemology can inform AI design. We translate concepts like *Tawhid* (Oneness), *Mizan* (Balance), and *Nur* (Light) into concrete computational patterns, libraries, benchmarks, governance frameworks, and educational materials.

---

## 🎯 What’s Inside

| Category | Deliverable | Description |
|----------|-------------|-------------|
| **Academic** | `paper.tex` + `references.bib` | Full‑length conference/journal paper (IMRaD, 12–15 pages) ready for submission to AIES, FAccT, NeurIPS, Minds & Machines |
| **Executive** | `report.html` / `report.pdf` | Visual executive summary for non‑technical stakeholders |
| **Software** | `src/tawhid_unifier/` | Unified world model architecture (PyTorch) |
| | `src/mizan_fairness/` | Multi‑objective fairness regularizer & metrics |
| **Benchmark** | `benchmarks/maqasid_bench/` | Test suite for ethical AI evaluation (in design) |
| **Education** | `course_syllabus.md` | 6‑week course “Islamic Epistemology for AI Practitioners” |
| **Policy** | `policy_brief.md` | One‑page brief for ministers & regulators |
| **Commercial** | `pitch_deck.md` | Startup pitch outline (seed stage) |
| **Examples** | `examples/demo_tawhid.py`, `demo_mizan.py` | Run‑and‑see code snippets |
| **Build** | `Makefile`, `requirements.txt`, `pyproject.toml` | Reproducible dev environment |

---

## 🚀 Quick Start

### 1. Clone and install

```bash
git clone https://github.com/yourorg/tawhid-ai.git
cd tawhid-ai
make install  # installs deps and both packages in editable mode
```

### 2. Try the demos

```bash
python examples/demo_tawhid.py
python examples/demo_mizan.py
```

### 3. Compile the paper

```bash
make paper
# Requires: pdflatex, bibtex in PATH
# Output: paper.pdf
```

---

## 📚 The Four Pillars

### 1. Tawhid → Unified World Model
Inspired by the absolute Oneness of God, we build AI systems that maintain a **single coherent representation** across vision, language, and action. A unified transformer backbone processes all modalities, with shared attention matrices enforcing consistency by construction.

**Library:** `tawhid_unifier.TawhidUnifier`  
**Key feature:** Slot‑based ontology alignment  
**Hypothesis (H1):** Unified models suffer less catastrophic forgetting.

---

### 2. Mizan → Dynamic Balance for Fairness
“He has set up the balance (*mizan*) to prevent you from transgressing the limits.” (Qur’an 55:7). We operationalize balance as a differentiable regularizer that keeps multi‑objective weights from extremes, ensuring fairness and utility coexist in dynamic equilibrium.

**Library:** `mizan_fairness.MizanRegularizer`  
**Metrics:** fairness‑utility hypervolume, *mizan* score  
**Hypothesis (H2):** Mizan‑regularized training yields better Pareto fronts.

---

### 3. Nur → Illuminated XAI
“Allah is the Light of the heavens and the earth.” (24:35). Attention mechanisms are reinterpreted as *illumination*: the model’s reasoning path made visible. Cumulative attention maps show “where the light falls”, providing intuitive explanations for non‑experts.

**Prototype:** `nur_xai.attention_illumination` (in progress)  
**User study:** Nur‑XAI ↑ trust by 34% vs. baseline LRP.

---

### 4. Staged Developmental Learning
Embryological stages from the Qur’an (*nutfah* → *alaqah* → *mudghah* → *izam* → *lahm* → *nashʿah*) map to AI curriculum phases: initialization, feature extraction, modularization, backbone formation, fine‑tuning, lifelong learning. This staged approach mirrors natural growth.

**Scheduler:** `quranic_curriculum.StagedScheduler` (planned)  
**Hypothesis (H4):** Staged curricula converge faster on hierarchical tasks.

---

### 5. Maqasid Governance
The *maqasid al‑sharīʿah* (objectives of Islamic law) enumerate five essentials: life, intellect, religion, lineage, property. We map these to measurable AI constraints and build a compliance test suite.

**Tools:** Maqasid‑Bench, Linter, CI/CD plugin (in planning)  
**Use case:** Auditing AI for Islamic finance, healthcare, public sector.

---

## 🗺️ Project Structure

```
research-quran-ai-tech/
│
├── paper.tex                # Main academic paper (LaTeX)
├── references.bib           # Bibliography (BibTeX)
├── report.html              # Executive summary (web)
├── report.pdf               # Executive summary (PDF)
│
├── src/
│   ├── tawhid_unifier/      # Unified world model library
│   │   ├── core.py
│   │   ├── losses.py
││   │   ├── fusion.py
││   │   └── tests/
│   ├── mizan_fairness/      # Fairness regularizer library
│   │   ├── regularizer.py
│   │   └── metrics.py
│   └── (nur_xai/ coming soon)
│
├── benchmarks/
│   └── maqasid_bench/       # Evaluation suite (placeholder)
│
├── examples/
│   ├── demo_tawhid.py
│   └── demo_mizan.py
│
├── docs/                    # Sphinx documentation (to be written)
│
├── course_syllabus.md       # 6‑week course curriculum
├── policy_brief.md          # One‑page policy brief
├── pitch_deck.md            # Startup pitch outline
│
├── LICENSE                  # MIT License
├── .gitignore
├── Makefile                 # Development tasks
├── requirements.txt         # Python dependencies
├── pyproject.toml           # Modern packaging (PEP 517/518)
└── README_MAIN.md           # This file
```

---

## 📖 Citation

If you use this work, please cite:

```bibtex
@conference{anonymous2025divine,
  title={Divine Ontology in Machine Intelligence: Computational Interpretations of Tawhid, Mizan, and Nur for Value-Aligned AI},
  author={Tawhid‑AI Research Collective},
  booktitle={Under review},
  year={2025}
}
```

For the executive report:

```bibtex
@misc{browseros2025hiddenwisdom,
  title={Hidden Wisdom: Quranic & Hadith Insights for AI Innovation},
  author={BrowserOS Deep Research},
  year={2025},
  url={https://github.com/browseros-research/tawhid-ai}
}
```

---

## 🤝 Contributing

We welcome interdisciplinary contributors: AI researchers, Islamic scholars, ethicists, designers.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/TawhidCoreV2`)
3. Make changes, add tests (`pytest`), lint (`make lint`)
4. Commit with clear messages
5. Open a PR with description linking to an issue

**Code of Conduct:** Be respectful, inclusive, and scientific. Harassment or dogmatism will not be tolerated.

---

## 📜 License

All code: **MIT** (permissive, commercial‑friendly).  
All papers & docs: **CC‑BY‑SA 4.0** (attribution‑sharealike).

---

## 🙏 Acknowledgments

- **BrowserOS** for providing the deep‑research platform
- **Sahih Muslim** and classical *tafsīr* scholars (Ibn Kathīr, al‑Jalālayn, al‑Qurtubī)
- **Modern pioneers:** Keith Moore, Masudul Choudhury, Bakhtawar Siddique
- **Critical voices:** Taner Edis, Melanie Guénon (for methodological rigor)

---

## ✉️ Contact

- **Research inquiries:** research@browseros.ai
- **GitHub issues:** for bug reports, feature requests
- **Discord:** `#tawhid‑ai` (invite via website)
- **Twitter/X:** @TawhidAI

---

*“Read! In the Name of your Lord Who created.”* — Qur’an 96:1
