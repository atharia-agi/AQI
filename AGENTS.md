# AGENTS.md — Divine AI Suite Agent Instructions

> This file tells AI coding agents (Claude Code, Codex, Cursor, etc.) how to work with this codebase. Read it before making any changes.

---

## Project Identity

- **Name**: Divine AI Suite (a.k.a. Tawhid Engine)
- **Repo**: `atharia-agi/tawhid-engine`
- **License**: MIT (code), CC-BY-SA 4.0 (docs & data)
- **Python**: 3.10+ (target: 3.11, 3.12)
- **OS**: Cross-platform (Windows, Linux, macOS)

---

## Architecture Overview

This is a **mono-repo** containing 5 independent AI frameworks + research code. Each framework lives in its own numbered directory:

```
1.TES/          → Theological Embedding Space
2.NBCD/         → Nass-Based Causal Discovery
3.DNO/          → Divine Names Ontology
4.EPM/          → Eschatological Predictive Modeling
5.PDI-GPT/      → Prophetic Dream Interpreter
research/       → Academic papers + Tawhid Unifier + Mizan Fairness
docs/           → Sphinx documentation
```

### Root-Level Scripts

| File | Purpose |
|------|---------|
| `agent.py` | CLI manager (`python agent.py demo all`, `python agent.py check`, etc.) |
| `run_all_demos.py` | Orchestrates all 5 demos sequentially |
| `verification.py` | File integrity checker |
| `quickstart.bat` | Windows one-click starter |
| `quickstart.sh` | Unix/Linux/macOS one-click starter |

---

## Coding Conventions

### Python Style

- **Formatter**: Black (line length 100)
- **Sorter**: isort (profile: black)
- **Lint**: flake8 (critical errors only: E9, F63, F7, F82)
- **Type hints**: Optional, not enforced (mypy `disallow_untyped_defs = false`)

### File Encoding

- **UTF-8** only. NO BOM.
- **NO emojis** in code files. Use `[OK]`, `[FAIL]`, `[WARN]` instead.
- **NO non-breaking hyphens** (U+2011). Use regular hyphens `-`.
- **NO non-breaking spaces** (U+00A0). Use regular spaces.
- Line endings: CRLF on Windows, LF on Linux (git handles conversion).

### Import Patterns

Each framework demo uses local imports:

```python
# Inside 1.TES/demo.py
import sys
sys.path.insert(0, 'src')
from theological_embedding import TheologicalEmbedding, build_tier_mapping

# Inside 2.NBCD/demo.py
from src.causal_graph import NBCDGraph, DivineInterventionPrior
```

This is intentional — demos are designed to run from within their project directory.

### Print Statements

- Use `[OK]`, `[FAIL]`, `[WARN]` prefixes for status messages
- Use f-strings with single quotes inside: `f"value={data['key']}"` (Python < 3.12 compat)
- No emojis in any Python file

### Demo Structure

Every `demo.py` must follow this pattern:

```python
def main():
    # ... demo logic ...
    pass

if __name__ == "__main__":
    main()
```

**NEVER** call `main()` at module level. **ALWAYS** use the `if __name__` guard.

---

## Build & Test Commands

### Run Demos

```bash
# All demos
python run_all_demos.py

# Single demo
cd 1.TES && python demo.py

# Via agent
python agent.py demo all
```

### Verify Integrity

```bash
python verification.py
```

### Build Docs

```bash
python -m sphinx -b html docs docs/_build/html
# or
make docs
```

### Lint

```bash
# Critical errors only
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics \
  --exclude=docs,build,dist,*.egg-info,.git,__pycache__,research

# Format check
black --check 1.TES/src 1.TES/demo.py 2.NBCD/src 2.NBCD/demo.py \
  3.DNO/src 3.DNO/demo.py 4.EPM/src 4.EPM/demo.py \
  5.PDI-GPT/src 5.PDI-GPT/demo.py agent.py run_all_demos.py verification.py
```

### CI Pipeline

The GitHub Actions CI (`.github/workflows/ci.yml`) runs:
1. **verify** — `verification.py` + `run_all_demos.py` on Python 3.10, 3.11, 3.12
2. **lint** — flake8 + black check
3. **docs** — Sphinx build + deploy to GitHub Pages (on main/master branch)

---

## Package Configuration

### pyproject.toml

