import streamlit as st 
import pandas as pd
import numpy as np
import folium
from folium import Marker
from streamlit_folium import folium_static

st.set_page_config (layout="wide")

df = pd.read_csv("C:/Users/user/Downloads/open_pubs.csv", names=['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority'])

df.replace('\\N', np.nan, inplace=True)

df.dropna(inplace=True)

df['latitude'] = df['latitude'].astype('float') 

df['longitude'] = df['longitude'].astype('float')

df.drop_duplicates(inplace=True)

st.title("pubs")

search_method = st.radio("Search by:", ('postcode', 'local_authority'))

if search_method == 'postcode':
    search_list = sorted(df['postcode'].unique())
else:
    search_list = sorted(df['local_authority'].unique())
    
search_using = st.selectbox(f"Select {search_method}", search_list)

if search_method == 'postcode':
    data_1 = df[df['postcode'] == search_using]
else:
    data_1 = df[df['local_authority'] == search_using]
    
map = folium.Map(location=[data_1['latitude'].mean(), data_1['longitude'].mean()])

for i, r in data_1.iterrows():
    folium.Marker(location=[r['latitude'], r['longitude']], popup=r['name']).add_to(map)
    
folium_static(map)