
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load trained model and feature columns
model = joblib.load("model/logistic_model.pkl")
columns = joblib.load("model/feature_columns.pkl")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", columns=columns, input_data={})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.form.to_dict()
        input_df = pd.DataFrame([input_data])

        # Convert all input to float and ensure correct column order
        input_df = input_df.astype(float)
        input_df = input_df[columns]

        # Predict probability
        prediction = model.predict_proba(input_df)[0][1]

        return render_template("index.html", probability=round(prediction, 3), input_data=input_data, columns=columns)

    except Exception as e:
        return render_template("index.html", error=str(e), input_data=request.form, columns=columns)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
