import streamlit as st
import pandas as pd
import joblib

model = joblib.load('best_medical_insurance_model.pkl')

st.set_page_config(
    page_title="Medical Insurance Cost Prediction",
    page_icon="🏥",
    layout="centered"
)

st.title("Medical Insurance Cost Prediction")

st.write(
    "Enter patient details to predict medical insurance charges."
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

sex = st.selectbox(
    "Sex",
    ['male', 'female']
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.5
)

children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
)

smoker = st.selectbox(
    "Smoker",
    ['yes', 'no']
)

region = st.selectbox(
    "Region",
    ['southwest', 'southeast', 'northwest', 'northeast']
)

if st.button("Predict Insurance Cost"):

    patient = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })

    prediction = model.predict(patient)[0]

    st.success(
        f"Predicted Insurance Charges: ${prediction:,.2f}"
    )