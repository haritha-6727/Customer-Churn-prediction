

import streamlit as st
from predict_churn import predict_churn


st.title("Customer Churn Prediction")

st.write(
    "This app predicts the likelihood of a customer churning (leaving) based on various features."
)


gender = st.selectbox('Gender', ['Male', 'Female'])
senior_citizen = st.selectbox('SeniorCitizen', ['0', '1'])
partner = st.selectbox('Partner', ['Yes', 'No'])
dependents = st.selectbox('Dependents', ['Yes', 'No'])
tenure = st.number_input('Tenure (months)', min_value=0, max_value=72, step=1)
phone_service = st.selectbox('PhoneService', ['Yes', 'No'])
multiple_lines = st.selectbox('MultipleLines', ['Yes', 'No'])
internet_service = st.selectbox('InternetService', ['DSL', 'Fiber optic', 'No'])
online_security = st.selectbox('OnlineSecurity', ['Yes', 'No'])
online_backup = st.selectbox('OnlineBackup', ['Yes', 'No'])
device_protection = st.selectbox('DeviceProtection', ['Yes', 'No'])
tech_support = st.selectbox('TechSupport', ['Yes', 'No'])
streaming_tv = st.selectbox('StreamingTV', ['Yes', 'No'])
streaming_movies = st.selectbox('StreamingMovies', ['Yes', 'No'])
contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
paperless_billing = st.selectbox('PaperlessBilling', ['Yes', 'No'])
payment_method = st.selectbox('PaymentMethod', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
monthly_charges = st.number_input('MonthlyCharges', min_value=0.0, step=0.1)
total_charges = st.number_input('TotalCharges', min_value=0.0, step=0.1)


input_data = {
    'gender': gender,
    'SeniorCitizen': senior_citizen,
    'Partner': partner,
    'Dependents': dependents,
    'tenure': tenure,
    'PhoneService': phone_service,
    'MultipleLines': multiple_lines,
    'InternetService': internet_service,
    'OnlineSecurity': online_security,
    'OnlineBackup': online_backup,
    'DeviceProtection': device_protection,
    'TechSupport': tech_support,
    'StreamingTV': streaming_tv,
    'StreamingMovies': streaming_movies,
    'Contract': contract,
    'PaperlessBilling': paperless_billing,
    'PaymentMethod': payment_method,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges
}


if st.button('Predict Churn'):
    prob = predict_churn(input_data)
    st.write(f"Churn Probability: {prob * 100:.2f}%")


