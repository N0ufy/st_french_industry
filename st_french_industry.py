import pandas as pd
import streamlit as st

df = pd.read_csv('merged_NO_NA_geo_salary_ets.csv')

st.title("""
# French **Industry** #
# """)

col1, col2, col3 = st.columns(3, gap='large')

with col1:
    st.header('Test 1')
    latitude = [i for i in df.latitude]
    longitude = [i for i in df.longitude]
    df_geo = pd.DataFrame({ 'lat': latitude , 'lon': longitude})

    st.map(df_geo, use_container_width=True)
with col2:
    st.header('Test 2')

with col3:
    st.header('Test 3')