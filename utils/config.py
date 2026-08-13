"""
Configuration
TED Decision Support System
"""

# ==========================================================
# PAGE
# ==========================================================

APP_TITLE = "TED Decision Support System"

APP_SUBTITLE = (
    "Predictive Analytics for Public Procurement in Germany"
)

# ==========================================================
# MODEL
# ==========================================================

MODEL_PATH = "models/model.pkl"

SCALER_PATH = "models/scaler.pkl"

FEATURE_ORDER_PATH = "models/feature_order.json"

# ==========================================================
# POWER BI
# ==========================================================

POWER_BI_IFRAME = ""

# ==========================================================
# INPUT FIELDS
# ==========================================================

SIMULATOR_FIELDS = [

    {
        "key": "contract_value",

        "label": "Geschätzter Auftragswert (€)",

        "type": "number",

        "default": 500000,

        "min": 0
    },

    {
        "key": "procedure",

        "label": "Vergabeverfahren",

        "type": "select",

        "options": [

            "Offenes Verfahren",

            "Nichtoffenes Verfahren",

            "Verhandlungsverfahren"

        ]
    },

    {
        "key": "cpv",

        "label": "CPV-Bereich",

        "type": "select",

        "options": [

            "Bauleistungen",

            "Lieferleistungen",

            "Dienstleistungen"

        ]
    },

    {
        "key": "region",

        "label": "Bundesland",

        "type": "select",

        "options": [

            "Bayern",

            "Berlin",

            "Hamburg",

            "Nordrhein-Westfalen"

        ]
    },

    {
        "key": "eu_funding",

        "label": "EU-Förderung",

        "type": "select",

        "options": [

            "Ja",

            "Nein"

        ]
    },

    {
        "key": "submission_days",

        "label": "Angebotsfrist (Tage)",

        "type": "slider",

        "min": 5,

        "max": 120,

        "default": 30

    }

]
