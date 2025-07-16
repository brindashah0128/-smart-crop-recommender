import streamlit as st
import numpy as np
import pickle

# Load model
with open('crop_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🌱 Crop Recommendation System")

# Inputs
N = st.number_input('Nitrogen (N)', min_value=0, max_value=200, value=50)
P = st.number_input('Phosphorus (P)', min_value=0, max_value=200, value=50)
K = st.number_input('Potassium (K)', min_value=0, max_value=200, value=50)
temperature = st.slider('Temperature (°C)', 0.0, 50.0, 25.0)
humidity = st.slider('Humidity (%)', 0.0, 100.0, 50.0)
ph = st.slider('pH', 0.0, 14.0, 6.5)
rainfall = st.slider('Rainfall (mm)', 0.0, 300.0, 100.0)

# Predict
if st.button('Recommend'):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f"✅ Recommended Crop: **{prediction[0]}**")
