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
            config={
                "system_instruction": """You are an expert F1 analyst. You ONLY answer questions about Formula 1 — drivers, teams, races, cars, circuits, championships, incidents, and F1 history from 2021 to 2026. 
If someone asks about anything unrelated to F1, politely say: 'I only know about Formula 1! Ask me anything about F1 🏎️'
Never answer questions about other sports, politics, general knowledge, or anything outside F1."""
            }
        )
    
    return response.text