import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

df = pd.read_csv('merged_ets.csv')
df['elevation'] = df['E14TST']
elevation_range = [df['E14TST'].min(), df['E14TST'].max()]


st.set_page_config(page_title="French Industry Project", layout="wide")

st.title("""Nombre d\'entreprises par CODGEO INSEE""")

st.pydeck_chart(pdk.Deck(   
    map_style='dark',
    initial_view_state=pdk.ViewState(
        latitude=46.6167,
        longitude=1.85,
        zoom=5,
        pitch=20, #pour la vue en angle de la map
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=df,
           get_position='[longitude, latitude]',
           auto_highlight=True,
           elevation_scale=100,
           pickable=True,
           elevation_range= elevation_range,
           extruded=True,
           coverage=1,
           radius=800,
           get_elevation='elevation',
        
        ),


    ],
), use_container_width=True)