# This file is based on: https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/app.py

"""An example of showing geographic data."""

import requests
from io import BytesIO

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image

from src.data_filtering import filter_dataframe

DATE_TIME = "date/time"
DATA_PATH = (
    "../data/swansonhealth_2023-01-04_full_data.csv"
)
TOTAL_SAMPLES = 100000
CLIENT_NAME = 'swansonhealth'
TARGET_COL_NAME = 'add_to_cart_to_views'

st.set_page_config(page_title="Data exploration", page_icon="📊",  layout="wide")
st.title(f"Persuasiveness exploration for {CLIENT_NAME}")
st.markdown(
    """
    This is a visual tool to explore persuasivenss of different products and how is can be improved.
    """
)


@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_PATH, nrows=nrows)
    # data.rename(lambda x: str(x).lower(), axis="columns", inplace=True)
    return data


def run():
    data = load_data(TOTAL_SAMPLES)
    st.dataframe(filter_dataframe(data))
    url = st.text_input("Image URL", key="image_url")

    if url != "":
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            st.image(img)
        except:
            st.error("The URL does not seem to be valid.")

    # with st.sidebar:
    if st.checkbox("Show histograms", False):
        st.subheader(
            "Histograms for features"
        )
        # create two columns for charts
        # fig_col1, fig_col2 = st.rows(2)

        # with fig_col1:
        st.markdown("### Target distribution")
        target_hist = px.histogram(data_frame=data, x=TARGET_COL_NAME)
        st.write(target_hist)

        # with fig_col2:
        st.markdown("### Features distribution")
        columns = data.columns
        make_col_choice = st.selectbox('Select the column to visualize distribution:', columns)
        selected_column = data[make_col_choice]

        col1, col2 = st.columns(2)

        with col1:
            feature_hist = px.histogram(data_frame=data, x=selected_column)
            st.write(feature_hist)
        with col2:
            feature_scatter = px.scatter(data, TARGET_COL_NAME, selected_column)
            st.write(feature_scatter)



if __name__ == "__main__":
    run()
