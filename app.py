from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load your model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    data = request.form.to_dict()
    input_data = pd.DataFrame([data])

    # Make a prediction
    prediction = model.predict(input_data)[0]

    # Return the result
    return jsonify({'prediction': 'Default' if prediction == 1 else 'No Default'})

if __name__ == '__main__':
    app.run(debug=True)
