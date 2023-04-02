import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

df = pd.read_csv('merged_ets.csv')
q1 = df[df['salaire_categorie'] == 'quantile 1'].reset_index(drop=True)
q2 = df[df['salaire_categorie'] == 'quantile 2'].reset_index(drop=True)
q3 = df[df['salaire_categorie'] == 'quantile 3'].reset_index(drop=True)
q4 = df[df['salaire_categorie'] == 'quantile 4'].reset_index(drop=True)

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
           data=q1,
           get_position='[longitude, latitude]',
           auto_highlight=True,
           elevation_scale=100,
           pickable=True,
           elevation_range= [0,250],
           extruded=True,
           coverage=1,
           radius=400,
           get_elevation='E14TST',
        
        ),

        pdk.Layer(
           'HexagonLayer',
           data=q2,
           get_position='[longitude, latitude]',
           auto_highlight=True,
           elevation_scale=100,
           pickable=True,
           elevation_range= [250,500],
           extruded=True,
           coverage=1,
           radius=600,
           get_elevation='E14TST',
        
        ),
        pdk.Layer(
           'HexagonLayer',
           data=q3,
           get_position='[longitude, latitude]',
           auto_highlight=True,
           elevation_scale=100,
           pickable=True,
           elevation_range= [500,750],
           extruded=True,
           coverage=1,
           radius=800,
           get_elevation='E14TST',
        
        ),
        pdk.Layer(
           'HexagonLayer',
           data=q4,
           get_position='[longitude, latitude]',
           auto_highlight=True,
           elevation_scale=100,
           pickable=True,
           elevation_range= [750,1000],
           extruded=True,
           coverage=1,
           radius=1000,
           get_elevation='E14TST',
        
        ),
    ],
), use_container_width=True)