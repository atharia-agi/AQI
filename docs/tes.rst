Theological Embedding Space (TES)
=================================

Overview
--------

The Theological Embedding Space (TES) learns embeddings where vector geometry reflects ontological hierarchy derived from Islamic theological concepts. Unlike standard word embeddings that capture co-occurrence statistics, TES organizes concepts according to their relationship to the Divine.

Key Features
------------

- Learns embeddings where vector magnitude correlates with ontological proximity to Divine
- Incorporates 99 Beautiful Names of Allah as structural anchors
- Uses contrastive loss with theological triplets
- Embeddings usable for downstream tasks like semantic similarity and classification
- Visualizable ontology showing conceptual hierarchy

Architecture
------------

TES consists of:

1. **Embedding Layer**: Maps theological concepts to vectors in R^n
2. **Theological Constraint Layer**: Applies soft constraints based on known ontological relationships
3. **Contrastive Loss Module**: Optimizes for both statistical and theological fidelity

The loss function combines:

.. math::

    \mathcal{L} = \mathcal{L}_{contrastive} + \lambda_{tier} \mathcal{L}_{tier} + \lambda_{hier} \mathcal{L}_{hier}

Usage
-----

Basic usage:

.. code-block:: python

    import sys
    sys.path.insert(0, '1.TES/src')
    from theological_embedding import TheologicalEmbedding, build_tier_mapping

    tier_map = build_tier_mapping("1.TES/data/asmaullah.json")
    vocab_size = max(max(ids) for ids in tier_map.values()) + 1

    model = TheologicalEmbedding(
        vocab_size=vocab_size,
        embed_dim=64,
        tier_to_indices=tier_map,
        margin=1.0,
        lambda_tier=0.1,
        lambda_hier=0.1,
    )

    # Training step
    loss = model(
        token_ids=torch.randint(0, vocab_size, (4, 5)),
        positive_pairs=pos_pairs,
        negative_pairs=neg_pairs,
    )

    # Query ontological position
    info = model.get_ontological_position(token_id)
    sim = model.query_similarity(token_a, token_b)

See the `TES README <../1.TES/README.md>`_ for more details.

Theoretical Foundation
----------------------

TES is grounded in the Islamic concept of *tawhid* (Divine Unity) and the gradation of existence (*tashkik al-wujud*).

References
----------

- Nasr, S. H. (1993). *An Introduction to Islamic Cosmological Doctrines*. SUNY Press.
- Chittick, W. C. (1989). *The Sufi Path of Knowledge*. SUNY Press.
- Izutsu, T. (1964). *Ethico-Religious Concepts in the Qur'an*. McGill-Queen's University Press.
