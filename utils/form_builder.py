utils/form_builder.py
"""
Dynamic Form Builder

TED Decision Support System
"""

import streamlit as st


def build_form(fields):
    """
    Generates the simulator form based on the configuration.

    Parameters
    ----------
    fields : list
        List of dictionaries describing all input fields.

    Returns
    -------
    dict
        User input values.
    """

    values = {}

    left_column, right_column = st.columns(2)

    for index, field in enumerate(fields):

        column = left_column if index % 2 == 0 else right_column

        with column:

            field_type = field["type"]

            # ----------------------------------------
            # Number Input
            # ----------------------------------------

            if field_type == "number":

                values[field["key"]] = st.number_input(

                    label=field["label"],

                    min_value=field.get("min", 0),

                    max_value=field.get("max"),

                    value=field.get("default", 0)

                )

            # ----------------------------------------
            # Select Box
            # ----------------------------------------

            elif field_type == "select":

                values[field["key"]] = st.selectbox(

                    label=field["label"],

                    options=field["options"]

                )

            # ----------------------------------------
            # Slider
            # ----------------------------------------

            elif field_type == "slider":

                values[field["key"]] = st.slider(

                    label=field["label"],

                    min_value=field["min"],

                    max_value=field["max"],

                    value=field["default"]

                )

            # ----------------------------------------
            # Checkbox
            # ----------------------------------------

            elif field_type == "checkbox":

                values[field["key"]] = st.checkbox(

                    field["label"]

                )

            # ----------------------------------------
            # Text Input
            # ----------------------------------------

            elif field_type == "text":

                values[field["key"]] = st.text_input(

                    field["label"]

                )

    return values
