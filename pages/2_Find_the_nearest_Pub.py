import streamlit as st 
import pandas as pd
import numpy as np
import folium
from folium import Marker
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static


st.set_page_config (layout="wide")

df = pd.read_csv("C:/Users/user/Downloads/open_pubs.csv", names=['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority'])

df.replace('\\N', np.nan, inplace=True)

df.dropna(inplace=True)

df['latitude'] = df['latitude'].astype('float') 

df['longitude'] = df['longitude'].astype('float')

df.drop_duplicates(inplace=True)

latd = st.number_input("Enter latitude:", value=52.896164)
longd = st.number_input("Enter longitude:", value=-0.655576)

def euclidean_dist(latd1, longd1, latd2, longd2):
    return np.sqrt((latd1-latd2)**2 + (longd1-longd2)**2)

df['distance'] = df.apply(lambda r:euclidean_dist(r['latitude'], r['longitude'], latd, longd), axis=1)

nearest_5pubs = df.sort_values(by='distance').head(5)

map = folium.Map(location=[latd, longd])

folium.Marker(location=[latd, longd], icon=folium.Icon(color='red'), popup='Your Location').add_to(map)

marker_cluster = MarkerCluster().add_to(map)

for i, r in nearest_5pubs.iterrows():
    Marker([r['latitude'], r['longitude']], popup=r['name']).add_to(marker_cluster)

folium_static(map)