# -*- coding: utf-8 -*-
"""prediction_streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/132HOnlJ4lAaOa9mUVXcOqMgP27z5S3FU
"""

import pandas as pd
import pickle

# Function to load the model (assuming it's saved as XGBoost.pkl)
def load_model():
    with open("XGBoost.pkl", "rb") as file:
        loaded_model = pickle.load(file)
    return loaded_model

# Function to predict churn
def predict_churn(input_data, model):
    input_features = input_data[["CreditScore", "Age", "Tenure", "Balance", "NumOfProducts", "HasCrCard", "IsActiveMember", "EstimatedSalary"]]
    prediction = model.predict(input_features)
    return prediction

# Load the model
model = load_model()

# Define header, description, and empty DataFrames for user input
header = "Customer Churn Prediction"
description = "Enter customer details to predict churn probability."
data_1 = {"CreditScore": [], "Age": [], "Tenure": [], "Balance": [],
         "NumOfProducts": [], "HasCrCard": [], "IsActiveMember": [], "EstimatedSalary": []}
data_2 = {"CreditScore": [], "Age": [], "Tenure": [], "Balance": [],
         "NumOfProducts": [], "HasCrCard": [], "IsActiveMember": [], "EstimatedSalary": []}
df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame(data_2)

# Streamlit App
import streamlit as st

st.title(header)
st.write(description)

# Create two sections for test cases
with st.expander("Test Case 1"):
    st.subheader("Customer 1")

    counter = 0
    for col in df_1.columns:
        counter += 1
        df_1.loc[0, col] = st.number_input(col, key=f"customer1_{col}_{counter}")

    predict_button_1 = st.button("Predict Churn", key="predict_churn_1")  # Unique key for button

    if predict_button_1:
        prediction_1 = predict_churn(df_1.copy(), model)
        class_label = ["No Churn", "Churn"][int(prediction_1[0])]
        if class_label == "No Churn":
            st.success(f"**Prediction:** Customer is likely to stay. (No Churn)")
        else:
            st.error(f"**Prediction:** Customer is likely to churn.")

with st.expander("Test Case 2"):
    st.subheader("Customer 2")

    counter = 0
    for col in df_2.columns:
        counter += 1
        df_2.loc[0, col] = st.number_input(col, key=f"customer2_{col}_{counter}")

    predict_button_2 = st.button("Predict Churn", key="predict_churn_2")  # Unique key for button

    if predict_button_2:
        prediction_2 = predict_churn(df_2.copy(), model)
        class_label = ["No Churn", "Churn"][int(prediction_2[0])]
        if class_label == "No Churn":
            st.success(f"**Prediction:** Customer is likely to stay. (No Churn)")
        else:
            st.error(f"**Prediction:** Customer is likely to churn.")
