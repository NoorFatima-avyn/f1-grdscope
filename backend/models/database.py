import firebase_admin
from firebase_admin import credentials, firestore
import os
import json
from pathlib import Path

if not firebase_admin._apps:
    firebase_key_json = os.environ.get("FIREBASE_KEY_JSON")
    
    if firebase_key_json:
        key_dict = json.loads(firebase_key_json)
        cred = credentials.Certificate(key_dict)
    else:
        key_path = Path('D:/AI,ML NOOR/f1-gridscope/firebase-key.json')
        cred = credentials.Certificate(str(key_path))
    
    firebase_admin.initialize_app(cred)

db = firestore.client(database_id='f1-gridscopedb')