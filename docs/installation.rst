Installation
============

Prerequisites
-------------

- Python 3.10 or higher (3.11+ recommended)
- pip (Python package manager)
- Git (for cloning the repository)

Steps
-----

1. Clone the repository::

    git clone https://github.com/atharia-agi/tawhid-engine.git
    cd tawhid-engine

2. Install the required dependencies::

    pip install -r requirements.txt

3. (Optional) Install in development mode::

    pip install -e .

4. Verify the installation::

    python verification.py

5. Run all demos::

    python run_all_demos.py

   Or use the quick start script:

   - Windows: ``quickstart.bat``
   - Unix/Linux/macOS: ``bash quickstart.sh``

Note: On Windows, if you encounter issues with the ``python`` command, use ``py`` instead.

Troubleshooting
---------------

- If you get a ``ModuleNotFoundError`` for ``torch``, ensure you have installed the CPU version:

  .. code-block:: bash

      pip install --index-url https://download.pytorch.org/whl/cpu torch>=2.0

- If Sphinx is not found when building docs, install it via:

  .. code-block:: bash

      pip install sphinx sphinx-rtd-theme
