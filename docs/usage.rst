Usage
=====

Running Demos
-------------

Each framework includes a demo script that showcases its capabilities.

To run all demos sequentially:

.. code-block:: bash

    python run_all_demos.py

To run a specific framework demo:

.. code-block:: bash

    cd 1.TES && python demo.py
    cd ../2.NBCD && python demo.py
    cd ../3.DNO && python demo.py
    cd ../4.EPM && python demo.py
    cd ../5.PDI‑GPT && python demo.py

Using the CLI
-------------

The suite provides a command-line interface via ``agent.py``.

.. code-block:: bash

    python agent.py --help

Available commands:

- ``demo``: Run all demos
- ``check``: Check file integrity of all projects
- ``docs``: Build the documentation
- ``test``: Run tests (if any)

Example:

.. code-block:: bash

    python agent.py demo

Programmatic Usage
------------------

Each framework can be imported and used as a module.

Example for TES:

.. code-block:: python

    from TES.src.theological_embedding import TheologicalEmbeddingSpace
    model = TheologicalEmbeddingSpace(embedding_dim=128)
    # ... train or use model

Refer to each framework's README.md for detailed API documentation.

Customization
-------------

You can modify the configuration files in each project directory to adjust hyperparameters, data paths, etc.

Contributing
------------

See CONTRIBUTING.md for guidelines on how to contribute to the Divine AI Suite.