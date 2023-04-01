import pandas as pd
import streamlit as st

df = pd.read_csv('merged_NO_NA_geo_salary_ets.csv')

st.title("""
# French **Industry** #
# """)

    st.header('Test 1')
    latitude = [i for i in df.latitude]
    longitude = [i for i in df.longitude]
    df_geo = pd.DataFrame({ 'lat': latitude , 'lon': longitude})

    st.map(df_geo, use_container_width=True)