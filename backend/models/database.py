import firebase_admin
from firebase_admin import credentials, firestore
from pathlib import Path

key_path = Path('D:/AI,ML NOOR/f1-gridscope/firebase-key.json')

if not firebase_admin._apps:
    cred = credentials.Certificate(str(key_path))
    firebase_admin.initialize_app(cred)

db = firestore.client(database_id='f1-gridscopedb')