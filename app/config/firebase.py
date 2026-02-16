import os
import firebase_admin
from firebase_admin import credentials, firestore, auth
from dotenv import load_dotenv

load_dotenv()


class FirebaseConfig:
    """Configuration Firebase"""
    
    _initialized = False
    _db = None
    
    @classmethod
    def initialize(cls):
        """Initialiser Firebase"""
        if not cls._initialized:
            cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
            
            if cred_path and os.path.exists(cred_path):
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)
            else:
                # Utiliser les credentials par défaut (pour Cloud Run, etc.)
                firebase_admin.initialize_app()
            
            cls._db = firestore.client()
            cls._initialized = True
    
    @classmethod
    def get_db(cls):
        """Obtenir le client Firestore"""
        if not cls._initialized:
            cls.initialize()
        return cls._db
    
    @classmethod
    def get_auth(cls):
        """Obtenir le module Auth"""
        if not cls._initialized:
            cls.initialize()
        return auth