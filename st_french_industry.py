import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

df = pd.read_csv('merged_ets.csv')
df['elevation'] = df['E14TST']

st.title("""#Nombre d\'ntreprises par localisation#""")

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=46.6167,
        longitude=1.85,
        zoom=4,
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
           elevation_range=[0, 3000],
           extruded=True,
           coverage=1,
           radius=1000,
           get_elevation='elevation',
        
        ),


    ],
), use_container_width=True)