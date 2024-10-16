import streamlit as st

# Function to convert temperatures
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
        else:
            return value
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return "Invalid unit"

# Streamlit interface
st.title("🌡️ Temperature Converter")

st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin with ease!")

# User input
input_temp = st.number_input("Enter the temperature value:", format="%f")
from_unit = st.selectbox("Select the unit to convert from:", ['Celsius', 'Fahrenheit', 'Kelvin'])
to_unit = st.selectbox("Select the unit to convert to:", ['Celsius', 'Fahrenheit', 'Kelvin'])

# Conversion result
if st.button('Convert'):
    converted_temp = convert_temperature(input_temp, from_unit, to_unit)
    st.success(f"The converted temperature is {converted_temp:.2f} {to_unit}!")
