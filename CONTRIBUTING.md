# Contributing to AQI - Artificial Quranic Intelligence

Thank you for your interest in contributing! This document provides guidelines and information for contributors.

---

## How to Contribute

### Reporting Bugs
- Open an issue on GitHub with a clear title and description.
- Include steps to reproduce, expected vs actual behavior.
- Attach logs or screenshots if applicable.

### Suggesting Features
- Open an issue with the tag "enhancement".
- Describe the feature, its use case, and potential impact.
- Discuss with maintainers before starting implementation.

### Submitting Pull Requests
1. Fork the repository and create a feature branch (`git checkout -b feature/AmazingFeature`).
2. Ensure code follows PEP 8 (use `black` and `isort`).
3. Add unit tests for new functionality (pytest).
4. Verify all tests pass: `pytest` or `make test`.
5. Update documentation if needed.
6. Submit PR with clear description and reference to related issue.

---

## Development Setup

```bash
git clone git@github.com:atharia-agi/AQI.git
cd AQI
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## Project Structure

AQI contains 6 pillars: Quranic Principles + 5 AI frameworks:

```
quranic_principles/  → Mathematical codes, scientific references, hidden patterns, literary devices, ontological hierarchy
1.TES/               → Theological Embedding Space
2.NBCD/              → Nass-Based Causal Discovery
3.DNO/               → Divine Names Ontology
4.EPM/               → Eschatological Predictive Modeling
5.PDI-GPT/           → Prophetic Dream Interpreter
research/            → Academic papers + Tawhid Unifier + Mizan Fairness
docs/                → Sphinx documentation
data_pipeline/       → Data loaders (Quran, Hadith, Tafsir)
training/            → Training scripts with GPU support
integration/         → AQI pipeline orchestrator
evaluation/          → Framework-specific metrics
api/                 → FastAPI server
configs/             → YAML configuration files
tests/               → Unit tests (32/32 PASS)
```

Each framework follows this structure:

```
<project>/
├── src/          # Core Python modules
│   ├── __init__.py
│   └── <module>.py
├── data/         # JSON data files (small, versioned)
├── tests/        # Unit tests
├── demo.py       # Demonstration script
└── README.md     # Project-specific details
```

---

## Coding Standards

- **Formatter:** Black (line length 100)
- **Sorter:** isort (profile: black)
- **Lint:** flake8 (critical errors only: E9, F63, F7, F82)
- **Type hints:** Optional, not enforced
- **Docstrings:** Google style
- **Imports:** Use `isort` to sort (standard library, third-party, local)
- **Error handling:** Raise meaningful exceptions; avoid bare `except`
- **Print statements:** Use `[OK]`, `[FAIL]`, `[WARN]` prefixes. NO emojis.
- **Encoding:** UTF-8 only. NO BOM. NO non-breaking hyphens or spaces.

---

## Research Ethics

These projects engage with religious texts and concepts. Contributors must:

- Respect theological diversity; avoid claiming exclusive truth.
- Clearly distinguish between *inspired computational models* and *religious doctrine*.
- Cite sources accurately (Qur'an, hadith, scholarly works).
- Include methodological caveats (e.g., over-interpretation risks) in any publication.

---

## Commit Messages

Follow conventional commits format:

```
feat: add Quranic Principles module
fix: correct NBCD intervention sampling
docs: update README with AQI branding
test: add unit tests for TheologicalEmbedding
```

---

## License

By contributing, you agree your contributions will be licensed under the MIT License (see LICENSE file).

---

## Questions?

Open an issue on GitHub.

---

"Whoever treads a path in search of knowledge, Allah will make easy for him the path to Paradise." — Sahih Muslim 2699a

Happy coding!
