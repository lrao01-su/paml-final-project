import streamlit as st                  # pip install streamlit
from helper_functions import load_dataset, display_missingValue
import streamlit as st
import pandas as pd
import numpy as np
#############################################

st.markdown("# Practical Applications of Machine Learning (PAML)")

#############################################

st.markdown("### Farelytics ML: Using Machine Learning to Analyze and Compare Uber and Lyft Pricing Models")

#############################################

st.markdown('# Explore & Preprocess Dataset')

#############################################
col1, col2 = st.columns(2)
# with(col1):
with(col1):
    cab_data = st.file_uploader("Upload Your df_cab Dataset", type=['csv','txt'])
# with(col2): #upload from cloud
with(col2):
    weather_data = st.file_uploader("Upload Your df_weather Dataset", type=['csv','txt'])
if cab_data and weather_data:
    ###################### EXPLORE DATASET #######################
    st.markdown('### Explore Dataset Features')

<<<<<<< HEAD
    # Load dataset
    df_cab = load_dataset(cab_data)
    df_weather = load_dataset(weather_data)
    # Restore dataset if already in memory
    st.session_state['df_cab']=df_cab
    st.session_state['df_weather']=df_weather
    
    # Display dataframe as table using streamlit dataframe function
    st.write("df_cab")
    st.dataframe(df_cab)
    st.write("df_weather")
    st.dataframe(df_weather)
=======



if df is not None:
    # Display original dataframe
    st.markdown('View initial data with missing values or invalid inputs')
    st.markdown('You have uploaded the dataset.')
    #write multiple dataframes
    for i in range(len(df)):
        st.dataframe(df[i])
>>>>>>> 52f0cf8b72dd871cb844c9ff53fea1d35a73d1c1

    # Inspect the dataset
    st.markdown('### Inspect and visualize some interesting features')

    #display missing data for df_cab and df_weather/ Olga
    st.markdown('### Missing Data') 
    missing_data = display_missingValue(df_rides, df_weather)

    st.dataframe(missing_data)
    # Deal with missing values for cab /Olga
    st.markdown('### Handle missing values for cab')

    # Deal with missing values for weather /Mary
    st.markdown('### Handle missing values for weather') 

    #merge df_cab and df_weather /Mary
    st.markdown('### Merge cab and weather data')

    # Handle Text and Categorical Attributes
    st.markdown('### Handling Non-numerical Features')

    st.markdown('### You have preprocessed the dataset.')
    #st.dataframe(df)

    st.write('Continue to Train Model')
