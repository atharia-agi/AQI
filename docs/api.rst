API Reference
=============

This page documents the public API of AQI.

Note: The numbered framework directories (1.TES, 2.NBCD, etc.) are runtime directories, not valid Python packages. Their APIs are documented below manually.

Quranic Principles
------------------

.. py:module:: quranic_principles

   The foundation module containing all Quranic principles.

Mathematical Codes
^^^^^^^^^^^^^^^^^^

.. py:class:: QuranicMathematicalCodes

   Mathematical patterns in the Quran.

   .. py:method:: get_sea_land_ratio()

      Returns the sea/land ratio from Quranic word counts.
      
      :return: Dictionary with sea_percentage, land_percentage, and accuracy
      :rtype: dict

   .. py:method:: get_all_symmetries()

      Returns all verified word symmetries.
      
      :return: List of symmetry dictionaries
      :rtype: list

   .. py:method:: check_nineteen_pattern(number)

      Checks if a number is divisible by 19.
      
      :param number: The number to check
      :type number: int
      :return: Dictionary with divisibility info
      :rtype: dict

Scientific References
^^^^^^^^^^^^^^^^^^^^^

.. py:class:: QuranicScientificReferences

   Scientific references in the Quran.

   .. py:method:: get_embryology_stages()

      Returns the 6 stages of embryology from Surah Al-Mu'minun.
      
      :return: List of embryology stage dictionaries
      :rtype: list

   .. py:method:: count_total_references()

      Returns the total number of scientific references.
      
      :return: Total count
      :rtype: int

Hidden Patterns
^^^^^^^^^^^^^^^

.. py:class:: QuranicHiddenPatterns

   Hidden patterns in the Quran.

   .. py:method:: get_all_muqattatat()

      Returns all muqattatat groups.
      
      :return: List of muqattatat group dictionaries
      :rtype: list

   .. py:method:: get_abjad_value(letter)

      Returns the Abjad numerical value of an Arabic letter.
      
      :param letter: Arabic letter
      :type letter: str
      :return: Numerical value
      :rtype: int

Literary Devices
^^^^^^^^^^^^^^^^

.. py:class:: QuranicLiteraryDevices

   Literary devices in the Quran.

   .. py:method:: get_metaphors()

      Returns all documented metaphors.
      
      :return: List of metaphor dictionaries
      :rtype: list

   .. py:method:: get_parables()

      Returns all documented parables.
      
      :return: List of parable dictionaries
      :rtype: list

Ontological Hierarchy
^^^^^^^^^^^^^^^^^^^^^

.. py:class:: QuranicOntologicalHierarchy

   Ontological hierarchy from the Quran.

   .. py:method:: get_all_levels()

      Returns all 9 levels of existence.
      
      :return: List of level dictionaries
      :rtype: list

   .. py:method:: get_level_properties(level)

      Returns properties of a specific level.
      
      :param level: Level number (0-8)
      :type level: int
      :return: Level properties
      :rtype: dict

Theological Embedding Space (TES)
---------------------------------

.. py:class:: TheologicalEmbedding

   Main TES class (from 1.TES/src/theological_embedding.py).

   .. py:method:: initialize_embeddings()

      Initializes the embedding space.

   .. py:method:: visualize()

      Visualizes the embedding space.

.. py:function:: build_tier_mapping()

   Builds a mapping of concepts to ontological tiers.
   
   :return: Dictionary mapping concept names to tier numbers
   :rtype: dict

Nass-Based Causal Discovery (NBCD)
----------------------------------

.. py:class:: NBCDGraph

   Main NBCD graph class (from 2.NBCD/src/causal_graph.py).

   .. py:method:: add_node(*nodes)

      Adds nodes to the graph.
      
      :param nodes: Node names
      :type nodes: str

   .. py:method:: add_divine_intervention(target)

      Adds a Divine intervention edge.
      
      :param target: Target node
      :type target: str

.. py:class:: DivineInterventionPrior

   Encodes Quranic knowledge about Divine intervention likelihood.

Divine Names Ontology (DNO)
---------------------------

.. py:class:: DivineNamesOptimizer

   Main DNO optimizer class (from 3.DNO/src/names_optimizer.py).

   .. py:method:: load_names()

      Loads the 99 Beautiful Names.

   .. py:method:: optimize(decisions, weights)

      Optimizes decisions against Divine Names.
      
      :param decisions: List of decision options
      :type decisions: list
      :param weights: Weight dictionary for each Name
      :type weights: dict
      :return: Optimization result
      :rtype: dict

Eschatological Predictive Modeling (EPM)
-----------------------------------------

.. py:class:: EschatologicalPredictor

   Main EPM predictor class (from 4.EPM/src/eschatological_model.py).

   .. py:method:: load_signs()

      Loads the signs of the Hour.

   .. py:method:: update_evidence(sign_id, evidence_strength)

      Updates evidence for a sign.
      
      :param sign_id: Sign identifier
      :type sign_id: str
      :param evidence_strength: Strength of evidence (0-1)
      :type evidence_strength: float

Prophetic Dream Interpreter (PDI-GPT)
--------------------------------------

.. py:class:: DreamInterpreter

   Main dream interpreter class (from 5.PDI-GPT/src/dream_engine.py).

   .. py:method:: load_symbols()

      Loads dream symbols from hadith.

   .. py:method:: interpret(dream_text)

      Interprets a dream.
      
      :param dream_text: Dream description
      :type dream_text: str
      :return: Interpretation result
      :rtype: dict
