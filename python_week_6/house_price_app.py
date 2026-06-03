import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load(
    "best_house_price_model.pkl"
)

# Title
st.title("🏠 House Price Prediction System")

st.write(
    "Enter house details to estimate price."
)

# Inputs

area = st.number_input(
    "Area (sq ft)",
    min_value=500,
    max_value=10000,
    value=1500
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

floors = st.number_input(
    "Floors",
    min_value=1,
    max_value=5,
    value=1
)

parking = st.number_input(
    "Parking Spaces",
    min_value=0,
    max_value=10,
    value=1
)

# Predict

if st.button("Predict Price"):

    input_data = pd.DataFrame(
        {
            "Area": [area],
            "Bedrooms": [bedrooms],
            "Bathrooms": [bathrooms],
            "Floors": [floors],
            "Parking": [parking]
        }
    )

    prediction = model.predict(
        input_data
    )

    st.success(
        f"Estimated House Price: ₹{prediction[0]:,.0f}"
    )