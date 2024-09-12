import streamlit as st

# Set the title of the app
st.title("Simple Interest Calculator")

# Get user input for principal, rate, and time
principal = st.number_input("Enter the principal amount:", min_value=0.0)
rate = st.number_input("Enter the annual interest rate (%):", min_value=0.0)
time = st.number_input("Enter the time in years:", min_value=0.0)

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
st.write(f"The simple interest is: {simple_interest}")
