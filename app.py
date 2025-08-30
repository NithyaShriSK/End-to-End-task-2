import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.sav', 'rb'))

st.title("Life Expectancy Prediction")
st.write("Enter the details below to predict the life expectancy.")

Year = st.number_input("Year", min_value=0, max_value=90, value=2)
Adult_Mortality = st.number_input("Adult Mortality", min_value=0, max_value=90, value=2,format="%.2f")
infant_deaths = st.number_input("infant deaths", min_value=0, max_value=100, value=50)
Alcohol = st.number_input("Alcohol", min_value=0, max_value=100, value=50,format="%.2f")
Hepatitis_B = st.number_input("Hepatitis B", min_value=0, max_value=100, value=50,format="%.2f")
Measles = st.number_input("Measles", min_value=0, max_value=100, value=50)
BMI = st.number_input("BMI", min_value=0, max_value=100, value=50,format="%.2f")
under_five_deaths = st.number_input("under-five deaths", min_value=0, max_value=100, value=50)
Polio = st.number_input("Polio", min_value=0, max_value=100, value=50,format="%.2f")
Total_expenditure = st.number_input("Total expenditure", min_value=0, max_value=100, value=50,format="%.2f")
Diphtheria = st.number_input("Diphtheria", min_value=0, max_value=100, value=50,format="%.2f")
HIV_AIDS = st.number_input("HIV/AIDS", min_value=0, max_value=100, value=50,format="%.2f")
GDP = st.number_input("GDP", min_value=0, max_value=100, value=50,format="%.2f")
Population = st.number_input("Population", min_value=0, max_value=100, value=50,format="%.2f")
thinness_5_9_years= st.number_input("thinness 5-9 years", min_value=0, max_value=100, value=50,format="%.2f")
Income_composition_of_resources = st.number_input("Income composition of resources", min_value=0, max_value=100, value=50,format="%.2f")
Schooling = st.number_input("Schooling", min_value=0, max_value=100, value=50,format="%.2f")

Status = st.selectbox(
    "Status",
    options=["Developing","Developed"],
    index=0
)
# Encoding categorical values
Status = {"Developing": 1, "Developed": 0}

features = np.array([[
    Year,Status,Adult_Mortality,infant_deaths,Alcohol,Hepatitis_B,Measles,BMI,under_five_deaths,Polio,
    Total_expenditure,Diphtheria,HIV_AIDS,GDP,Population,thinness_5_9_years,Income_composition_of_resources,Schooling
]])

# Prediction
if st.button("Result"):
    prediction = model.predict(features)
    st.success(f"Predicted Life Expectancy: {prediction[0]:.2f} years")