# AQI - Artificial Quranic Intelligence — Quickstart Guide

Welcome to AQI, the first AI system that thinks with the paradigm of the Quran.

## Prerequisites

- **Python 3.10+** (recommended: 3.11 or 3.12)
- **Git** (optional, for version control)
- **Virtual environment** (venv or conda) – highly recommended

## Installation Steps

### 1. Clone or Download the Suite

```bash
# If using git
git clone git@github.com:atharia-agi/AQI.git
cd AQI

# Or just navigate to the folder
cd K:\Quranic_AI
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

You should see a green check for all 5 projects + Quranic Principles.

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

### Test Quranic Principles

```python
from quranic_principles.mathematical_codes import QuranicMathematicalCodes
mc = QuranicMathematicalCodes()
print(mc.get_sea_land_ratio())  # {'sea_percentage': 71.11, 'land_percentage': 28.89}
```

## Expected Output

Each demo will print:

- Project title & description
- Synthetic data generation or loading
- Model training (very short, 5-20 epochs)
- Results: loss curves, sample outputs, success messages
- A final "[OK] Demo completed successfully" line.

If you see errors, ensure:
- You are inside the project folder when running `demo.py`
- All files in `data/` exist (they are provided)
- PyTorch is correctly installed (CPU version works fine)

## Project Structure

```
AQI/
├── quranic_principles/    → Mathematical codes, scientific references, hidden patterns
├── agent.py               # CLI for actions
├── run_all_demos.py       # Master runner
├── requirements.txt       # Python dependencies
├── Makefile               # Shortcuts
├── LICENSE                # MIT
├── README.md              # Overview
├── DELIVERABLES.md        # Detailed deliverables matrix
├── QUICKSTART.md          # This file
├── docs/                  # Sphinx documentation
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
| Slow training on CPU | Normal for small nets; use GPU if available | Install CUDA-compatible torch or increase epochs for full convergence |

## Next Steps

- Explore the **Deliverables Matrix** in `DELIVERABLES.md` to see where to take each project.
- Read `README.md` for philosophy and research background.
- Try the **agent CLI**: `python agent.py --help`
- Contribute improvements via pull requests.
- Cite this suite if used in research: include paper.tex or report.pdf.

## Citation

If you use AQI in your work, please cite:

```
@software{aqi_2026,
  author = {Atharia AGI Team},
  title = {AQI: Artificial Quranic Intelligence},
  year = {2026},
  url = {https://github.com/atharia-agi/AQI}
}
```

## License

MIT License (see LICENSE file). Use freely for research, education, and commercial purposes.

## Contact

For questions, issues, or collaboration: open an issue on GitHub.

---

**May your AI be aligned with wisdom that transcends time.**
