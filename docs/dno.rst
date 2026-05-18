Divine Names Ontology (DNO)
============================

The Divine Names Ontology (DNO) is a multi-attribute optimization framework that uses the 99 Beautiful Names of Allah (Asma ul-Husna) to evaluate and rank decisions across multiple theological dimensions.

Overview
--------

DNO treats each of the 99 Names as an optimization objective, allowing for nuanced decision-making that reflects the multifaceted nature of Divine attributes.

Architecture
------------

The DNO framework includes:

- **Name Registry**: All 99 Names with Arabic, transliteration, and meaning
- **Attribute Scoring**: Each decision is scored against relevant Names
- **Pareto Optimization**: Finds solutions that balance competing Divine attributes
- **Conflict Resolution**: Handles tensions between Names (e.g., Al-Ghaffar vs Al-Adl)

Usage
-----

.. code-block:: python

    import sys
    sys.path.insert(0, 'src')
    from divine_names import DivineNamesOptimizer

    optimizer = DivineNamesOptimizer()
    optimizer.load_names()
    result = optimizer.optimize(decisions, weights={'Al-Rahman': 0.3, 'Al-Adl': 0.2})

API Reference
-------------

.. py:class:: DivineNamesOptimizer

   Main DNO optimizer class.

   .. py:method:: load_names()

      Loads the 99 Beautiful Names.

   .. py:method:: optimize(decisions, weights)

      Optimizes decisions against Divine Names.

      :param decisions: List of decision options
      :param weights: Weight dictionary for each Name
