from flask import Flask
# from flask_cors import CORS 
import firebase_admin
from firebase_admin import credentials, storage

# Initialize Flask app
app = Flask(__name__)
# CORS(app)

cred = credentials.Certificate('./firebase/firebase_credential.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'stylist-app-df191'
})

from app import routes
