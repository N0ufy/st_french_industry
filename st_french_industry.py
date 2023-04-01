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

st.header('Bas salaires - 1er quantile')
st.map(df_quantile1 , use_container_width=True)
st.header('Classe moyenne inf - 2ème quantile')
st.map(df_quantile2 , use_container_width=True)