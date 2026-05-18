Eschatological Predictive Modeling (EPM)
=========================================

Eschatological Predictive Modeling (EPM) is a Bayesian framework that tracks the signs of the Hour (Ashrat al-Sa'ah) using probabilistic reasoning and historical data.

Overview
--------

EPM models the progression of eschatological signs as a Bayesian inference problem, updating probabilities as new evidence emerges.

Architecture
------------

The EPM framework includes:

- **Sign Registry**: Major and minor signs from hadith literature
- **Bayesian Updater**: Updates probabilities based on new evidence
- **Temporal Model**: Tracks progression over time
- **Confidence Scoring**: Quantifies certainty of each sign's appearance

Usage
-----

.. code-block:: python

    import sys
    sys.path.insert(0, 'src')
    from eschatological_model import EschatologicalPredictor

    predictor = EschatologicalPredictor()
    predictor.load_signs()
    predictor.update_evidence('sign_id', evidence_strength=0.7)
    predictions = predictor.predict()

API Reference
-------------

.. py:class:: EschatologicalPredictor

   Main EPM predictor class.

   .. py:method:: load_signs()

      Loads the signs of the Hour.

   .. py:method:: update_evidence(sign_id, evidence_strength)

      Updates evidence for a sign.

   .. py:method:: predict()

      Returns prediction results.
