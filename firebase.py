# import firebase_admin
# from firebase_admin import credentials , firestore

# cred = credentials.Certificate("maitawn-firebase-adminsdk-fbsvc-941841e5af.json")
# firebase_admin.initialize_app(cred)

# get_firebase_db = firestore.client()

import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

firebase_json = os.getenv("FIREBASE_CREDENTIALS")

cred_dict = json.loads(firebase_json)

cred = credentials.Certificate(cred_dict)

firebase_admin.initialize_app(cred)

get_firebase_db = firestore.client()
