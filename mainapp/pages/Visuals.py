import streamlit as st
import os
import sys
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.header("Please indicate which visualisations you would like to be rendered.")

df = pd.read_csv("data/melb_data.csv")

button_1 = st.button("Display entire dataset")
button_2 = st.button("Display head of dataset")
button_3 = st.button("Display head of data in json")
button_4 = st.button("Display all data in json")


if button_1:
    large_data = st.dataframe(data=df, width=None, height=None)


if button_2:
    head_data = st.table(data=df.head(st.session_state.height))


if button_3:
    json = df.head(5).to_dict()
    st.json(json)


if button_4:
    columns = tuple(df.columns)
    select_column = st.selectbox("Select the column you want to display", columns)
    st.dataframe(df[[select_column]])
