# Divine AI Suite — Quickstart Guide

Welcome to the first‑ever collection of AI frameworks inspired by Quranic & Hadith wisdom.

## Prerequisites

- **Python 3.10+** (recommended: 3.11 or 3.12)
- **Git** (optional, for version control)
- **Virtual environment** (venv or conda) – highly recommended

## Installation Steps

### 1. Clone or Download the Suite

```bash
# If using git
git clone <your-repo-url>
cd divine-ai-suite

# Or just navigate to the folder
cd K:\\Quranic_AI
```

### 2. Create & Activate Virtual Environment

```bash
# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python agent.py check
```

You should see a green check for all 5 projects.

## Running Demos

### All demos at once

```bash
python run_all_demos.py
```

Or use the Makefile:

```bash
make demo-all          # Run all 5 demos sequentially
```

### Individual project demo

```bash
cd 1.TES
python demo.py
```

Repeat for 2.NBCD, 3.DNO, 4.EPM, 5.PDI-GPT.

## Expected Output

Each demo will print:

- Project title & description
- Synthetic data generation or loading
- Model training (very short, 5‑20 epochs)
- Results: loss curves, sample outputs, success messages
- A final "✅ Demo completed successfully" line.

If you see errors, ensure:
- You are inside the project folder when running `demo.py`
- All files in `data/` exist (they are provided)
- PyTorch is correctly installed (CPU version works fine)

## Project Structure

```
divine-ai-suite/
├── agent.py               # CLI for actions
├── run_all_demos.py       # Master runner
├── requirements.txt       # Python dependencies
├── Makefile               # Shortcuts
├── LICENSE                # MIT
├── README_MAIN.md         # Overview
├── DELIVERABLES.md        # Detailed deliverables matrix
├── QUICKSTART.md          # This file
├── docs/                  # Sphinx documentation (to‑build)
├── 1.TES/
│   ├── src/theological_embedding.py
│   ├── data/asmaullah.json
│   └── demo.py
├── 2.NBCD/
│   ├── src/causal_graph.py
│   ├── data/hadith_causal_rules.json
│   └── demo.py
├── 3.DNO/
│   ├── src/names_optimizer.py
│   ├── data/asmaul_husna.json
│   └── demo.py
├── 4.EPM/
│   ├── src/prophecy_tracker.py
│   ├── data/signatures_of_the_hour.json
│   └── demo.py
└── 5.PDI-GPT/
    ├── src/dream_engine.py
    ├── data/dream_symbols.json
    └── demo.py
```

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|--------------|-----|
| `ModuleNotFoundError: No module named 'torch'` | PyTorch not installed | `pip install torch` |
| `FileNotFoundError` for JSON data | Not running from project folder | `cd` into the specific project before running demo |
| Import errors from `src` | Wrong working directory | Use provided demo scripts (they set `src` correctly) |
| CUDA out of memory | Using GPU with insufficient VRAM | Set `device='cpu'` in demo.py (edit the line) |
| Slow training on CPU | Normal for small nets; use GPU if available | Install CUDA‑compatible torch or increase epochs for full convergence |

## Next Steps

- Explore the **Deliverables Matrix** in `DELIVERABLES.md` to see where to take each project.
- Read `README_MAIN.md` for philosophy and research background.
- Try the **agent CLI**: `python agent.py --help`
- Contribute improvements via pull requests.
- Cite this suite if used in research: include paper.tex or report.pdf.

## Citation

If you use Divine AI Suite in your work, please cite:

```
@software{divine_ai_suite_2025,
  author = {BrowserOS Research},
  title = {Divine AI Suite: Theological Embeddings, Causal Discovery, Divine Names Optimization, Eschatological Modeling, and Prophetic Dream Interpreter},
  year = {2025},
  url = {https://github.com/browseros-research/divine-ai-suite}
}
```

## License

MIT License (see LICENSE file). Use freely for research, education, and commercial purposes.

## Contact

For questions, issues, or collaboration: open an issue on GitHub or reach out to the maintainer.

---

**May your AI be aligned with wisdom that transcends time.** 🤲

