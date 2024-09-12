from flask import Flask, request, render_template
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load your machine learning model (make sure the model is in the same directory)
model = joblib.load('customer_churn_random_forest_model.pkl')

# Home route to render the HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    tenure = float(request.form['tenure'])
    monthlycharges = float(request.form['monthlycharges'])
    totalcharges = float(request.form['totalcharges'])
    gender = request.form['gender']
    internetservice = request.form['internetservice']

    # Process the data for prediction (you may need to preprocess it depending on the model)
    data = np.array([[tenure, monthlycharges, totalcharges, gender, internetservice]])

    # Perform the prediction
    prediction = model.predict(data)[0]

    # Render the result in the HTML page
    return render_template('index.html', prediction_text=f'Churn Prediction: {prediction}')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
