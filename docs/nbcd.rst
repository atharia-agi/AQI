Nass-Based Causal Discovery (NBCD)
==================================

Overview
--------

Nass-Based Causal Discovery (NBCD) is a causal inference framework that incorporates the Islamic concept of *nass* (definitive textual evidence from Qur'an and Sunnah) as latent variables in causal graphs. NBCD distinguishes between natural causal relationships and those that may involve divine intervention, providing a principled way to model supernatural causality while respecting methodological naturalism in scientific inquiry.

Key Features
------------

- Explicit modeling of Divine Will as a latent variable in causal graphs
- Integration of *nass* (definitive religious texts) as constraints on causal structure
- Bayesian estimation of divine intervention probability from observational data
- Separation of natural causal strength from supernatural intervention likelihood
- Compatible with standard causal discovery algorithms (PC, FCI, NOTEARS)
- Provides interpretability metrics for theological vs. natural explanations

Architecture
------------

NBCD extends standard causal discovery by:

1. **Latent Divine Node**: Introduces a latent variable representing Divine Will that can influence observed variables
2. **Textual Constraints**: Uses definitive religious texts (*nass*) to constrain possible causal structures
3. **Bayesian Inference**: Computes posterior probability of divine intervention given data and prior beliefs
4. **Effect Decomposition**: Separates total effect into natural and supernatural components

The causal model is represented as:

.. math::

    P(V, D | \theta) = P(D | \alpha) \prod_{i} P(V_i | Pa(V_i), D, \theta_i)

where :math:`V` are observed variables, :math:`D` is the Divine Will latent variable, and :math:`\theta` are parameters.

Usage
-----

Basic usage::

    from NBCD.src.causal_graph import DivineCausalModel
    
    # Initialize model with variables and nass constraints
    model = DivineCausalModel(variables=['prayer', 'heart_peace', 'miraculous_outcome'])
    
    # Add nass constraints (definitive textual evidence)
    model.add_nass_constraint("prayer -> heart_peace", strength=0.3, source="Quran 13:28")
    
    # Fit model to data
    model.fit(observational_data)
    
    # Estimate divine intervention probability
    prob_divine = model.estimate_divine_intervention('prayer', 'miraculous_outcome')
    
    # Decompose causal effect
    natural_effect, supernatural_effect = model.decompose_effect('prayer', 'heart_peace')

See the `NBCD README <../2.NBCD/README.md>`_ for detailed API documentation and examples.

Theoretical Foundation
----------------------

NBCD is grounded in Islamic theological concepts of:
- *Nass*: Definitive texts that establish certain beliefs or legal rulings
- *Kawniyyat*: Signs of Allah in the cosmos that can be studied empirically
- *Mi'jazaat*: Miracles that exceed natural causal capacities
- *Qadar*: Divine decree and predestination

The framework operationalizes the theological principle that while natural causes operate according to divinely established patterns, Allah retains the ability to intervene in causal chains in accordance with wisdom and purpose.

References
----------

- Al-Ghazali. (Ihya Ulum al-Din). Dar al-Ma'rifah.
- Al-Razi, F. (Mafatih al-Ghayb). Dar Ihya al-Turath al-Arabi.
- Doi, A. R. (1984). *Shariah: The Islamic Law*. Ta-Ha Publishers.
- Hashmi, S. H. (2002). *Islamic Political Ethics: Civil Society, Pluralism, and Conflict*. Princeton University Press.