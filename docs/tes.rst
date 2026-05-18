Theological Embedding Space (TES)
=================================

Overview
--------

The Theological Embedding Space (TES) learns embeddings where vector geometry reflects ontological hierarchy derived from Islamic theological concepts. Unlike standard word embeddings that capture co-occurrence statistics, TES organizes concepts according to their relationship to the Divine, creating a space where proximity to the origin represents increasing divine manifestation.

Key Features
------------

- Learns embeddings where vector magnitude correlates with ontological proximity to Divine
- Incorporates 99 Beautiful Names of Allah as structural anchors
- Uses contrastive loss with theological triplets (concept, closer-to-divine, farther-from-divine)
- Embeddings usable for downstream tasks like semantic similarity, classification, and generation
- Visualizable ontology showing conceptual hierarchy from divine attributes to worldly phenomena

Architecture
------------

TES consists of:

1. **Embedding Layer**: Maps theological concepts to vectors in R^n
2. **Theological Constraint Layer**: Applies soft constraints based on known ontological relationships
3. **Contrastive Loss Module**: Optimizes for both statistical and theological fidelity
4. **Annotation Interface**: Allows scholars to provide feedback on embedding quality

The loss function combines:

.. math::

    \mathcal{L} = \mathcal{L}_{\text{contrastive}} + \lambda \mathcal{L}_{\text{theological}}

where :math:`\mathcal{L}_{\text{contrastive}}` pulls related concepts together and pushes unrelated ones apart, and :math:`\mathcal{L}_{\text{theological}}` penalizes violations of known ontological hierarchies.

Usage
-----

Basic usage::

    from TES.src.theological_embedding import TheologicalEmbeddingSpace
    
    # Initialize model
    tes = TheologicalEmbeddingSpace(embedding_dim=128)
    
    # Train on theological concepts dataset
    tes.train(theological_concepts, epochs=100)
    
    # Get embedding for a concept
    vector = tes.get_embedding("tawhid")
    
    # Find concepts similar to a given vector
    similar = tes.find_similar(vector, k=5)

See the `TES README <../1.TES/README.md>`_ for detailed API documentation and training instructions.

Theoretical Foundation
----------------------

TES is grounded in the Islamic concept of *tawhid* (Divine Unity) and the gradation of existence (*tashkik al-wujud*). The embedding space operationalizes the insight that all creation exists on a spectrum of divine manifestation, from the Necessary Existent (Allah) to contingent beings.

References
----------

- Nasr, S. H. (1993). *An Introduction to Islamic Cosmological Doctrines*. SUNY Press.
- Chittick, W. C. (1989). *The Sufi Path of Knowledge: Ibn al-Arabi's Metaphysics of Imagination*. SUNY Press.
- Izutsu, T. (1964). *Ethico-Religious Concepts in the Qur'an*. McGill-Queen's University Press.