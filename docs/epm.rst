Eschatological Predictive Modeling (EPM)
========================================

Overview
--------

Eschatological Predictive Modeling (EPM) is a Bayesian tracking system that monitors contemporary events against Islamic eschatological signs.

Key Features
------------

- Bayesian network modeling of eschatological signs and their interdependencies
- Real-time data ingestion from news feeds and social media
- Probability updating of major and minor signs based on observed events
- Configurable thresholds for alerts based on scholarly interpretations

Architecture
------------

EPM consists of:

1. **Sign Ontology**: Hierarchical representation of minor and major signs
2. **Evidence Collector**: Module that gathers and preprocesses data
3. **Bayesian Updater**: Core algorithm that updates sign probabilities
4. **Alert System**: Triggers notifications when probabilities cross thresholds

The core updating formula uses particle filtering:

.. math::

    P(S_i | E) = \frac{P(E | S_i) P(S_i)}{P(E)}

Usage
-----

Basic usage:

.. code-block:: python

    import sys
    sys.path.insert(0, '4.EPM/src')
    from prophecy_tracker import ProphecyBayesNet, SignNode

    net = ProphecyBayesNet()
    node = SignNode(
        name="trust_liar", category="minor",
        prior_p_manifest=0.01, description="People trust liars",
    )
    net.add_node(node)

    observations = {"trust_liar": True}
    p_end = net.update_posterior(observations, n_particles=5000)

See the `EPM README <../4.EPM/README.md>`_ for more details.

Theoretical Foundation
----------------------

EPM is grounded in Islamic eschatological teachings from the Qur'an, Sahih Bukhari, and Sahih Muslim.

References
----------

- Ibn Kathir, I. *Al-Bidayah wan-Nihayah*. Dar al-Ma'rifah.
- Ibn Hajar al-Asqalani, A. *Fath al-Bari*. Dar al-Ma'rifah.
