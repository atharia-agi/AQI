Theological Embedding Space (TES)
=================================

The Theological Embedding Space (TES) is a framework that learns vector representations of theological concepts where the geometry of the embedding space reflects the ontological hierarchy of the Quran.

Overview
--------

TES maps concepts like Allah, angels, humans, animals, and inanimate objects into a continuous vector space such that:

- Higher ontological levels are positioned "above" lower ones
- Concepts with similar theological properties cluster together
- The distance between vectors reflects theological similarity

Architecture
------------

The embedding space has three dimensions:

1. **Ontological Level** (y-axis): Position in the hierarchy (0-8)
2. **Knowledge Capacity** (x-axis): Epistemic access and understanding
3. **Free Will** (z-axis): Capacity for moral choice

Usage
-----

.. code-block:: python

    import sys
    sys.path.insert(0, 'src')
    from theological_embedding import TheologicalEmbedding, build_tier_mapping

    tes = TheologicalEmbedding()
    tes.initialize_embeddings()
    tes.visualize()

    tier_map = build_tier_mapping()
    for concept, tier in tier_map.items():
        print(f"{concept}: tier {tier}")

API Reference
-------------

.. py:class:: TheologicalEmbedding

   Main TES class.

   .. py:method:: initialize_embeddings()

      Initializes the embedding space.

   .. py:method:: visualize()

      Visualizes the embedding space.

.. py:function:: build_tier_mapping()

   Builds a mapping of concepts to ontological tiers.
