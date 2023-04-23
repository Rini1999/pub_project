import streamlit as st 
import pandas as pd
import numpy as np

st.set_page_config (layout="wide")

st.title("Open Pub Application")

st.sidebar.title("Pages")

df = pd.read_csv("C:/Users/user/Downloads/open_pubs.csv", names=['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority'])

print(df.head())

df.info()

df.replace('\\N', np.nan, inplace=True)

df.dropna(inplace=True)

print(df.isnull().sum())

df['latitude'] = df['latitude'].astype('float') 

df['longitude'] = df['longitude'].astype('float')

df.drop_duplicates(inplace=True)

st.write(f"This dataset - Geocoded Open Pubs in UK, with Food Hygiene Ratings - contains data on open pubs located in England, such as their FSA ID, name, address and postcode, easting and northing coordinates for geographical mapping purposes, as well as latitude and longitude values. This information can be used to plot pubs onto a map or to create applications that allow you to locate the nearest pub.")
st.write(f"The raw data used for this dataset comes from the Food Standard Agency's Food Hygiene Ratings database and is licensed under their terms & conditions. The local authority field is derived from the ONS Postcode Directory which is licenced under OGL (Open Government Licence). This open-data has been published by GetTheData (https://www.getthedata.com) thank you!")

st.balloons()