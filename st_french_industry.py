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

#df_geo = pd.DataFrame({'lat': latitude , 'lon': longitude})

st.map(df_quantile1 , use_container_width=True)