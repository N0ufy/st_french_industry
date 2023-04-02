import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

df = pd.read_csv('merged_ets.csv')

st.set_page_config(page_title="French Industry Project", layout="wide")

st.title("""Nombre d\'entreprises par communes
**Suivant les données INSEE pour 33.513 communes documentées avec CODGEO, latitude, longitude et nombre d'établissements**""")

st.pydeck_chart(pdk.Deck(   
    map_style='dark',
    initial_view_state=pdk.ViewState(
        latitude=46.6167,
        longitude=1.85,
        zoom=5,
        pitch=10, #pour la vue en angle de la map
    ),
    layers=[
        pdk.Layer(
           'ColumnLayer',
           data=df,
           get_position='[longitude, latitude]',
           auto_highlight=True,
           #elevation_scale=5,
           pickable=True,
           #elevation_range= [0,1000],  
           extruded=True,
           coverage=1,
           radius=400,
           get_elevation='E14TST',
           get_fill_color=['255', 'Gcolor', '45' , '140']
        )],
), use_container_width=True)

