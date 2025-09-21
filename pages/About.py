import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️")

st.title("Your Name Here")  # <-- replace with your name

st.markdown(
    """
**Project summary (example — 100–150 words)**

During the DSHI course I worked on a small data science project aimed at demonstrating the end-to-end process of data preparation, exploratory analysis and simple visualization. I used synthetic and example clinical datasets to practice cleaning, summarising and visualising key indicators using Python (pandas, NumPy) and Streamlit for rapid dashboard prototyping. The project demonstrates generating reproducible synthetic samples, exploratory plots (distribution, boxplot), and a lightweight interactive dashboard to share results. The primary learning objectives were reproducibility, UI layout for non-technical stakeholders, and integrating interactive widgets for rapid hypothesis testing.
"""
)