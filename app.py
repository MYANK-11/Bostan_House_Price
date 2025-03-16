#Note:- Always First write the library in the requirements.txt then we will install them in the new envirnoment using the pip install -r requirements.txt and only then we can import the lib start the code in the app.py or any other file  

# import pickle # it is used to load the ml file i.e. in our case it is Bostan House Price Predicition
# from flask import Flask,render_template,request,app,jsonify,url_for,render_template
# import numpy  as np
# import pandas as pd 



# app=Flask(__name__) 
# model=pickle.load(open('Bostan.pkl','rb')) # loaded the model 
# scalar=pickle.load(open('scaling.pkl','rb'))
# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/predict_api',methods=['POST'])

# def predict_api():
#     data=request.json['data']
#     print(data)
#     print(np.array(list(data.values())).reshape(1,-1))
#     new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
#     output=model.predict(new_data)
#     print(output[0])
#     return jsonify(output[0])

# if __name__=='__main__':
#     app.run(debug=True)


import pickle  # Used to load the ML model and scaler
from flask import Flask, render_template, request, jsonify  # Import necessary Flask modules
import numpy as np  # Used for numerical operations and array manipulations
import pandas as pd  # (Not used in the current code, can be removed)

# Initialize Flask application
app = Flask(__name__)

# Load the trained machine learning model
# Ensure the file 'Boston.pkl' (correct spelling) exists in the same directory
model = pickle.load(open('Boston.pkl', 'rb'))  

# Load the scaler used for feature transformation
scalar = pickle.load(open('scaling.pkl', 'rb'))  

# Define the home route which renders the homepage
@app.route('/')
def home():
    return render_template('home.html')  # Make sure 'home.html' exists in the templates folder

# API endpoint for predictions using POST method
@app.route('/predict_api', methods=['POST'])
def predict_api():
    """
    This function receives JSON input, processes it, and returns the model prediction.
    """
    # Extract JSON data from the POST request
    data = request.json  # Entire JSON payload
    if 'data' not in data:
        return jsonify({'error': 'Invalid input, "data" key missing'}), 400  # Handle missing key

    data_values = data['data']  # Extract 'data' key
    print("Received input data:", data_values)

    # Convert input dictionary values to a NumPy array and reshape for model compatibility
    input_array = np.array(list(data_values.values())).reshape(1, -1)
    print("Reshaped Input Array:", input_array)

    # Apply the same scaling transformation used during model training
    new_data = scalar.transform(input_array)

    # Predict using the loaded model
    output = model.predict(new_data)
    print("Model Prediction:", output[0])

    # Return the prediction result as JSON
    return jsonify(output[0])

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for easier debugging
