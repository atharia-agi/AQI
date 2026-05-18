API Reference
=============

This section documents the public API for each framework in the Divine AI Suite.

Theological Embedding Space (TES)
---------------------------------

.. py:module:: tes_src.theological_embedding

.. py:class:: TheologicalEmbedding(vocab_size, embed_dim, tier_to_indices, margin=1.0, lambda_tier=0.1, lambda_hier=0.1)

   Learns embeddings where vector magnitude correlates with ontological proximity to Divine.

   :param int vocab_size: Number of tokens in vocabulary
   :param int embed_dim: Embedding dimension
   :param dict tier_to_indices: Mapping from tier level to token indices
   :param float margin: Margin for contrastive loss
   :param float lambda_tier: Weight for tier loss
   :param float lambda_hier: Weight for hierarchical loss

   .. py:method:: forward(token_ids, positive_pairs=None, negative_pairs=None)

      Compute total loss combining contrastive, tier, and hierarchical losses.

   .. py:method:: get_ontological_position(token_id)

      Return dict with tier, norm, and embedding for a token.

   .. py:method:: query_similarity(token_a, token_b)

      Return cosine similarity between two token embeddings.

.. py:function:: build_tier_mapping(data_path)

   Build tier mapping from JSON data file.

   :param str data_path: Path to JSON file with tier data
   :return: Dict mapping tier level to list of token indices

Nass-Based Causal Discovery (NBCD)
----------------------------------

.. py:module:: nbcd_src.causal_graph

.. py:class:: NBCDGraph()

   Causal graph with latent Divine Will node for discovering supernatural causality.

   .. py:method:: add_edge(source, target, strength, edge_type="natural")

      Add a causal edge with specified strength.

   .. py:method:: sample_observation(intervention_node=None, noise_std=0.1)

      Generate a synthetic observation from the causal graph.

   .. py:method:: estimate_divine_probability(data, intervention_node, target_node, threshold=2.0)

      Estimate posterior probability of divine intervention.

.. py:class:: DivineInterventionPrior(alpha=1.0, beta=9.0)

   Beta prior for divine intervention probability.

Divine Names Ontology (DNO)
---------------------------

.. py:module:: dno_src.names_optimizer

.. py:class:: DivineNamesOptimizer(attributes_config, init_weights=None, learn_weights=True)

   Multi-attribute optimizer using divine names as constraints.

   :param list attributes_config: List of attribute configurations
   :param list init_weights: Initial weights for each attribute
   :param bool learn_weights: Whether to learn weights during optimization

   .. py:method:: forward(logits, labels)

      Compute weighted loss across all divine attributes.

      :return: (total_loss, weights_dict, losses_dict)

   .. py:method:: get_weights()

      Return current attribute weights as dict.

.. py:data:: DEFAULT_ATTRIBUTES

   Default configuration for 6 divine attributes.

Eschatological Predictive Modeling (EPM)
----------------------------------------

.. py:module:: epm_src.prophecy_tracker

.. py:class:: SignNode(name, category, prior_p_manifest, parents=None, description="", hadith_ref="")

   Represents a single eschatological sign.

.. py:class:: ProphecyBayesNet()

   Bayesian network for tracking signs of the Hour.

   .. py:method:: add_node(node)

      Add a sign node to the network.

   .. py:method:: update_posterior(observations, n_particles=1000)

      Update posterior probability using particle filtering.

      :return: Probability that all major signs will manifest

Prophetic Dream Interpreter (PDI-GPT)
-------------------------------------

.. py:module:: pdi_gpt_src.dream_engine

.. py:class:: DreamSymbolDictionary(data_path)

   Maps dream symbols to their prophetic meanings.

   :param str data_path: Path to JSON symbol database

   .. py:method:: interpret(dream_description)

      Interpret a dream description using symbol matching.

      :return: Dict with interpretations list and verdict string

.. py:class:: DreamScriptGenerator(symbol_dict)

   Generates dream narratives for specific spiritual goals.

   .. py:method:: generate(goal, length=3)

      Generate a dream script for the given goal.

      :return: Dict with goal, symbols_used, narrative, and interpretation

Agent Interface
---------------

.. py:module:: agent

Command-line interface for managing the Divine AI Suite.

Available commands:

- ``help`` - Show help message
- ``list`` - List all projects and status
- ``demo <project|all>`` - Run demo for a project
- ``test <project|all>`` - Run tests for a project
- ``install`` - Install dependencies
- ``build-docs`` - Build Sphinx documentation
- ``check`` - Verify file integrity
- ``status`` - Print suite status
