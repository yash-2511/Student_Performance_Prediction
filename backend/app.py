
from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import joblib
import os

app = Flask(__name__, static_folder='../frontend')

# Load model and preprocessors
model = joblib.load("../models/model.pkl")
scaler = joblib.load("../models/scaler.pkl")
encoder = joblib.load("../models/encoder.pkl")

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory(app.static_folder, path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    df[["internet", "parent_education"]] = encoder.transform(df[["internet", "parent_education"]])
    scaled_input = scaler.transform(df)
    prediction = model.predict(scaled_input)[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
