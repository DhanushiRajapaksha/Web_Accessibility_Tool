from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import tensorflow as tf

# Load the TensorFlow model
model = tf.keras.models.load_model('COLORCONTRAST.h5')

app = Flask(__name__)
CORS(app)  # Enable CORS to allow communication with React frontend

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Receive input from React as JSON
        data = request.json
        input_features = np.array(data['features']).reshape(1, -1)  # Reshape to match model input shape
        
        # Get predictions
        predictions = model.predict(input_features)
        
        # Convert predictions to a list and send them back
        return jsonify({'suggested_colors': predictions.tolist()})
    except Exception as e:
        return jsonify({'Error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

'''from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load your model
model = tf.keras.models.load_model("COLORCONTRAST.h5")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = np.array(data['input_data']).reshape(1, -1)  # Adjust reshape if necessary
    predictions = model.predict(input_data)
    return jsonify({"predicted_colors": predictions.tolist()})

if __name__ == '__main__':
    app.run(debug=True)'''

