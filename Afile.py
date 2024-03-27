# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 11:06:57 2023

@author: shraddha
"""

import pickle
import streamlit as st

st.title('Claim Prediction :bar_chart:' )

load = open ('model.pkl','rb')
model = pickle.load(load)

def predict(temperature,exhaust_vacuum,amb_pressure,r_humidity):
    prediction = model.predict([[temperature,exhaust_vacuum,amb_pressure,r_humidity]])
    return prediction

def main():
    
    st.markdown("This a website which gives Energy Production based on of features. :chart:")
    temperature = st.number_input('Select temperature: ',min_value = 0, max_value = 100)
    exhaust_vacuum = st.number_input('Select exhaust vacuum: ')
    amb_pressure = st.number_input('Select amb pressure: ')
    r_humidity = st.number_input('Select r humidity: ')
    if st.button('Predict'):
        result = predict(temperature,exhaust_vacuum,amb_pressure,r_humidity)
        st.success('The Energy Production is : {} '.format(result))
        
if __name__ == '__main__':
    main()
    