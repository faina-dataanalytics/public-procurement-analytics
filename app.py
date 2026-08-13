"""
TED Decision Support System

Main Streamlit Application
"""

import streamlit as st

from utils.style import load_css
from utils.config import (
    APP_TITLE,
    APP_SUBTITLE,
    SIMULATOR_FIELDS,
    POWER_BI_IFRAME
)

from utils.form_builder import build_form

from services.prediction_service import PredictionService


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(

    page_title=APP_TITLE,

    page_icon="📊",

    layout="wide"

)

load_css()


# ==========================================================
# HEADER
# ==========================================================

col_logo, col_title = st.columns([1, 6])

with col_logo:

    st.image("assets/logo.svg", width=90)

with col_title:

    st.markdown(
        f"""
        <h1 class="main-title">{APP_TITLE}</h1>
        <p class="subtitle">{APP_SUBTITLE}</p>
        """,
        unsafe_allow_html=True
    )


st.divider()


# ==========================================================
# SIMULATOR
# ==========================================================

st.markdown(
    '<h2 class="section-title">Simulation</h2>',
    unsafe_allow_html=True
)

st.write(
    "Geben Sie die wichtigsten Merkmale der Ausschreibung ein."
)

user_input = build_form(SIMULATOR_FIELDS)


simulate = st.button(

    "Simulation starten",

    use_container_width=True

)


# ==========================================================
# PREDICTION
# ==========================================================

if simulate:

    service = PredictionService()

    result = service.predict(user_input)

    st.divider()

    st.markdown(
        '<h2 class="section-title">Ergebnis</h2>',
        unsafe_allow_html=True
    )

    if result["available"]:

        probability = result["probability"] * 100

        risk = result["risk"]

        st.markdown(
            f"""
            <div class="result-card">

                <div class="result-label">

                    Risiko einer geringen Bieterbeteiligung

                </div>

                <div class="result-value">

                    {probability:.1f} %

                </div>

                <div class="risk-level">

                    {risk}

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.warning(

            "Das Machine-Learning-Modell wurde noch nicht eingebunden."

        )


# ==========================================================
# DASHBOARD
# ==========================================================

st.divider()

st.markdown(
    '<h2 class="section-title">Historische Analyse</h2>',
    unsafe_allow_html=True
)

if POWER_BI_IFRAME:

    st.components.v1.iframe(

        POWER_BI_IFRAME,

        height=820,

        scrolling=True

    )

else:

    st.info(

        "Das Power BI Dashboard wird nach der Veröffentlichung eingebunden."

    )


# ==========================================================
# AI ANALYSIS
# ==========================================================

st.divider()

st.markdown(
    '<h2 class="section-title">KI-Analyse</h2>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="coming-soon">

        <span class="badge">

            Geplant für Version 2.0

        </span>

        <p>

        In einer zukünftigen Version wird dieser Bereich
        durch eine KI-gestützte Analyse erweitert.

        Die KI kombiniert

        Machine Learning,

        historische Vergabedaten

        und generative KI,

        um die Prognose fachlich einzuordnen.

        </p>

    </div>
    """,
    unsafe_allow_html=True
)
