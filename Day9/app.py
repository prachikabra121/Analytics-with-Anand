import streamlit as st

# Set the title of the app
st.title("BMI Calculator")

# Add a description to the app
st.write("""
This app calculates your Body Mass Index (BMI) and provides feedback.
BMI is a measure of body fat based on height and weight.
""")

# Input fields for height and weight
height = st.number_input("Enter your height in centimeters:", min_value=50, max_value=300, value=170)
weight = st.number_input("Enter your weight in kilograms:", min_value=20, max_value=300, value=70)

# Calculate the BMI
if height > 0 and weight > 0:
    # Convert height from cm to meters
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    
    # Display the calculated BMI
    st.write(f"Your BMI is: {bmi:.2f}")
    
    # Provide feedback based on the BMI value
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")
else:
    st.write("Please enter valid height and weight values.")
