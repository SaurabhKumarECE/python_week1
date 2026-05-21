import streamlit as st
import pandas as pd

from sklearn.linear_model import LinearRegression

# Page title
st.title("Interactive Salary Prediction Dashboard")

# Sidebar
st.sidebar.header("User Input")

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

# Slider input
experience = st.sidebar.slider(
    "Years of Experience",
    min_value=0,
    max_value=20,
    value=1
)

# Predict button
if st.button("Predict Salary"):

    prediction = model.predict([[experience]])

    st.success(
        f"Estimated Salary: ₹{prediction[0]:,.2f}"
    )

# Show dataset
st.subheader("Dataset")

st.dataframe(df)

# Show information
st.info("This dashboard predicts salary based on years of experience.")