Divine Names Ontology (DNO)
===========================

Overview
--------

The Divine Names Ontology (DNO) is a multi-attribute optimization framework that uses the 99 Beautiful Names of Allah as ethical and functional constraints in machine learning models.

Key Features
------------

- Optimization under multiple divine attribute constraints
- Weight balancing system preventing neglect of any divine attribute
- Hadith-informed priority weights for names
- Interpretability module showing which divine names influenced decisions

Architecture
------------

DNO implements a layered optimization approach:

1. **Attribute Encoder**: Maps the 99 Names to measurable mathematical properties
2. **Constraint Layer**: Enforces minimum thresholds for each divine attribute
3. **Weight Balancer**: Dynamically adjusts optimization weights
4. **Loss Function**: Combines task performance with divine attribute compliance

Usage
-----

Basic usage:

.. code-block:: python

    import sys
    sys.path.insert(0, '3.DNO/src')
    from names_optimizer import DivineNamesOptimizer, DEFAULT_ATTRIBUTES

    dno = DivineNamesOptimizer(
        attributes_config=DEFAULT_ATTRIBUTES,
        init_weights=[1.0, 1.0, 1.0, 0.8, 0.5, 0.3],
        learn_weights=True,
    )

    total_loss, weights, losses = dno.forward(logits, labels)
    final_weights = dno.get_weights()

See the `DNO README <../3.DNO/README.md>`_ for more details.

Theoretical Foundation
----------------------

DNO is grounded in Islamic theological concepts of *Asma' Allah al-Husna*, *Tawhid al-Asma' wa al-Sifat*, *Wasatiyyah*, and *Adl wa Ihsan*.

References
----------

- Al-Ghazali. *Ihya Ulum al-Din*. Kitab al-Asma' wa al-Sifat.
- Ibn Arabi, M. *Al-Futuhat al-Makkiyya*. Dar Sadr.
