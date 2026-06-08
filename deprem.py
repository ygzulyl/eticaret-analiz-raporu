import plotly.express as px
import streamlit as st
import requests

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson"
yanit = requests.get(url)

veri = yanit.json()

tum_depremler = veri["features"]

deprem_boyutu = []
deprem_turu = []
longitude = []
latitute = []

for deprem in tum_depremler:
    deprem_boyutu.append(deprem["properties"]["mag"])
    deprem_turu.append(deprem["properties"]["magType"])
    longitude.append(deprem["geometry"]["coordinates"][0])
    latitute.append(deprem["geometry"]["coordinates"][1])

fig = px.scatter_geo(data_frame=tum_depremler, color=deprem_turu, size=deprem_boyutu, lat=latitute, lon=longitude)
fig.show()
st.plotly_chart(fig, witdh="stretch")