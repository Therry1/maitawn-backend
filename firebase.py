import firebase_admin
from firebase_admin import credentials , firestore

cred = credentials.Certificate("maitawn-firebase-adminsdk-fbsvc-941841e5af.json")
firebase_admin.initialize_app(cred)

get_firebase_db = firestore.client()