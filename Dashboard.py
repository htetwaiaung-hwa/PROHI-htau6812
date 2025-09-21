import streamlit as st
import numpy as np

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
    layout='wide'
)

# Sidebar configuration with new logo, About page
with st.sidebar:
    st.image("./assets/Sample Project Logo.png")
    st.markdown("## Navigation")
    st.markdown("- Dashboard")
    st.markdown("- About")
    st.divider()
    st.caption("PROHI practice dashboard — synthetic data demo")

# # Page information

st.write("# Welcome to My PROHI Practice Dashboard! 👋")

st.markdown(
"""
    ## Objectives of the Dashboard

    This Practice Sample Dashboard is formulated for follwing reasons:
    - to learn pre-filled codes and features added by the course lealders
    - to practice expertise taughted in the classes and laboratory sessions
    - to fullfill the tasks set in individual assignements
    - to submit individual assignement outputs as per the timeline

"""
)

# You can also add text right into the web as long comments (""")
"""
Note: The practice project is just a sample simple one, not necessarialy at comprehensive and full scale extent.
"""

### UNCOMMENT THE CODE BELOW TO SEE EXAMPLE OF INPUT WIDGETS

# DATAFRAME MANAGEMENT

"""
    Sample Syntheic Data
"""
dataframe = np.random.randn(1, 100)
st.dataframe(dataframe)

# Add a slider to the sidebar:
add_slider = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
