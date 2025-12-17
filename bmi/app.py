import streamlit as st

st.set_page_config(page_title="BMI Calculator", layout="centered")
st.title("Body Mass Index(BMI) Calculator")

st.write("Enter your height and weight to calculate BMI")

height = st.number_input("Height (in cm):", min_value=50.0, max_value=250.0, step=1.0)
weight = st.number_input("Weight (in kg)", min_value=10.0, max_value=250.0, step=1.0)

if st.button("Calculate BMI"):
    if height >0 and weight >0:
        bmi = weight / ((height / 100) ** 2)
        st.write(f"**Your BMI is:** {bmi:.2f}")
        if bmi < 18.5:
            st.warning("Underweight")
        elif 18.5 <= bmi <24.9:
            st.success("Normal weight")
        else:
            st.error("Obese") 
else:
    st.warning("Please enter valid height and weight")                  