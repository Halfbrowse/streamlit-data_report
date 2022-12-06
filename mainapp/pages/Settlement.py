import streamlit as st
import pandas as pd
import pydeck as pdk


df = pd.read_excel("data/settlement_data.xlsx", index_col=0)

df = pd.DataFrame(df)
st.header(
    "A catalogue of sites with urban characteristics in the Roman Empire between 100 B.C. and A.D. 300"
)

st.map(df)

df = df.to_json(orient="records")


view_state = pdk.ViewState(latitude=41.9028, longitude=12.4964, zoom=10)
layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position=["lon", "lat"],
    get_radius=50,
    pickable=True,
    filled=True,
)

st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        layers=[layer],
        initial_view_state=view_state,
    )
)
