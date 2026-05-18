Nass-Based Causal Discovery (NBCD)
==================================

Nass-Based Causal Discovery (NBCD) is a causal inference framework that incorporates a latent Divine Will node (D) into causal graphs, allowing for the modeling of both natural causality and Divine intervention.

Overview
--------

Traditional causal discovery assumes all causality is natural. NBCD introduces:

- **Divine Will Node (D)**: A latent variable representing Divine decree
- **Nass-Based Priors**: Prior probabilities derived from Quranic text
- **Causal Graphs with Divine Intervention**: Edges from D to any node

Architecture
------------

The NBCD graph extends standard causal models:

- Natural causes: X -> Y
- Divine intervention: D -> Y
- Combined: X -> Y <- D

The DivineInterventionPrior class encodes Quranic knowledge about when Divine intervention is more likely.

Usage
-----

.. code-block:: python

    import sys
    sys.path.insert(0, 'src')
    from causal_graph import NBCDGraph, DivineInterventionPrior

    graph = NBCDGraph()
    graph.add_node('prayer', 'outcome')
    graph.add_divine_intervention('outcome')
    graph.compute_causal_effect('prayer', 'outcome')

API Reference
-------------

.. py:class:: NBCDGraph

   Main NBCD graph class.

   .. py:method:: add_node(*nodes)

      Adds nodes to the graph.

   .. py:method:: add_divine_intervention(target)

      Adds a Divine intervention edge.

   .. py:method:: compute_causal_effect(source, target)

      Computes the causal effect between two nodes.

.. py:class:: DivineInterventionPrior

   Encodes Quranic knowledge about Divine intervention likelihood.
