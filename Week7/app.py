import streamlit as st
import pandas as pd
import joblib

# Load your trained model
model = joblib.load("stroke_prediction_model.joblib")

# Set up the page
st.set_page_config(page_title="Stroke Prediction", layout="centered")
st.title(" Stroke Risk Prediction App")
st.write("Enter the patient details below to predict stroke risk.")

# Input form
with st.form("prediction_form"):
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.slider("Age", 0, 100, 35)
    hypertension = st.selectbox("Hypertension", [0, 1])
    heart_disease = st.selectbox("Heart Disease", [0, 1])
    ever_married = st.selectbox("Ever Married", ["Yes", "No"])
    work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
    residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
    avg_glucose_level = st.number_input("Average Glucose Level", value=100.0)
    bmi = st.number_input("BMI", value=25.0)
    smoking_status = st.selectbox("Smoking Status", ["formerly smoked", "never smoked", "smokes", "Unknown"])
    submit = st.form_submit_button("Predict")

# Prediction output
if submit:
    input_data = pd.DataFrame([{
        'gender': gender,
        'age': age,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'ever_married': ever_married,
        'work_type': work_type,
        'Residence_type': residence_type,
        'avg_glucose_level': avg_glucose_level,
        'bmi': bmi,
        'smoking_status': smoking_status
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")
    if prediction == 1:
        st.error(f" High Risk of Stroke\n\n**Probability: {prob:.2f}**")
    else:
        st.success(f" Low Risk of Stroke\n\n**Probability: {prob:.2f}**")
