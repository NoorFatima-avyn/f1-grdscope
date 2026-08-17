from flask import Blueprint, jsonify, request
from services.jolpica import get_driver_standings, get_season_races, get_race_winner
from google import genai
import os
from dotenv import load_dotenv
from pathlib import Path

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

        standings_text = '\n'.join([
            f"P{s['position']}: {s['Driver']['givenName']} {s['Driver']['familyName']} ({s['Constructors'][0]['name']}) - {s['points']} pts"
            for s in standings[:10]
        ])

        from datetime import datetime
today = datetime.now().strftime('%Y-%m-%d')

prompt = f"""You are an expert F1 race analyst and predictor. Today's date is {today}.

Race to predict: {race_name} {year}
Circuit: {circuit_name}, {country}
Round: {round_num}

Current {year} Championship Standings (Top 10):
{standings_text}

IMPORTANT CONTEXT:
- If this race has NOT happened yet, clearly state: "⚠️ This race hasn't happened yet — this is an AI prediction based on current form, circuit history, and championship standings."
- If this race HAS already happened, state: "📊 This race has already taken place. Here is what the AI predicted based on pre-race data."
- Base your prediction on: current standings, recent race pace, circuit characteristics, tyre strategies, and historical performance at {circuit_name}.

Predict the TOP 5 race finishers with reasoning.

Format EXACTLY like this:
⚠️ [Status message about whether race has happened]

🥇 P1: [Driver Name] ([Team]) - [One sentence reason]
🥈 P2: [Driver Name] ([Team]) - [One sentence reason]  
🥉 P3: [Driver Name] ([Team]) - [One sentence reason]
P4: [Driver Name] ([Team]) - [One sentence reason]
P5: [Driver Name] ([Team]) - [One sentence reason]

📊 Key Factor: [One key factor that could decide this race]
📝 Note: These predictions are based on {today} data including qualifying results and practice sessions where available."""

Race to predict: {race_name} {year}
Circuit: {circuit_name}, {country}
Round: {round_num}

Current {year} Championship Standings (Top 10):
{standings_text}

Based on:
1. Current championship standings and momentum
2. Historical performance at {circuit_name}
3. Team strengths and recent form
4. Circuit characteristics

Predict the TOP 5 race finishers. Be specific and give brief reasoning for each pick.

Format your response EXACTLY like this:
🥇 P1: [Driver Name] ([Team]) - [One sentence reason]
🥈 P2: [Driver Name] ([Team]) - [One sentence reason]
🥉 P3: [Driver Name] ([Team]) - [One sentence reason]
P4: [Driver Name] ([Team]) - [One sentence reason]
P5: [Driver Name] ([Team]) - [One sentence reason]

Then add: "📊 Key Factor: [One key factor that could decide this race]"
"""

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