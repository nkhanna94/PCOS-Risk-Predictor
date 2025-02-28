import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("random_forest_model.pkl")

# Set the app title and icon
st.set_page_config(page_title="🩺 PCOS Detection", page_icon="🩺")

# App Header
st.title("PCOS Risk Predictor 🏥")
st.markdown("### Enter patient details to assess the likelihood of PCOS.")

# Input fields
age = st.number_input("🔢 Age", min_value=10, max_value=60, step=1)
bmi = st.number_input("⚖️ BMI", min_value=10.0, max_value=50.0, step=0.1)
menstrual_irregularity = st.radio("🩸 Menstrual Irregularity", ["No", "Yes"])
testosterone_level = st.number_input("🧪 Testosterone Level (ng/dL)", min_value=0.0, max_value=200.0, step=0.1)
antral_follicle_count = st.number_input("🟢 Antral Follicle Count", min_value=0, max_value=50, step=1)

# Convert categorical input to numerical
menstrual_irregularity = 1 if menstrual_irregularity == "Yes" else 0

# Prediction button
if st.button("🔍 Predict PCOS Risk"):
    input_data = np.array([[age, bmi, menstrual_irregularity, testosterone_level, antral_follicle_count]])
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠️ **PCOS Detected**")
    else:
        st.success("✅ **No PCOS Detected**")
