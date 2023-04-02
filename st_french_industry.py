import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

df = pd.read_csv('merged_ets.csv')

st.set_page_config(page_title="French Industry Project", layout="wide")

st.title('French Industry Project')
#**Suivant les données INSEE pour 33.513 communes documentées avec CODGEO, latitude, longitude et nombre d'établissements**"""

st.header("""Nombre d\'entreprises par communes""")

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

st.write("""'Suivant les données INSEE pour 33.513 communes documentées'  \n
'Données : CODGEO, latitude, longitude, E14TST'  \n
Les données E14TST relatent le nombre d\'entreprises par commune.  \n
Les données E14TST ont été légendées par quartiles (0.25, 0.50, 0.75) pour la colorimétrie.  \n
Jaune = 1er quartile  \n
Orange = 2ème quartile  \n
Rouge = 3ème quartile \n
""") 
