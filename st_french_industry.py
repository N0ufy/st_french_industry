import pandas as pd
import streamlit as st

df = pd.read_csv('merged_NO_NA_geo_salary_ets.csv')

st.title("""
# French **Industry** #
# """)

city = [i for i in df.LIBGEO]
latitude = [i for i in df.latitude]
longitude = [i for i in df.longitude]
df_geo = pd.DataFrame({ 'city': city, 'lat': latitude , 'lon': longitude})

st.map(df_geo, height= 1200, use_container_width=True)