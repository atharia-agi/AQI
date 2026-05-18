Installation
============

Prerequisites
-------------

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

Steps
-----

1. Clone the repository (if you haven't already)::

    git clone https://github.com/atharia-agi/tawhid-engine.git
    cd tawhid-engine

2. Install the required dependencies::

    pip install -r requirements.txt

3. (Optional) Install in development mode::

    pip install -e .

4. Verify the installation by running the quick start script::

    py quickstart.bat

   Or on Unix-like systems::

    ./quickstart.sh

Note: On Windows, if you encounter issues with the `python` command, use `py` instead.

Troubleshooting
---------------

- If you get a ``ModuleNotFoundError`` for ``torch``, ensure you have installed the CPU version as specified in ``requirements.txt``.
- If Sphinx is not found when building docs, install it via ``pip install sphinx sphinx-rtd-theme``.