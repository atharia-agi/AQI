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
    cd ../5.PDI-GPT && python demo.py

Using the CLI
-------------

The suite provides a command-line interface via ``agent.py``.

.. code-block:: bash

    python agent.py help

Available commands:

- ``list`` - List all projects and status
- ``demo all`` - Run all demos
- ``demo 1.TES`` - Run a specific demo
- ``check`` - Verify file integrity
- ``status`` - Print suite status
- ``install`` - Install dependencies
- ``build-docs`` - Build documentation

Example:

.. code-block:: bash

    python agent.py demo all
    python agent.py check

Programmatic Usage
------------------

Each framework can be imported and used as a module.

Example for TES:

.. code-block:: python

    import sys
    sys.path.insert(0, '1.TES/src')
    from theological_embedding import TheologicalEmbedding, build_tier_mapping

    tier_map = build_tier_mapping("1.TES/data/asmaullah.json")
    model = TheologicalEmbedding(vocab_size=100, embed_dim=64, tier_to_indices=tier_map)

Refer to each framework's README.md for detailed API documentation.

Customization
-------------

You can modify the configuration files in each project directory to adjust hyperparameters, data paths, etc.

Contributing
------------

See CONTRIBUTING.md for guidelines on how to contribute to the Divine AI Suite.
