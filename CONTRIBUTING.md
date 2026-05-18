# Contributing to Divine AI Suite

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
git clone https://github.com/yourorg/divine-ai-suite.git
cd divine-ai-suite
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
pre-commit install  # optional: run formatting hooks
```

---

## Project Structure

Each project (1.TES, 2.NBCD, 3.DNO, 4.EPM, 5.PDI-GPT) follows this structure:

```
<project>/
├── src/          # Core Python modules
│   ├── __init__.py
│   └── <module>.py
├── data/         # JSON data files (small, versioned)
├── tests/        # Unit tests (to be added)
├── demo.py       # Demonstration script
└── README.md     # Project-specific details
```

---

## Coding Standards

- **Type hints:** Use for all function signatures.
- **Docstrings:** Google style.
- **Imports:** Use `isort` to sort (standard library, third‑party, local).
- **Formatting:** `black` (line length 88).
- **Error handling:** Raise meaningful exceptions; avoid bare `except`.
- **Logging:** Use `logging` module for debug/info messages in demos.

---

## Research Ethics

These projects engage with religious texts and concepts. Contributors must:

- Respect theological diversity; avoid claiming exclusive truth.
- Clearly distinguish between *inspired computational models* and *religious doctrine*.
- Cite sources accurately (Qur'an, hadith, scholarly works).
- Include methodological caveats (e.g., over‑interpretation risks) in any publication.

---

## Commit Messages

Follow conventional commits format:

```
feat: add Mizan fairness regularizer
fix: correct NBCD intervention sampling
docs: update README with usage examples
test: add unit tests for TheologicalEmbedding
```

---

## License

By contributing, you agree your contributions will be licensed under the MIT License (see LICENSE file).

---

## Questions?

Contact the maintainer: research@browseros.ai or open an issue.

---

*“Whoever treads a path in search of knowledge, Allah will make easy for him the path to Paradise.”* — Sahih Muslim 2699a

Happy coding! 🚀