- Project name: `divine-ai-suite`
- Python modules at root: `agent`, `run_all_demos`, `verification`
- Dependencies: torch (CPU), numpy, networkx, transformers, tqdm, scipy
- Dev dependencies: pytest, flake8, black, isort, mypy, sphinx

### Important: Package Names

Python package names **cannot** start with digits or contain hyphens. The numbered directories (`1.TES`, `5.PDI-GPT`) are **not** valid Python packages. They are runtime directories for demos only.

If creating installable packages, rename to: `tes_src`, `nbcd_src`, `dno_src`, `epm_src`, `pdi_gpt_src`.

---

## Documentation Rules

### Sphinx (docs/)

- `docs/conf.py` — Sphinx config (extensions: autodoc, viewcode, napoleon, mathjax)
- `docs/index.rst` — Main page (toctree points to `intro`)
- `docs/intro.rst` — Introduction with nested toctrees
- All `.rst` files must use **regular hyphens**, no non-breaking characters
- Math formulas use `:math:` directive (requires `sphinx.ext.mathjax`)

### API Docs (docs/api.rst)

Documents the public API using `py:module`, `py:class`, `py:method` directives.
Do NOT use `automodule` with the numbered directory paths — they are not valid Python packages.

---

## Research Directory

The `research/` folder contains:

- **paper.tex** — Academic paper (LaTeX, needs TeX Live to compile)
- **references.bib** — BibTeX bibliography
- **report.html** — Executive summary
- **src/tawhid_unifier/** — Multi-modal fusion engine (separate package)
- **src/mizan_fairness/** — Islamic fairness metrics (separate package)

The research code is **independent** from the main 5 frameworks. It has its own `pyproject.toml` and can be installed separately:

```bash
pip install -e research/src/tawhid_unifier
pip install -e research/src/mizan_fairness
```

---

## Common Pitfalls

### 1. f-string Nested Quotes

```python
# WRONG (fails on Python < 3.12)
print(f"value={data["key"]}")

# CORRECT
print(f"value={data['key']}")
```

### 2. Module Imports

```python
# WRONG (numbered directory is not a valid package)
from 1.TES.src.theological_embedding import TheologicalEmbedding

# CORRECT (run from within the directory)
import sys
sys.path.insert(0, 'src')
from theological_embedding import TheologicalEmbedding
```

### 3. Demo Entry Point

```python
# WRONG (causes infinite recursion when imported)
main()

# CORRECT
if __name__ == "__main__":
    main()
```

### 4. Encoding

```python
# WRONG (emoji in code)
print("✅ Success")

# CORRECT
print("[OK] Success")
```

### 5. Path Separators

Use `pathlib.Path` or forward slashes. Avoid hardcoded Windows paths.

```python
# WRONG
path = "K:\\Workspace\\divine-ai-suite\\data"

# CORRECT
from pathlib import Path
path = Path(__file__).parent / "data"
```

---

## Git Workflow

- **Branch**: `main` or `master` (production), `develop` (integration)
- **Commits**: Conventional commits (`feat:`, `fix:`, `docs:`, `chore:`)
- **Push**: Always push after committing
- **CI**: Must pass before merging

---

## What NOT to Do

1. **DO NOT** add emojis to any `.py` file
2. **DO NOT** use non-breaking hyphens (U+2011) or spaces (U+00A0) in code
3. **DO NOT** call `main()` at module level in any demo
4. **DO NOT** use nested double quotes in f-strings (Python < 3.12 compat)
5. **DO NOT** hardcode absolute paths
6. **DO NOT** modify the numbered directory structure (`1.TES/`, `2.NBCD/`, etc.)
7. **DO NOT** remove the `if __name__ == "__main__"` guard from any demo
8. **DO NOT** use `shell=True` in `subprocess.run()` with a list argument
9. **DO NOT** commit `__pycache__/`, `*.pyc`, `docs/_build/`, or `*.bak` files
10. **DO NOT** change the project name or GitHub URLs without updating all references

---

## Quick Reference

| Task | Command |
|------|---------|
| Run all demos | `python run_all_demos.py` |
| Run single demo | `cd 1.TES && python demo.py` |
| Check integrity | `python verification.py` |
| Build docs | `python -m sphinx -b html docs docs/_build/html` |
| Format code | `black 1.TES/src 1.TES/demo.py ...` |
| Lint | `flake8 . --select=E9,F63,F7,F82 --exclude=docs,build,research` |
| Install deps | `pip install -r requirements.txt` |
| CLI help | `python agent.py help` |

---

*Last updated: 2026-05-18*
