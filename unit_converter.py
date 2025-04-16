import streamlit as st   # Streamlit is a Python library used to create interactive web apps

# Function to convert between units
def convert_units(value, unit_from, unit_to):
    # Dictionary containing conversion rates between supported units
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,   # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,    # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000      # 1 kilogram = 1000 grams
    }
    
    # Generate a key like 'meters_kilometers' to look up the conversion rate
    key = f"{unit_from}_{unit_to}"
    
    # Check if the conversion key exists in the dictionary
    if key in conversions:
        conversion = conversions[key]
        return value * conversion  # Return the converted value
    else:
        return "Conversion not supported"  # Error message if conversion not found

# Streamlit UI starts here

st.title("Unit Converter")  # Title of the app

# Input field to enter the numeric value to be converted
value = st.number_input("Enter the value:", min_value = 1.0, step = 1.0)

# Dropdown to select the unit to convert from
unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])

# Dropdown to select the unit to convert to
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# Button to perform conversion when clicked
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)  # Call the conversion function
    st.write(f"Converted value: {result}")  # Display the result




