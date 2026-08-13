Preprocessing
"""
Preprocessing Utilities

TED Decision Support System
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


class Preprocessor:
    """
    Converts Streamlit user input into the feature vector
    expected by the trained ML model.
    """

    def __init__(self, feature_order_path: str | None = None):

        self.feature_order = None

        if feature_order_path:

            path = Path(feature_order_path)

            if path.exists():

                with open(path, "r", encoding="utf-8") as file:

                    self.feature_order = json.load(file)

    # ---------------------------------------------------------

    def create_dataframe(self, user_input: dict) -> pd.DataFrame:
        """
        Converts the simulator dictionary into a DataFrame.
        """

        return pd.DataFrame([user_input])

    # ---------------------------------------------------------

    def align_columns(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Ensures that the column order matches the ML model.
        """

        if self.feature_order is None:

            return dataframe

        for column in self.feature_order:

            if column not in dataframe.columns:

                dataframe[column] = 0

        dataframe = dataframe[self.feature_order]

        return dataframe

    # ---------------------------------------------------------

    def transform(self, user_input: dict) -> pd.DataFrame:
        """
        Complete preprocessing pipeline.
        """

        dataframe = self.create_dataframe(user_input)

        dataframe = self.align_columns(dataframe)

        return dataframe
