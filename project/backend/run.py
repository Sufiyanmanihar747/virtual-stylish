from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
from werkzeug.datastructures import FileStorage

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import pdb

model = MobileNetV2(weights='imagenet')

app = Flask(__name__)
CORS(app)

# Configure file upload settings
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.path.dirname(__file__), 'uploads')

if not os.path.exists(app.config['UPLOADED_PHOTOS_DEST']):
    os.makedirs(app.config['UPLOADED_PHOTOS_DEST'])

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

@app.route('/upload', methods=['POST'])

def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    file_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], file.filename)
    # pdb.set_trace()
    # return f"The result is {file_path}"
    file.save(file_path)

    result = process_image(file_path)
    
    return jsonify({'message': 'File uploaded successfully', 'result': result})

def process_image(file_path):
    
    img = image.load_img(file_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    # pdb.set_trace()
    # return f"The result is {img_array}"
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)

    decoded_predictions = decode_predictions(predictions, top=3)[0]
    
    # Return the top-3 predictions
    result = [{'class': pred[1], 'description': pred[1], 'confidence': float(pred[2])} for pred in decoded_predictions]
    return result

if __name__ == '__main__':
    app.run(debug=True)
