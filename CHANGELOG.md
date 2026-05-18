# Changelog

All notable changes to AQI (Artificial Quranic Intelligence) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.2.0] — 2026-05-18

### Added
- **AQI Rebranding**: Project renamed from "Divine AI Suite" to "AQI - Artificial Quranic Intelligence"
- **Quranic Principles Module** — The foundation of AQI:
  - `mathematical_codes.py`: 19-based system, word symmetries (dunya=akhirah=115, sea/land ratio 71.11%), golden ratio, prime patterns
  - `scientific_references.py`: 21 references including embryology (6 stages), Big Bang, expanding universe, mountains as pegs, iron from space, pain receptors, frontal lobe
  - `hidden_patterns.py`: Abjad numerals (28 letters), muqattatat (11 groups, 29 surahs), ring composition, structural symmetry
  - `literary_devices.py`: 7-layer metaphors, 31x repetition patterns, oaths, rhetorical questions, parables
  - `ontological_hierarchy.py`: Complete 9-level hierarchy from Allah (Level 0) to Jamad (Level 8)
- **Integration Pipeline**: Updated `integration/pipeline.py` to use Quranic Principles as foundation layer
- **Full Infrastructure**:
  - `data_pipeline/` — Quran, Hadith, Tafsir data loaders
  - `training/` — GPU-supported training with checkpointing
  - `integration/` — AQI pipeline orchestrator
  - `evaluation/` — Framework-specific metrics
  - `api/` — FastAPI server for external access
  - `configs/` — YAML configuration files
  - `tests/` — 32 unit tests across all frameworks (32/32 PASS)
  - `Dockerfile` & `docker-compose.yml` — Containerization
- **CI/CD**: Updated to include pytest job on Python 3.10, 3.11, 3.12
- **Documentation**: Complete Sphinx docs with zero warnings

### Changed
- `pyproject.toml`: Project name changed to `aqi`, version 0.2.0-dev
- `README.md`: Comprehensive AQI branding and architecture
- `AGENTS.md`: Updated for AI coding agents
- All documentation files updated with AQI branding

### Fixed
- 142 critical issues: infinite recursion (TES), f-string syntax (NBCD), mojibake, CI/CD mismatches, docs warnings
- Syntax error in `hidden_patterns.py` (center_verse quote)

## [0.1.0] — 2026-05-18

### Added
- Initial creation of the Divine AI Suite with five revolutionary frameworks:
  - **TES** (Theological Embedding Space) — learn ontological tiers from embeddings
  - **NBCD** (Nass-Based Causal Discovery) — causal graphs with divine intervention node
  - **DNO** (Divine Names Ontology) — multi-attribute optimization via Asma'ul Husna
  - **EPM** (Eschatological Predictive Modeling) — Bayesian tracker of signs of the Hour
  - **PDI-GPT** (Prophetic Dream Interpreter) — dream interpretation and generation
- Each project includes:
  - Core module in `src/`
  - JSON data file(s) in `data/`
  - `demo.py` for quick demonstration
  - `README.md` with API documentation
- Root repository files:
  - `README_MAIN.md` — comprehensive overview
  - `DELIVERABLES.md` — deliverables summary and roadmap
  - `LICENSE` (MIT)
  - `requirements.txt`
  - `Makefile` with common commands
  - `run_all_demos.py` — master demo runner
  - `agent.py` — command-line interface for suite management
  - `verification.py` — integrity checker
  - `quickstart.bat` — Windows one-click starter
  - `quickstart.sh` — Unix/Linux/macOS starter
  - `docs/` with Sphinx documentation (zero warnings)
  - `.github/workflows/ci.yml` — CI/CD pipeline
  - `pyproject.toml` — packaging configuration
- Research directory with:
  - Academic paper (LaTeX)
  - Executive summary (HTML/PDF)
  - Framework specifications (10+ documents)
  - Source code for Tawhid Unifier and Mizan Fairness modules

### Known Issues
- Data files are minimal (toy examples); need enrichment with full Arabic lexicon and hadith corpus.
- Unit tests need expansion beyond demo verification.
- Packages not yet published to PyPI.

---

## [Planned] — Upcoming Releases

### 0.3.0 — Data & Training
- Expand datasets: full Quran lexicon, Hadith corpus, Tafsir
- GPU training on real datasets
- Model validation with Islamic scholars + AI researchers

### 1.0.0 — Production Ready
- Stable APIs (semantic versioning)
- Full documentation website (hosted on GitHub Pages)
- Academic paper submission to top conferences (NeurIPS, AIES, FAccT)
- API server deployment
- Community adoption

---

**Note:** This project is experimental and exists at the intersection of computer science and religious epistemology. Use with appropriate caution and scholarly consultation.
