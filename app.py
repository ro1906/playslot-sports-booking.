from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PlaySlot — Book your next game",
    page_icon="🎾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      #MainMenu, footer, header { visibility: hidden; }
      .block-container { padding: 0 !important; max-width: 100% !important; }
      [data-testid="stAppViewContainer"] { background: #F8F6F0; }
      iframe { border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "index.html"
html = html_path.read_text(encoding="utf-8")
components.html(html, height=3000, scrolling=True)
