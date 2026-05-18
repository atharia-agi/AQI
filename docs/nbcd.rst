Nass-Based Causal Discovery (NBCD)
==================================

Overview
--------

Nass-Based Causal Discovery (NBCD) is a causal inference framework that incorporates the Islamic concept of *nass* (definitive textual evidence) as latent variables in causal graphs.

Key Features
------------

- Explicit modeling of Divine Will as a latent variable in causal graphs
- Integration of *nass* as constraints on causal structure
- Bayesian estimation of divine intervention probability from observational data
- Compatible with standard causal discovery algorithms

Architecture
------------

NBCD extends standard causal discovery by:

1. **Latent Divine Node**: Introduces a latent variable representing Divine Will
2. **Textual Constraints**: Uses definitive religious texts to constrain causal structures
3. **Bayesian Inference**: Computes posterior probability of divine intervention
4. **Effect Decomposition**: Separates total effect into natural and supernatural components

Usage
-----

Basic usage:

.. code-block:: python

    import sys
    sys.path.insert(0, '2.NBCD/src')
    from causal_graph import NBCDGraph, DivineInterventionPrior

    graph = NBCDGraph()
    graph.add_edge("salat_prayer", "heart_peace", 0.3, edge_type="prayer")
    graph.add_edge("salat_prayer", "miraculous_outcome", 0.05, edge_type="prayer")

    obs = graph.sample_observation(intervention_node="salat_prayer", noise_std=0.2)
    p_divine = graph.estimate_divine_probability(
        data, intervention_node="salat_prayer",
        target_node="miraculous_outcome", threshold=2.5,
    )

See the `NBCD README <../2.NBCD/README.md>`_ for more details.

Theoretical Foundation
----------------------

NBCD is grounded in Islamic theological concepts of *nass*, *kawniyyat*, *mi'jazaat*, and *qadar*.

References
----------

- Al-Ghazali. *Ihya Ulum al-Din*. Dar al-Ma'rifah.
- Al-Razi, F. *Mafatih al-Ghayb*. Dar Ihya al-Turath al-Arabi.
