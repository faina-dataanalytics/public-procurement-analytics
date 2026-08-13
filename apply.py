import streamlit as st
from pathlib import Path

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="TED Decision Support System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():

    css_path = Path("assets/css")

    css_files = [
        "variables.css",
        "base.css",
        "layout.css",
        "header.css",
        "cards.css",
        "forms.css",
        "dashboard.css",
        "footer.css",
        "responsive.css"
    ]

    css = ""

    for file in css_files:

        path = css_path / file

        if path.exists():

            css += path.read_text(encoding="utf-8")

    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


load_css()

# ==========================================================
# HEADER
# ==========================================================

col_logo, col_title = st.columns([1, 8])

with col_logo:

    logo_path = "assets/logo.svg"

    if Path(logo_path).exists():
        st.image(logo_path, width=95)

with col_title:

    st.markdown(
        """
        <div class="page-title">
            TED Decision Support System
        </div>

        <div class="page-subtitle">
            Predictive Analytics for Public Procurement in Germany
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="section-divider"></div>',
    unsafe_allow_html=True
)

# ==========================================================
# PROJECT DESCRIPTION
# ==========================================================

st.markdown(
    """
### Projekt

Diese Anwendung kombiniert Machine Learning, Entscheidungsunterstützung
und interaktive Datenanalyse.

Sie unterstützt öffentliche Auftraggeber dabei,

- Ausschreibungen mit erhöhtem Risiko geringer Bieterbeteiligung frühzeitig zu erkennen,
- historische Vergabedaten zu analysieren,
- mögliche Auswirkungen verschiedener Ausschreibungsparameter zu simulieren.
"""
)

st.write("")

# ==========================================================
# SIMULATOR
# ==========================================================

st.markdown(
    '<div class="section-title">Simulation</div>',
    unsafe_allow_html=True
)

left, right = st.columns([1, 1])

with left:

    contract_value = st.number_input(
        "Geschätzter Auftragswert (€)",
        min_value=0,
        value=500000
    )

    procedure = st.selectbox(
        "Vergabeverfahren",
        [
            "Offenes Verfahren",
            "Nichtoffenes Verfahren",
            "Verhandlungsverfahren"
        ]
    )

    cpv = st.selectbox(
        "CPV-Bereich",
        [
            "Bauleistungen",
            "Lieferleistungen",
            "Dienstleistungen"
        ]
    )

with right:

    region = st.selectbox(
        "Bundesland",
        [
            "Bayern",
            "Berlin",
            "Hamburg",
            "Nordrhein-Westfalen"
        ]
    )

    eu_funding = st.selectbox(
        "EU-Förderung",
        [
            "Ja",
            "Nein"
        ]
    )

    days = st.slider(
        "Angebotsfrist (Tage)",
        5,
        120,
        30
    )

st.write("")

predict = st.button("Risiko berechnen")

# ==========================================================
# PREDICTION
# ==========================================================

st.markdown(
    '<div class="section-title">Prognose</div>',
    unsafe_allow_html=True
)

if predict:

    probability = 0.37

    st.markdown(
        f"""
<div class="result-card">

<div class="metric-value">

{probability:.0%}

</div>

<div class="metric-label">

Geschätzte Wahrscheinlichkeit einer geringen Bieterbeteiligung

</div>

</div>
""",
        unsafe_allow_html=True
    )

else:

    st.info("Bitte wählen Sie die Parameter aus und starten Sie die Simulation.")

# ==========================================================
# POWER BI
# ==========================================================

st.write("")

st.markdown(
    '<div class="section-title">Historische Analyse</div>',
    unsafe_allow_html=True
)

st.components.v1.html(
    """
<div class="powerbi">

Power BI Dashboard wird hier eingebettet.

</div>
""",
    height=820
)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
"""
<div class="footer">

TED Decision Support System

Machine Learning • Business Analytics • Decision Support

</div>
""",
unsafe_allow_html=True
)
