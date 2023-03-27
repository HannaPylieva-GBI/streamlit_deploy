import requests
from io import BytesIO

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image

from src.data_filtering import filter_dataframe
from src.load import load_data
from src.settings import *

st.set_page_config(page_title="Data exploration", page_icon="📊",  layout="wide")
st.title(f"Persuasiveness exploration for {CLIENT_NAME}")

st.markdown(
    """
    This is a visual tool to explore persuasivenss of different products and how is can be improved.
    """
)


def run():
    df = load_data(TOTAL_SAMPLES)
    numeric_columns = list(df.select_dtypes('number'))
    st.dataframe(filter_dataframe(df))
    url = st.text_input("Image URL", key="image_url")

    if url != "":
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            st.image(img)
        except:
            st.error("The URL does not seem to be valid.")

    if st.checkbox("Show histograms", False):
        st.subheader(
            "Histograms for features"
        )
        st.markdown("### Target distribution")
        target_hist = px.histogram(data_frame=df, x=TARGET_COL_NAME)
        st.write(target_hist)

        st.markdown("### Features distribution")
        make_col_choice = st.selectbox('Select the column to visualize distribution:', numeric_columns)
        selected_column = df[make_col_choice]

        col1, col2 = st.columns(2)

        with col1:
            feature_hist = px.histogram(data_frame=df, x=selected_column)
            st.write(feature_hist)
        with col2:
            feature_scatter = px.scatter(df, TARGET_COL_NAME, selected_column)
            st.write(feature_scatter)

if __name__ == "__main__":
    run()
