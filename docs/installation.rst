Installation
============

System Requirements
-------------------

- **Python**: 3.10, 3.11, or 3.12 (recommended: 3.12)
- **OS**: Windows, Linux, macOS
- **RAM**: 4 GB minimum (8 GB recommended)
- **GPU**: Optional (CUDA-compatible for training)

Install from Source
-------------------

Clone the repository::

    git clone git@github.com:atharia-agi/AQI.git
    cd AQI

Create a virtual environment (recommended)::

    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate     # Windows

Install dependencies::

    pip install -r requirements.txt

For GPU support (optional)::

    pip install torch --index-url https://download.pytorch.org/whl/cu121

Verify Installation
-------------------

Run the integrity checker::

    python verification.py

Run all demos::

    python run_all_demos.py

Or run a single demo::

    cd 1.TES && python demo.py

Development Installation
------------------------

For development, install with dev dependencies::

    pip install -e ".[dev]"

This includes pytest, flake8, black, isort, mypy, and sphinx.
