import pandas as pd
import streamlit as st
from .settings import *

@st.cache_data(persist=True)
def load_data(nrows=100):
    data = pd.read_csv(DATA_PATH, nrows=nrows)
    return data