import streamlit as st
import pandas as pd

from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Experience": [1, 2, 3, 4, 5, 6],
    "Salary": [30000, 40000, 50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Experience"]]
y = df["Salary"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title("Salary Prediction App")

st.write("Predict salary based on years of experience")

experience = st.number_input(
    "Enter Years of Experience",
    min_value=0.0,
    step=0.5
)

if st.button("Predict Salary"):

    prediction = model.predict([[experience]])

    st.success(f"Predicted Salary: ₹{prediction[0]:,.2f}")