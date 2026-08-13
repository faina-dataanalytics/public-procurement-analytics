"""
CSS Loader

TED Decision Support System
"""

from pathlib import Path

import streamlit as st


def load_css():

    css_folder = Path("assets/css")

    css_files = [

        "variables.css",
        "base.css",
        "layout.css",
        "cards.css",
        "buttons.css",
        "dashboard.css",
        "badges.css",
        "responsive.css"

    ]

    css = ""

    for file in css_files:

        path = css_folder / file

        if path.exists():

            css += path.read_text(encoding="utf-8")

    st.markdown(

        f"<style>{css}</style>",

        unsafe_allow_html=True

    )
