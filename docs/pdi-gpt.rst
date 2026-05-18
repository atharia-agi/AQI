Prophetic Dream Interpreter (PDI-GPT)
=====================================

Overview
--------

The Prophetic Dream Interpreter (PDI-GPT) is a system for interpreting and generating dreams based on Islamic dream interpretation traditions, particularly drawing from the works of Ibn Sirin and authenticated hadith. PDI-GPT maps dream symbols to their prophetic meanings and can generate dream narratives that encode desired spiritual outcomes (guidance, healing, peace, etc.) using symbols known to have positive connotations in Islamic tradition.

Key Features
------------

- Dream interpretation: Translates user-described dreams into meanings based on hadith literature
- Dream generation: Creates symbolic dream sequences designed to achieve specific spiritual goals
- Symbol dictionary: Curated database of dream symbols (objects, actions, colors, emotions) with meanings from Ibn Sirin and hadith
- Hadith referencing: Each interpretation includes references to supporting hadith where available
- Goal-oriented generation: Generates dreams tailored to outcomes like guidance, healing, solution-finding, peace, and wealth
- Narrative templates: Uses configurable templates to create coherent dream stories from symbolic elements
- Cultural authenticity: Grounded in Islamic epistemology rather than Western psychoanalytic frameworks

Architecture
------------

PDI-GPT consists of two main components:

1. **DreamSymbolDictionary**: 
   - Loads symbol data from JSON (symbols, actions, colors)
   - Provides interpretation via keyword matching
   - Summarizes interpretations into a verdict

2. **DreamScriptGenerator**:
   - Generates dream narratives for specific goals
   - Uses goal-specific symbol sets (e.g., guidance symbols: light, path, water, mountain)
   - Applies narrative templates to create coherent stories
   - Returns scene sequence with optional interpretation

The interpretation process:
    User dream description → Tokenization → Symbol lookup → Meaning aggregation → Verdict

The generation process:
    Goal selection → Symbol sampling → Template filling → Narrative construction

Usage
-----

Basic usage::

    from PDI_GPT.src.dream_engine import DreamSymbolDictionary, DreamScriptGenerator
    
    # Initialize components
    symbol_dict = DreamSymbolDictionary('data/dream_symbols.json')
    generator = DreamScriptGenerator(symbol_dict)
    
    # Interpret a dream
    interpretation = symbol_dict.interpret("I saw water and a key and felt peace")
    print(interpretation['verdict'])
    
    # Generate a dream for guidance
    dream = generator.generate(goal="guidance", length=3)
    print("Generated dream:", dream['scene'])
    
    # Get interpretation of generated dream (optional)
    generated_interpretation = symbol_dict.interpret(" ".join(dream['scene']))

See the `PDI-GPT README <../5.PDI-GPT/README.md>`_ for detailed API documentation and examples.

Theoretical Foundation
----------------------

PDI-GPT is grounded in Islamic dream interpretation traditions:

- Ibn Sirin's *Tabir al-Ruya*: Foundational work on dream interpretation in Islam
- Authenticated hadith about dreams (Sahih Bukhari, Sahih Muslim):

  - "Dreams are of three types: glad tidings from Allah, what the self contemplates, and what the devil suggests."
  - "A good dream is from Allah, so if anyone of you sees a dream which he likes, then he should not tell it to anyone except to whom he loves."
  - "If anyone of you sees a dream which he dislikes, then he should spit on his left side thrice and seek refuge with Allah from Satan and from its evil, for then it will not harm him."

- Works of later scholars like Ibn Qutaybah (Ta'bir al-Ruya) and Al-Nabulsi

The framework operationalizes the Islamic principle that dreams can be meaningful communications while maintaining skepticism about unreliable interpretations. It focuses on the first type of dream (glad tidings from Allah) and uses authenticated symbol meanings to provide beneficial guidance.

References
----------

- Ibn Sirin, M. (Tabir al-Ruya). Dar al-Ma'rifah.
- Al-Nabulsi, A. G. (Kitab al-Isharah li-Wujud al-Tafsir wa-al-I'jaz). Dar al-Kutub al-Ilmiyyah.
- Ibn Qutaybah, A. (Ta'bir al-Ruya). Dar al-Kutub al-Ilmiyyah.
- Sahih Bukhari, Kitab al-Ta'bir (Book of Dream Interpretation).
- Sahih Muslim, Kitab al-Ruya (Book of Dreams).
