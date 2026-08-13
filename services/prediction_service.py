"""
Prediction Service

TED Decision Support System
"""

from pathlib import Path

import joblib
import pandas as pd

from utils.config import (
    MODEL_PATH,
    FEATURE_ORDER_PATH
)

from utils.preprocessing import Preprocessor


class PredictionService:
    """
    Handles loading the trained model and generating predictions.
    """

    def __init__(self):

        self.model = None

        self.preprocessor = Preprocessor(
            FEATURE_ORDER_PATH
        )

        self.load_model()

    # ---------------------------------------------------------
    # Load Model
    # ---------------------------------------------------------

    def load_model(self):

        path = Path(MODEL_PATH)

        if path.exists():

            self.model = joblib.load(path)

        else:

            self.model = None

    # ---------------------------------------------------------
    # Prediction
    # ---------------------------------------------------------

    def predict(self, user_input: dict):

        """
        Predict probability of low bidder participation.

        Parameters
        ----------
        user_input : dict

        Returns
        -------
        dict
        """

        if self.model is None:

            return {

                "available": False,

                "probability": None,

                "risk": None

            }

        dataframe = self.preprocessor.transform(user_input)

        probability = float(

            self.model.predict_proba(dataframe)[0][1]

        )

        return {

            "available": True,

            "probability": probability,

            "risk": self.get_risk_level(probability)

        }

    # ---------------------------------------------------------
    # Risk Level
    # ---------------------------------------------------------

    @staticmethod
    def get_risk_level(probability: float):

        """
        Converts probability into business-friendly categories.
        """

        if probability < 0.30:

            return "Niedrig"

        elif probability < 0.60:

            return "Mittel"

        return "Hoch"
