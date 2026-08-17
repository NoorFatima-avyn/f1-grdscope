from flask import Blueprint, jsonify
from services.jolpica import get_driver_standings, get_season_races
from google import genai
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime

load_dotenv(Path('D:/AI,ML NOOR/f1-gridscope/.env'))
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

predictions_bp = Blueprint('predictions', __name__)

@predictions_bp.route('/race/<int:year>/<int:round_num>', methods=['GET'])
def predict_race(year, round_num):
    try:
        standings_data = get_driver_standings(year)
        standings = standings_data[0].get('DriverStandings', []) if standings_data else []

        races_data = get_season_races(year)
        target_race = next((r for r in races_data if int(r['round']) == round_num), None)

        if not target_race:
            return jsonify({'error': 'Race not found'}), 404

        circuit_name = target_race['Circuit']['circuitName']
        race_name = target_race['raceName']
        country = target_race['Circuit']['Location']['country']
        race_date = target_race.get('date', '')
        today = datetime.now().strftime('%Y-%m-%d')

        if race_date and race_date > today:
            status = "WARNING: This race has NOT happened yet. This is an AI prediction based on current standings, circuit history and recent form."
        else:
            status = "NOTE: This race has already taken place. This prediction was generated based on pre-race data."

        standings_text = '\n'.join([
            f"P{s['position']}: {s['Driver']['givenName']} {s['Driver']['familyName']} ({s['Constructors'][0]['name']}) - {s['points']} pts"
            for s in standings[:10]
        ])

        prompt = (
            f"You are an expert F1 race analyst. Today is {today}.\n\n"
            f"Race: {race_name} {year}\n"
            f"Circuit: {circuit_name}, {country}\n"
            f"Round: {round_num}\n"
            f"Status: {status}\n\n"
            f"Current {year} Championship Standings (Top 10):\n{standings_text}\n\n"
            f"Predict the TOP 5 finishers with reasoning. Format exactly like:\n"
            f"[Status message]\n\n"
            f"P1 (Winner): [Driver] ([Team]) - [reason]\n"
            f"P2: [Driver] ([Team]) - [reason]\n"
            f"P3: [Driver] ([Team]) - [reason]\n"
            f"P4: [Driver] ([Team]) - [reason]\n"
            f"P5: [Driver] ([Team]) - [reason]\n\n"
            f"Key Factor: [one decisive factor for this race]"
        )

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
        )

        return jsonify({
            'race_name': race_name,
            'circuit': circuit_name,
            'country': country,
            'round': round_num,
            'year': year,
            'prediction': response.text
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500