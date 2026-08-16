from flask import Blueprint, jsonify
from services.jolpica import get_race_winner, get_season_races

races_bp = Blueprint('races', __name__)

@races_bp.route('/<int:year>/<int:round_num>/winner', methods=['GET'])
def get_winner(year, round_num):
    data = get_race_winner(year, round_num)
    return jsonify(data)

@races_bp.route('/<int:year>', methods=['GET'])
def get_races(year):
    data = get_season_races(year)
    return jsonify(data)

@races_bp.route('/<int:year>/<int:round_num>/podium', methods=['GET'])
def get_podium(year, round_num):
    import requests
    url = f"https://api.jolpi.ca/ergast/f1/{year}/{round_num}/results.json"
    response = requests.get(url)
    data = response.json()
    races = data['MRData']['RaceTable']['Races']
    if not races:
        return jsonify([])
    results = races[0].get('Results', [])[:3]
    podium = []
    for r in results:
        podium.append({
            'position': r['position'],
            'driver': f"{r['Driver']['givenName']} {r['Driver']['familyName']}",
            'driver_id': r['Driver']['driverId'],
            'constructor': r['Constructor']['name'],
            'points': r['points'],
            'time': r.get('Time', {}).get('time', 'N/A'),
            'grid': r.get('grid', '-'),
            'laps': r.get('laps', '-')
        })
    return jsonify(podium)
