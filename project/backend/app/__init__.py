from flask import Flask
from flask_cors import CORS  # type: ignore
import firebase_admin # type: ignore
from firebase_admin import credentials, storage # type: ignore

# Initialize Flask app
app = Flask(__name__)
CORS(app)

cred = credentials.Certificate('./firebase/firebase_credential.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'stylist-app-df191'
})

from app import routes
