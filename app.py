# ==========================================
# TEMPERATURE CONVERTER WEB APP
# Built with Python and Streamlit
# ==========================================

# 1. Import Streamlit
import streamlit as st


# 2. Configure the webpage
st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="centered"
)


# 3. Display the title and introduction
st.title("🌡️ Temperature Converter")

st.write(
    "Welcome! Use this app to convert temperatures "
    "between Celsius and Fahrenheit."
)

st.divider()


# 4. Create a temperature input box
temperature = st.number_input(
    "Enter a temperature:",
    value=0.0,
    step=1.0,
    help="Enter the temperature you want to convert."
)


# 5. Create a dropdown menu for conversion type
conversion_type = st.selectbox(
    "Select conversion type:",
    [
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius"
    ]
)


# 6. Create the conversion button
if st.button("Convert Temperature", type="primary"):

    # Convert Celsius to Fahrenheit
    if conversion_type == "Celsius to Fahrenheit":

        converted_temperature = (temperature * 9 / 5) + 32

        formula = "°F = (°C × 9/5) + 32"

        unit = "°F"

    # Convert Fahrenheit to Celsius
    else:

        converted_temperature = (temperature - 32) * 5 / 9

        formula = "°C = (°F - 32) × 5/9"

        unit = "°C"


    # 7. Display a success message
    st.success("Your temperature has been converted!")


    # 8. Display the converted temperature
    st.subheader("Converted Temperature")

    st.metric(
        label="Your Result",
        value=f"{converted_temperature:.2f} {unit}"
    )


    # 9. Display the formula used
    st.subheader("Conversion Formula")

    st.code(formula, language="text")


    # 10. Display the original and converted values
    st.write(f"Original Temperature: {temperature:.2f}°")

    st.write(
        f"Converted Temperature: "
        f"{converted_temperature:.2f} {unit}"
    )


# 11. Add a divider and footer
st.divider()

st.caption(
    "Temperature Converter | Created using Python and Streamlit"
)
