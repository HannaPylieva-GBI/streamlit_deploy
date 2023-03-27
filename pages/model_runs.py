import joblib

import shap
import streamlit as st
from src.settings import *
from src.load import load_data


def load_model(model_path):
    with open(model_path, 'rb') as f:
        return joblib.load(f)

st.set_page_config(
    page_title="Model",
    page_icon="👋",
)

st.write("# Here we can check how model prediciton wil change with regard to the input")
df = load_data()
df = df[~df.remove]
df.fillna(0, inplace=True)
numeric_columns = list(df.select_dtypes('number'))
model = load_model(MODEL_PATH)
st.write(numeric_columns)
row_id = 0
inputs = [st.slider(c, min_value=float(df[c].min()), max_value=float(df[c].max()), value=float(df[c].loc[row_id]),
                step=0.01) for c in numeric_columns]

st.write(inputs)
model.predict([inputs])