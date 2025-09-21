import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋"
)

# Added the "About" page and revising the code in the sidebar
with st.sidebar:
    st.image("./assets/Sample Project Logo.png")
    st.markdown("")
    page = st.radio("Navigation", ["Dashboard", "About"], index=0)
    st.divider()
    st.caption("PROHI practice dashboard — synthetic data demo")

# Page content
# ---------------------------
# Dashboard view
# ---------------------------
if page == "Dashboard":
    st.title("Welcome to My PROHI Practice Dashboard! 👋")
    st.markdown("---")

    # -----------------------------
    # Elemenet 1: Three Widgets
    # -----------------------------
    st.subheader("Widgets")
    c1, c2, c3 = st.columns(3)
    with c1:
        age_widget = st.number_input(
            "Center age point", value=35, min_value=18, max_value=80, step=1, format="%d"
        )
    with c2:
        income_widget = st.slider(
            "Monthly income (median)", min_value=500, max_value=100_000, value=3000, step=50
        )
    with c3:
        education_widget = st.selectbox(
            "Education level",
            ["No formal education", "Primary", "Secondary", "High School", "Undergraduate", "Postgraduate"]
        )

    st.markdown("---")

    # -----------------------------
    # Element 2: Data section (Generate synthetic dataset (n=300) using widget values)
    # -----------------------------
    rng = np.random.default_rng(12345)
    n = 300

    # Ages: centered at age_widget
    ages = rng.normal(loc=float(age_widget), scale=8.0, size=n)
    ages = np.clip(np.round(ages).astype(int), 18, 80)

    # Education: probability for the selected level for the purpose of interaction (May not be fully correct)
    edu_levels = [
        "No formal education",
        "Primary",
        "Secondary",
        "High School",
        "Undergraduate",
        "Postgraduate",
    ]
    base_probs = np.array([0.03, 0.12, 0.35, 0.30, 0.15, 0.05]) #for the purpose of interaction (May not be fully correct)
    sel_idx = edu_levels.index(education_widget)
    boosted = base_probs.copy()
    boosted[sel_idx] = boosted[sel_idx] * 3.0
    probs = boosted / boosted.sum()
    education = rng.choice(edu_levels, size=n, p=probs)

    # Monthly income: centered at income_widget, with reasonable spread
    incomes = rng.normal(loc=float(income_widget), scale=0.6 * float(income_widget), size=n)
    incomes = np.round(np.clip(incomes, 100, 200_000)).astype(int)

    # Build DataFrame
    df = pd.DataFrame({
        "age": ages,
        "education_level": education,
        "monthly_income": incomes
    })

    # -----------------------------
    # Show data and simple summaries
    # -----------------------------
    st.subheader("Household Survey Data -2024")
    st.dataframe(df.head(50))

    # -----------------------------
    # Element 3 - Visualization: Age histogram only
    # -----------------------------
    st.markdown("---")
    st.subheader("Vistualization")
    fig = px.histogram(df, x="age", nbins=15, title="Age distribution -Household Survey Data -2024")
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# About page
# ---------------------------
else:
    st.title("Htet Wai Aung")
    st.markdown(
        """
        During the DSHI course I developed a compact data-science prototype to practise
        data cleaning, exploratory analysis, and visualization. Using synthetic data I
        demonstrated reproducible pipelines with NumPy and pandas and packaged visual
        outputs with Plotly inside a Streamlit dashboard. This project focuses on
        reproducibility and clear UI design for non-technical stakeholders.
        """
    )
    st.markdown("---")
    st.markdown("Author: Htet Wai Aung — htau6812")