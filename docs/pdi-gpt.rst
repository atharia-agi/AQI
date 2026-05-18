Prophetic Dream Interpreter (PDI-GPT)
=====================================

Overview
--------

The Prophetic Dream Interpreter (PDI-GPT) is a system for interpreting and generating dreams based on Islamic dream interpretation traditions, particularly drawing from the works of Ibn Sirin and authenticated hadith.

Key Features
------------

- Dream interpretation: Translates user-described dreams into meanings based on hadith literature
- Dream generation: Creates symbolic dream sequences for specific spiritual goals
- Symbol dictionary: Curated database of dream symbols with meanings from Ibn Sirin
- Hadith referencing: Each interpretation includes supporting hadith references

Architecture
------------

PDI-GPT consists of two main components:

1. **DreamSymbolDictionary**: Loads symbol data, provides interpretation via keyword matching
2. **DreamScriptGenerator**: Generates dream narratives for specific goals using configurable templates

Usage
-----

Basic usage:

.. code-block:: python

    import sys
    sys.path.insert(0, '5.PDI-GPT/src')
    from dream_engine import DreamSymbolDictionary, DreamScriptGenerator

    sym_dict = DreamSymbolDictionary("5.PDI-GPT/data/dream_symbols.json")
    result = sym_dict.interpret("I saw water and a key and felt peace")

    gen = DreamScriptGenerator(sym_dict)
    dream = gen.generate(goal="guidance", length=3)

See the `PDI-GPT README <../5.PDI-GPT/README.md>`_ for more details.

Theoretical Foundation
----------------------

PDI-GPT is grounded in Islamic dream interpretation traditions:

- Ibn Sirin's *Tabir al-Ruya*: Foundational work on dream interpretation in Islam
- Authenticated hadith about dreams (Sahih Bukhari, Sahih Muslim):

  - "Dreams are of three types: glad tidings from Allah, what the self contemplates, and what the devil suggests."
  - "A good dream is from Allah, so if anyone of you sees a dream which he likes, then he should not tell it to anyone except to whom he loves."

- Works of later scholars like Ibn Qutaybah (Ta'bir al-Ruya) and Al-Nabulsi

References
----------

- Ibn Sirin, M. *Tabir al-Ruya*. Dar al-Ma'rifah.
- Al-Nabulsi, A. G. *Kitab al-Isharah*. Dar al-Kutub al-Ilmiyyah.
- Sahih Bukhari, Kitab al-Ta'bir (Book of Dream Interpretation).
- Sahih Muslim, Kitab al-Ruya (Book of Dreams).
