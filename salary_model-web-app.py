import streamlit as st
import joblib

# Load the model
model = joblib.load('salary_model.joblib')

# Prepare the input form
st.title('Salary Prediction App')
experience = st.number_input('Enter your experience (in years)', min_value=0.0, max_value=50.0, value=1.0)

# Make a prediction
if st.button('Predict'):
    salary = model.predict([[experience]])
    st.write('The estimated salary is:', round(salary[0], 2))
