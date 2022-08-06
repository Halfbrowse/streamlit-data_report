import streamlit as st
import os
import sys
import numpy as np
import pandas as pd
import plotly as px


def validate_file(file):
    filename = file.name
    name, ext = os.path.splitext(filename)
    if ext in (".csv", ".xlsx"):
        return ext
    else:
        return False


with st.sidebar:

    uploaded_file = st.file_uploader("Upload .csv, .xlsx files not exceeding 200mb")


if uploaded_file is not None:
    ext = validate_file(uploaded_file)
    if ext:
        if ext == ".csv":
            df = pd.read_csv(uploaded_file)

        else:
            xl_file = pd.ExcelFile(uploaded_file)
            sheet_tuple = tuple(xl_file.sheet_names)
            sheet_name = st.sidebar.selectbox("Select the sheet", sheet_tuple)
            df = xl_file.parse(sheet_name)

        cols = df.columns
        st.subheader("Sunburst chart")
        path = st.multiselect("Select the cagetory features", cols)
        fig = px.sunburst(data_frame=df, path=path)
        st.plotly_chart(fig)
