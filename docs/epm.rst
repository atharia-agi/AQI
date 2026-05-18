Eschatological Predictive Modeling (EPM)
========================================

Overview
--------

Eschatological Predictive Modeling (EPM) is a Bayesian tracking system that monitors contemporary events against Islamic eschatological signs (Al-Asharat Al-Kubra wa As-Sugra - the major and minor signs of the Hour). EPM provides an early warning system for civilizational risks by updating probabilities of eschatological events based on real-world observations, helping believers distinguish between normal tribulations and signs that may indicate the approaching Hour.

Key Features
------------

- Bayesian network modeling of eschatological signs and their interdependencies
- Real-time data ingestion from news feeds, social media, and sensor networks
- Probability updating of major and minor signs based on observed events
- Distinction between manifestations that are definitive signs vs. coincidental occurrences
- Configurable thresholds for alerts based on scholarly interpretations
- Visualization dashboard showing current state of eschatological timeline
- Compatible with various data sources (RSS feeds, Twitter API, news APIs)

Architecture
------------

EPM consists of:

1. **Sign Ontology**: Hierarchical representation of minor and major signs with source references
2. **Evidence Collector**: Module that gathers and preprocesses data from various sources
3. **Manifestation Detector**: Natural language processing component that identifies sign manifestations in text
4. **Bayesian Updater**: Core algorithm that updates sign probabilities using Bayes' theorem
5. **Interdependency Model**: Captures how signs influence each other (e.g., widespread injustice leads to specific manifestations)
6. **Alert System**: Triggers notifications when probabilities cross defined thresholds

The core updating formula is:

.. math::

    P(S_i | E) = \frac{P(E | S_i) P(S_i)}{P(E)} = \frac{P(E | S_i) P(S_i)}{\sum_j P(E | S_j) P(S_j)}

where :math:`S_i` represents an eschatological sign, :math:`E` represents evidence, and :math:`P(S_i)` is the prior probability.

Usage
-----

Basic usage::

    from EPM.src.prophecy_tracker import EschatologicalPredictiveModel
    
    # Initialize model with signs database
    model = EschatologicalPredictiveModel(signs_database='data/signs.json')
    
    # Add evidence sources (news feeds, social media, etc.)
    model.add_evidence_source('news', NewsAPISource(api_key='...'))
    model.add_evidence_source('social_media', TwitterSource(bearer_token='...'))
    
    # Update with latest evidence
    model.update_evidence()
    
    # Get current probabilities
    probabilities = model.get_sign_probabilities()
    
    # Check if any major signs have high probability
    alert = model.check_major_signs_threshold(threshold=0.5)
    
    # Generate report
    report = model.generate_report()

See the `EPM README <../4.EPM/README.md>`_ for detailed API documentation and configuration options.

Theoretical Foundation
----------------------

EPM is grounded in Islamic eschatological teachings from:
- Qur'an: Numerous verses describe signs of the Hour (e.g., Surah Al-Zalzalah, Surah Yasin, Surah Al-Qiyamah)
- Sahih Bukhari and Sahih Muslim: Collections of hadith detailing major and minor signs
- Works of scholars like Ibn Kathir (Al-Bidayah wan-Nihayah) and Ibn Hajar (Fath al-Bari)
- Contemporary scholars like Yusuf al-Qaradawi and Muhammad al-Ghazali

The framework implements the prophetic tradition of observing signs while avoiding both denial of clear manifestations and excessive speculation about uncertain ones. As the Prophet Muhammad (ﷺ) said: "The signs are like beads on a string; when one follows another, they come quickly." (Hadith)

References
----------

- Ibn Kathir, I. (Al-Bidayah wan-Nihayah). Dar al-Ma'rifah.
- Ibn Hajar al-Asqalani, A. (Fath al-Bari). Dar al-Ma'rifah.
- Al-Qaradawi, Y. S. (2004). *Fiqh al-Jihad: Dhawaabituhu wa-Asluhu*. Maktaba Wahba.
- Nadwi, A. H. (1980). *Mus hoz: Its Meaning and Message*. Islamic Foundation.
- Gibril, H. (2022). *Major Signs of the Hour*. Al-Firdous Ltd.
