import streamlit as st
import pandas as pd
import pydeck as pdk


df = pd.read_excel("data/settlement_data.xlsx", index_col=0)

df = pd.DataFrame(df)
# st.header(
#     "A catalogue of sites with urban characteristics in the Roman Empire between 100 B.C. and A.D. 300"
# )

# st.map(df)

df = df.to_json(orient="records")


view_state = pdk.ViewState(latitude=41.9028, longitude=12.4964, zoom=10)
layer = pdk.Layer(
    "ScatterplotLayer",  # this is the type of layer we want to plot on the map 
    df,  # this is the data we want to plot on the map 
    get_position=["lon", "lat"], # this is where we specify the longitude and latitude columns in our dataframe 
    auto_highlight=True, # this enables us to highlight points when we hover over them 
    pickable=True, # this enables us to click on points and see more information about them 
    opacity=0.8, # this sets the opacity of our points 
    stroked=True, # this enables us to draw outlines around our points 
    filled=True, # this enables us to fill in our points with color 
    radius_scale=6, # this sets the size of our points relative to one another (the default is 6) 
    radius_min_pixels=5, # this sets the minimum size of our points (the default is 5) 
    radius_max_pixels=100, # this sets the maximum size of our points (the default is 100)  
)
st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        layers=layer,
        initial_view_state=view_state,
    )
)


import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px



@st.cache(persist=True)
def load_data():
    data = pd.read_csv("data/melb_data.csv")
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[["Lattitude", "Longtitude"]] = data[["Lattitude", "Longtitude"]].astype(float)
    return data

data = load_data()


st.map(data)

st.header("How many urban sites are there by province?")
st.dataframe(data["Regionname"].value_counts())