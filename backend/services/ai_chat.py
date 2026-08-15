from google import genai
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path('D:/AI,ML NOOR/f1-gridscope/.env'))

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def get_f1_response(user_message, year=2024):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_message,
    )
    return response.text