from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# -------------------------------
# Load model and scaler
# -------------------------------
model_path = os.path.join("predictor_collection", "model.pkl")
scaler_path = os.path.join("predictor_collection", "scaler.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)


# -------------------------------
# Routes
# -------------------------------
@app.route("/")
def home():
    """Render input form"""
    return render_template("form.html")


@app.route("/predict", methods=["POST"])
def predict():
    """Handle form submission and make prediction"""
    try:
        # Collect input values from form
        age = int(request.form["age"])
        sex = int(request.form["sex"])
        cp = int(request.form["cp"])
        trestbps = int(request.form["trestbps"])
        chol = int(request.form["chol"])
        fbs = int(request.form["fbs"])
        restecg = int(request.form["restecg"])
        thalach = int(request.form["thalach"])
        exang = int(request.form["exang"])
        oldpeak = float(request.form["oldpeak"])
        slope = int(request.form["slope"])
        ca = int(request.form["ca"])
        thal = int(request.form["thal"])

        # Prepare features
        input_data = np.array([
            age, sex, cp, trestbps, chol, fbs,
            restecg, thalach, exang, oldpeak,
            slope, ca, thal
        ]).reshape(1, -1)

        # Scale input
        input_scaled = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_scaled)[0]
        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

        return render_template("result.html", result=result)

    except Exception as e:
        return render_template("result.html", result=f"Error: {str(e)}")


# -------------------------------
# Run locally
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
