"""
import pandas as pd


df = pd.read_csv('merged_NO_NA_geo_salary_ets.csv')
df_quantile1 = df[df['salaire_categorie'] == 'quantile 1'].reset_index(drop=True)
df_quantile2 = df[df['salaire_categorie'] == 'quantile 2'].reset_index(drop=True)
df_quantile3 = df[df['salaire_categorie'] == 'quantile 3'].reset_index(drop=True)
df_quantile4 = df[df['salaire_categorie'] == 'quantile 4'].reset_index(drop=True)

import streamlit as st
st.title("""
#French **Industry**#
# """)

#col1, col2, col3, col4 = st.columns(4)

"""
st.header('Bas salaires - 1er quantile')
st.map(df_quantile1 , use_container_width=True)
st.header('Classe moyenne inf - 2ème quantile')
st.map(df_quantile2 , use_container_width=True)
"""
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

df = pd.read_csv('merged_NO_NA_geo_salary_ets.csv')
df_quantile1 = df[df['salaire_categorie'] == 'quantile 1'].reset_index(drop=True)
df_quantile2 = df[df['salaire_categorie'] == 'quantile 2'].reset_index(drop=True)
df_quantile3 = df[df['salaire_categorie'] == 'quantile 3'].reset_index(drop=True)
df_quantile4 = df[df['salaire_categorie'] == 'quantile 4'].reset_index(drop=True)

chart_data = pd.DataFrame({'lat': lat, 'lon':lon})

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=48.858370,
        longitude=-2.294481,
        zoom=5,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=df_quantile4,
           get_position='[longitude, latitude]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),

         pdk.Layer(
           'HexagonLayer',
           data=df_quantile3,
           get_position='[longitude, latitude]',
           radius=200,
           elevation_scale=4,
           elevation_range=[250, 500],
           pickable=True,
           extruded=True,
        ),
         pdk.Layer(
           'HexagonLayer',
           data=df_quantile2,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[500, 700],
           pickable=True,
           extruded=True,
        ),
         pdk.Layer(
           'HexagonLayer',
           data=df_quantile1,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[500, 700],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))