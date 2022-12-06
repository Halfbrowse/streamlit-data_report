import streamlit as st
import os
import sys
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.header("Please indicate which visualisations you would like to be rendered.")
tab1, tab2 = st.tabs(["Visuals", "More Visuals"])
with tab1:
    df = pd.read_csv("data/melb_data.csv")

    button_1 = st.button("Display entire dataset")
    button_2 = st.button("Display head of dataset")
    button_3 = st.button("Display head of data in json")

    if button_1:
        large_data = st.dataframe(data=df, width=None, height=None)

    if button_2:
        head_data = st.table(data=df.head(5))

    if button_3:
        json = df.head(5).to_dict()
        st.json(json)

    st.markdown("---")

    st.header("Pie and Bar charts")

    st.markdown("---")

    color_option = st.selectbox(
        "Select the category to colour",
        ("Suburb", "Rooms", "Landsize", "CouncilArea"),
        key="qwerty",
    )
    fig = px.scatter(data_frame=df, x="Price", y="Regionname", color=color_option)
    st.plotly_chart(fig)

    st.subheader("Sunburst chart on features")
    path = st.multiselect(
        "Select the category features", ("Suburb", "Rooms", "Landsize", "CouncilArea")
    )
    fig = px.sunburst(data_frame=df, path=path)
    st.plotly_chart(fig)

    fig = px.histogram(data_frame=df, x="Price")
    st.plotly_chart(fig)

    st.subheader("Draw a Histogram for Price and Colour by Region")

    fig = px.histogram(data_frame=df, x="Price", color="Regionname")
    st.plotly_chart(fig)


st.markdown("---")
with tab2:
    # Widgets, dynamically change visualisations
    df = df.head(100)
    data_types = df.dtypes
    cat_cols = tuple(data_types[data_types == "object"].index)
    with st.container():
        feature = st.selectbox(
            "Select the feature you want to display on the charts", cat_cols
        )

        value_counts = df[feature].value_counts()
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Pie Chat")
            # draw pie chart
            fig, ax = plt.subplots()
            ax.pie(value_counts, autopct="%0.2f%%", labels=value_counts.index)
            st.pyplot(fig)
        with col2:
            st.subheader("Bar Chart")
            # draw bar lot
            fig, ax = plt.subplots()
            ax.bar(value_counts.index, value_counts)
            st.pyplot(fig)

    with st.expander("Click here to display value counts"):
        st.dataframe(value_counts)
