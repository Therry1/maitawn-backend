import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

def get_firebase_db():
    if not firebase_admin._apps:
        cred_json = os.environ.get("FIREBASE_CREDENTIALS")
        cred_dict = json.loads(cred_json)
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred, {
            "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET")
        })
    return firestore.client()