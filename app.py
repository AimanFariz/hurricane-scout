import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
from about import about_page
from home import home_page


st.sidebar.title('Hurricane Scout')
page = st.sidebar.radio('Select a page:', ['About', 'Hurricane Scout'])

# Show the corresponding page based on the selection
if page == 'About':
    about_page()
elif page == 'Hurricane Scout':
    home_page()
else:
    home_page()