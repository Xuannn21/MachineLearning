from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load your machine learning model (make sure the model is in the same directory)
model = joblib.load('customer_churn_model.pkl')
encoders = joblib.load('encoder.pkl')

# Home route to render the HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        tenure = float(request.form['tenure'])
        monthly_charges = float(request.form['monthly_charges'])
        total_charges = float(request.form['total_charges'])
        gender = request.form['gender']
        internet_service = request.form['internet_service']
        phone_service = request.form['phone_service']
        multiple_lines = request.form['multiple_lines']
        online_security = request.form['online_security']
        online_backup = request.form['online_backup']
        device_protection = request.form['device_protection']
        tech_support = request.form['tech_support']
        streaming_tv = request.form['streaming_tv']
        streaming_movies = request.form['streaming_movies']
        contract = request.form['contract']
        paperless_billing = request.form['paperless_billing']
        payment_method = request.form['payment_method']
        senior_citizen = request.form['senior_citizen']
        partner = request.form['partner']
        dependents = request.form['dependents']

        encoded_features = [
            encoders['gender'].transform([gender])[0],
            encoders['SeniorCitizen'].transform([senior_citizen])[0],
            encoders['Partner'].transform([partner])[0],    
            encoders['Dependents'].transform([dependents])[0],
            encoders['PhoneService'].transform([phone_service])[0],
            encoders['MultipleLines'].transform([multiple_lines])[0],
            encoders['InternetService'].transform([internet_service])[0],
            encoders['OnlineSecurity'].transform([online_security])[0],
            encoders['OnlineBackup'].transform([online_backup])[0],
            encoders['DeviceProtection'].transform([device_protection])[0],
            encoders['TechSupport'].transform([tech_support])[0],
            encoders['StreamingTV'].transform([streaming_tv])[0],
            encoders['StreamingMovies'].transform([streaming_movies])[0],
            encoders['Contract'].transform([contract])[0],
            encoders['PaperlessBilling'].transform([paperless_billing])[0],
            encoders['PaymentMethod'].transform([payment_method])[0]
        ]
        
        # Combine numerical and encoded features
        to_predict_array = [tenure, monthly_charges, total_charges] + encoded_features
        to_predict_array = np.array(to_predict_array).reshape((1, -1))
            
        # Perform the prediction
        prediction = model.predict(to_predict_array)[0]

        if prediction > 0.5:
            result = 'Will Churn'
        else:
            result = "Won't Churn"

        return jsonify ({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)