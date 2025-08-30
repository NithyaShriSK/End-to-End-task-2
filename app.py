import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.sav', 'rb'))

st.title("Life Expectancy Prediction")
st.write("Enter the details below to predict the life expectancy.")

Year = st.number_input("Year", min_value=2000, max_value=2025, value=2020)
Adult_Mortality = st.number_input("Adult Mortality", min_value=0.0, max_value=1000.0, value=150.0, format="%.2f")
infant_deaths = st.number_input("Infant deaths", min_value=0, max_value=1000, value=10)
Alcohol = st.number_input("Alcohol consumption", min_value=0.0, max_value=20.0, value=5.0, format="%.2f")
Hepatitis_B = st.number_input("Hepatitis B immunization", min_value=0.0, max_value=100.0, value=80.0, format="%.2f")
Measles = st.number_input("Measles cases", min_value=0, max_value=10000, value=50)
BMI = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0, format="%.2f")
under_five_deaths = st.number_input("Under-five deaths", min_value=0, max_value=1000, value=10)
Polio = st.number_input("Polio immunization", min_value=0.0, max_value=100.0, value=80.0, format="%.2f")
Total_expenditure = st.number_input("Total expenditure", min_value=0.0, max_value=20.0, value=5.0, format="%.2f")
Diphtheria = st.number_input("Diphtheria immunization", min_value=0.0, max_value=100.0, value=80.0, format="%.2f")
HIV_AIDS = st.number_input("HIV/AIDS deaths", min_value=0.0, max_value=100.0, value=0.5, format="%.2f")
GDP = st.number_input("GDP", min_value=0.0, max_value=100000.0, value=5000.0, format="%.2f")
Population = st.number_input("Population", min_value=0.0, max_value=1500000000.0, value=5000000.0, format="%.2f")
thinness_5_9_years = st.number_input("Thinness 5-9 years", min_value=0.0, max_value=50.0, value=10.0, format="%.2f")
Income_composition_of_resources = st.number_input("Income composition of resources", min_value=0.0, max_value=1.0, value=0.5, format="%.2f")
Schooling = st.number_input("Schooling years", min_value=0.0, max_value=20.0, value=12.0, format="%.2f")

Status_input = st.selectbox(
    "Status",
    options=["Developing","Developed"],
    index=0
)
Status = 1 if Status_input == "Developing" else 0

features = np.array([[
    Year,Status,Adult_Mortality,infant_deaths,Alcohol,Hepatitis_B,Measles,BMI,under_five_deaths,Polio,
    Total_expenditure,Diphtheria,HIV_AIDS,GDP,Population,thinness_5_9_years,Income_composition_of_resources,Schooling
]])

# Prediction
if st.button("Predict Life Expectancy"):
    prediction = model.predict(features)
    st.success(f"Predicted Life Expectancy: {prediction[0]:.2f} years")
