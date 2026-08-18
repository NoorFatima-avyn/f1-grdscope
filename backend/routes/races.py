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
@races_bp.route('/<int:year>/results', methods=['GET'])
def get_all_results(year):
    races = get_season_races(year)
    results = []
    for race in races:
        results.append({
            'round': race.get('round'),
            'raceName': race.get('raceName'),
            'circuit': race.get('Circuit', {}).get('circuitName'),
            'country': race.get('Circuit', {}).get('Location', {}).get('country'),
            'date': race.get('date'),
            'circuitId': race.get('Circuit', {}).get('circuitId')
        })
    return jsonify(results)
@races_bp.route('/circuit/<circuit_id>/winners', methods=['GET'])
def get_circuit_winners_route(circuit_id):
    from services.jolpica import get_circuit_winners
    data = get_circuit_winners(circuit_id)
    return jsonify(data) 
@races_bp.route('/circuit/<circuit_id>/image', methods=['GET'])
def get_circuit_image(circuit_id):
    from services.jolpica import get_wikipedia_image
    circuit_wiki_names = {
        'bahrain': 'Bahrain_International_Circuit',
        'jeddah': 'Jeddah_Street_Circuit',
        'albert_park': 'Albert_Park_Circuit',
        'suzuka': 'Suzuka_International_Racing_Course',
        'shanghai': 'Shanghai_International_Circuit',
        'miami': 'Miami_International_Autodrome',
        'imola': 'Autodromo_Enzo_e_Dino_Ferrari',
        'monaco': 'Circuit_de_Monaco',
        'catalunya': 'Circuit_de_Barcelona-Catalunya',
        'villeneuve': 'Circuit_Gilles_Villeneuve',
        'red_bull_ring': 'Red_Bull_Ring',
        'silverstone': 'Silverstone_Circuit',
        'hungaroring': 'Hungaroring',
        'spa': 'Circuit_de_Spa-Francorchamps',
        'zandvoort': 'Circuit_Zandvoort',
        'monza': 'Autodromo_Nazionale_Monza',
        'baku': 'Baku_City_Circuit',
        'marina_bay': 'Marina_Bay_Street_Circuit',
        'americas': 'Circuit_of_the_Americas',
        'rodriguez': 'Autodromo_Hermanos_Rodriguez',
        'interlagos': 'Autodromo_Jose_Carlos_Pace',
        'vegas': 'Las_Vegas_Street_Circuit',
        'losail': 'Losail_International_Circuit',
        'yas_marina': 'Yas_Marina_Circuit'
    }
    wiki_name = circuit_wiki_names.get(circuit_id, '')
    if not wiki_name:
        return jsonify({'image': ''})
    img = get_wikipedia_image(wiki_name)
    return jsonify({'image': img})

@races_bp.route('/circuit/<circuit_id>/detail', methods=['GET'])
def get_circuit_detail(circuit_id):
    import requests as req
    from datetime import datetime
    today = datetime.now().strftime('%Y-%m-%d')
    
    winners = {}
    circuit_info = {}
    
    for year in [2021, 2022, 2023, 2024, 2025, 2026]:
        url = f"https://api.jolpi.ca/ergast/f1/{year}/circuits/{circuit_id}/results/1.json"
        try:
            response = req.get(url, timeout=8)
            data = response.json()
            races = data['MRData']['RaceTable']['Races']
            if races:
                r = races[0]
                if not circuit_info:
                    circuit_info = {
                        'circuitId': circuit_id,
                        'circuitName': r['Circuit']['circuitName'],
                        'country': r['Circuit']['Location']['country'],
                        'locality': r['Circuit']['Location']['locality'],
                        'lat': r['Circuit']['Location']['lat'],
                        'long': r['Circuit']['Location']['long'],
                        'url': r['Circuit'].get('url', '')
                    }
                result = r['Results'][0]
                race_date = r.get('date', '')
                winners[str(year)] = {
                    'driver': f"{result['Driver']['givenName']} {result['Driver']['familyName']}",
                    'constructor': result['Constructor']['name'],
                    'raceName': r['raceName'],
                    'date': race_date,
                    'laps': result.get('laps', '-'),
                    'grid': result.get('grid', '-'),
                    'status': result.get('status', '-')
                }
            else:
                race_date_url = f"https://api.jolpi.ca/ergast/f1/{year}/circuits/{circuit_id}/races.json"
                r2 = req.get(race_date_url, timeout=5).json()
                races2 = r2['MRData']['RaceTable']['Races']
                if races2:
                    rd = races2[0].get('date', '')
                    if rd > today:
                        winners[str(year)] = {'status': 'upcoming', 'raceName': races2[0]['raceName'], 'date': rd}
        except:
            continue
    
    return jsonify({
        'circuit': circuit_info,
        'winners': winners
    })  
