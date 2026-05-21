from flask import Flask
from flask import request
from flask import jsonify

import pandas as pd

from sklearn.linear_model import LinearRegression

# Create Flask app
app = Flask(__name__)

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

# Home route
@app.route("/")
def home():

    return "Flask ML API is Running!"

# Prediction route
@app.route("/predict", methods=["GET"])
def predict():

    experience = float(request.args.get("experience"))

    prediction = model.predict([[experience]])

    return jsonify({
        "experience": experience,
        "predicted_salary": prediction[0]
    })

# Run app
if __name__ == "__main__":

    app.run(debug=True)