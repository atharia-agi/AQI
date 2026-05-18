Usage
=====

Running Demos
-------------

All demos can be run sequentially::

    python run_all_demos.py

Or individually::

    cd 1.TES && python demo.py
    cd ../2.NBCD && python demo.py
    cd ../3.DNO && python demo.py
    cd ../4.EPM && python demo.py
    cd ../5.PDI-GPT && python demo.py

Using the CLI
-------------

The agent.py script provides a command-line interface::

    python agent.py demo all      # Run all demos
    python agent.py demo tes      # Run TES demo only
    python agent.py check         # Verify integrity
    python agent.py help          # Show help

Using Quranic Principles
------------------------

The quranic_principles module is the foundation of AQI::

    from quranic_principles.mathematical_codes import QuranicMathematicalCodes
    from quranic_principles.scientific_references import QuranicScientificReferences
    from quranic_principles.hidden_patterns import QuranicHiddenPatterns
    from quranic_principles.literary_devices import QuranicLiteraryDevices
    from quranic_principles.ontological_hierarchy import QuranicOntologicalHierarchy

    mc = QuranicMathematicalCodes()
    print(mc.get_sea_land_ratio())  # {'sea_percentage': 71.11, 'land_percentage': 28.89}

    sr = QuranicScientificReferences()
    print(sr.get_embryology_stages())  # 6 stages from Surah Al-Mu'minun

Using the Integration Pipeline
------------------------------

The full AQI pipeline connects all frameworks::

    from integration.pipeline import run_aqi_pipeline

    result = run_aqi_pipeline()
    print(result['summary'])

Configuration
-------------

Global configuration is stored in ``configs/default.yaml``. Edit this file to customize parameters for each framework.

Docker
------

Build and run with Docker::

    docker build -t aqi .
    docker run --rm aqi python run_all_demos.py

Or with docker-compose::

    docker-compose up
