Prophetic Dream Interpreter (PDI-GPT)
======================================

The Prophetic Dream Interpreter (PDI-GPT) is a framework for dream interpretation based on hadith symbols and prophetic tradition.

Overview
--------

PDI-GPT uses a database of dream symbols from authentic hadith to interpret dreams according to the prophetic tradition.

Architecture
------------

The PDI-GPT framework includes:

- **Symbol Database**: Dreams and their interpretations from Sahih al-Bukhari and other sources
- **Context Analyzer**: Considers dreamer's circumstances and emotional state
- **Interpretation Engine**: Maps symbols to meanings using hadith-based rules
- **Generation Module**: Produces coherent interpretations in natural language

Usage
-----

.. code-block:: python

    import sys
    sys.path.insert(0, 'src')
    from dream_interpreter import DreamInterpreter

    interpreter = DreamInterpreter()
    interpreter.load_symbols()
    result = interpreter.interpret('I saw myself flying in the sky')
    print(result['interpretation'])

API Reference
-------------

.. py:class:: DreamInterpreter

   Main dream interpreter class.

   .. py:method:: load_symbols()

      Loads dream symbols from hadith.

   .. py:method:: interpret(dream_text)

      Interprets a dream.

      :param dream_text: Dream description
      :type dream_text: str
      :return: Interpretation result
