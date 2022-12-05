import streamlit as st
import os
import sys
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.header("Please indicate which visualisations you would like to be rendered.")

df = pd.read_csv("data/melb_data.csv")


button_1 = st.button("Display entire dataset")
button_2 = st.button("Display head of dataset")
button_3 = st.button("Display head of data in json")
button_4 = st.button("Display column")

if button_1:
    large_data = st.dataframe(data=df, width=None, height=None)

if button_2:
    head_data = st.table(data=df.head(5))

if button_3:
    json = df.head(5).to_dict()
    st.json(json)

if button_4:
    columns = tuple(df.columns)
    select_column = st.selectbox("Select the column you want to display", columns)
    st.dataframe(df[[select_column]])

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


tab1 = st.tabs(["More Visuals"])
st.markdown("---")
with tab1:
    # Widgets, dynamically change visualisations
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

    st.markdown("---")

    with st.container():
        st.subheader("Find the distribution for price and bedroom spread")

        fig, ax = plt.subplots()
        sns.boxplot(x="Price", y="Bedroom2", data=df, ax=ax)
        st.pyplot(fig)

    st.markdown("---")

    st.subheader("Allow users to pick and choose the chart type and data type")
    with st.container():
        # include all category features (multi select)
        # give options to bar line and area chart
        # stacked or not (radio)

        c1, c2, c3 = st.columns(3)
        with c1:
            group_cols = st.multiselect("select the features", cat_cols)
            features = group_cols
            n_features = len(features)

        with c2:
            chart_type = st.selectbox("Select Type", ("bar", "area", "line"))

        with c3:
            stack_options = st.radio("Stacked", ("Yes", "No"))
            if stack_options == "Yes":
                stacked = True
            else:
                stacked = False

        feature = ["price"]
        select_cols = features + feature
        avg_total = df[select_cols].groupby(features).mean()
        if n_features > 1:
            for i in range(n_features - 1):
                avg_total = avg_total.unstack()
        # visualisation
        fig, ax = plt.subplots()
        avg_total.plot(kind=chart_type, ax=ax, stacked=stacked)
        ax.legend(loc="center left", bbox_to_anchor=(1.0, 0.5))
        ax.set_ylabel("Average Total Price")
        st.pyplot(fig)

        with st.expander("Click to see values"):
            st.dataframe(avg_total)
