import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import StandardScaler
import pickle
from features_extract import extract_features

# Create flask app
flask_app = Flask(__name__)

# Load your model parameters
model = pickle.load(open("model.pkl", "rb"))
weights = model["weights"]
bias = model["bias"]
scaler = model["scaler"]

# Your custom predict function
def custom_predict(X):
    m, n = X.shape
    p = np.zeros(m)
    for i in range(m):
        z = np.dot(X[i], weights) + bias
        f = 1 / (1 + np.exp(-z))  # Sigmoid
        p[i] = 1 if f >= 0.5 else 0
    return p

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    # Parse input features from the form, excluding the URL input
    form_data = request.form.to_dict()
    url_input = form_data.pop("url", None)  # Remove the 'url' field if it exists
    float_features = [float(x) for x in form_data.values() if x.strip()]  # Convert remaining fields to float
    features = np.array([float_features])  # Convert to 2D array
    features = scaler.transform(features)  # Apply scaler

    prediction = custom_predict(features)
    prediction_text = "URL is safe" if prediction[0] == 1 else "WARNING! URL unsafe, proceed with caution"

    # Pass prediction_text and feature names to the template
    return render_template("index.html", prediction_text=prediction_text, feature_names=list(form_data.keys()))



@flask_app.route("/auto_extract", methods=["POST"])
def auto_extract():
    data = request.json
    url = data.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        features = extract_features(url)[0]
        return jsonify(features.tolist())  # Return features as a JSON array
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    flask_app.run(debug=True)
