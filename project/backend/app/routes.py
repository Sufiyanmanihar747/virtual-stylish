# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from flask_reuploaded import UploadSet, configure_uploads, IMAGES
# import os
# from werkzeug.utils import secure_filename

# app = Flask(__name__)
# CORS(app)

# # Configure file upload settings
# app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.getcwd(), 'uploads')
# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)

# # Ensure the 'uploads' directory exists
# if not os.path.exists(app.config['UPLOADED_PHOTOS_DEST']):
#     os.makedirs(app.config['UPLOADED_PHOTOS_DEST'])

# # API to handle image upload
# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
    
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
    
#     # Save the file
#     file_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], file.filename)
#     file.save(file_path)

#     # Process the file (AI prediction logic can go here)
#     result = process_image(file_path)
    
#     return jsonify({'message': 'File uploaded successfully', 'result': result})

# def process_image(file_path):
#     # Placeholder function for AI prediction
#     # You can load and process the image, and pass it to TensorFlow or another model
#     return 'AI Result based on image processing'

# if __name__ == '__main__':
#     app.run(debug=True)
