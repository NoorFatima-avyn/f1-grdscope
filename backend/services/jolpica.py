import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"

def get_season_drivers(year):
    url = f"{BASE_URL}/{year}/drivers.json"
    response = requests.get(url)
    data = response.json()
    return data['MRData']['DriverTable']['Drivers']

def get_season_races(year):
    url = f"{BASE_URL}/{year}/races.json"
    response = requests.get(url)
    data = response.json()
    return data['MRData']['RaceTable']['Races']

def get_driver_standings(year):
    url = f"{BASE_URL}/{year}/driverStandings.json"
    response = requests.get(url)
    data = response.json()
    return data['MRData']['StandingsTable']['StandingsLists']

def get_constructor_standings(year):
    url = f"{BASE_URL}/{year}/constructorStandings.json"
    response = requests.get(url)
    data = response.json()
    return data['MRData']['StandingsTable']['StandingsLists']

def get_race_results(year, round_num):
    url = f"{BASE_URL}/{year}/{round_num}/results.json"
    response = requests.get(url)
    data = response.json()
    return data['MRData']['RaceTable']['Races']
def get_race_winner(year, round_num):
    url = f"{BASE_URL}/{year}/{round_num}/results.json"
    response = requests.get(url)
    data = response.json()
    races = data['MRData']['RaceTable']['Races']
    if not races:
        return None
    results = races[0].get('Results', [])
    if not results:
        return None
    winner = results[0]
    return {
        'driver': f"{winner['Driver']['givenName']} {winner['Driver']['familyName']}",
        'constructor': winner['Constructor']['name'],
        'time': winner.get('Time', {}).get('time', 'N/A')
    }
def get_wikipedia_image(search_term):
    import urllib.parse
    encoded = urllib.parse.quote(search_term)
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        return data.get('thumbnail', {}).get('source', '')
    except:
        return ''
def get_circuit_winners(circuit_id):
    winners = []
    for year in [2021, 2022, 2023, 2024, 2025]:
        url = f"{BASE_URL}/{year}/circuits/{circuit_id}/results/1.json"
        try:
            response = requests.get(url, timeout=5)
            data = response.json()
            races = data['MRData']['RaceTable']['Races']
            if races:
                r = races[0]
                result = r['Results'][0]
                winners.append({
                    'year': year,
                    'driver': f"{result['Driver']['givenName']} {result['Driver']['familyName']}",
                    'constructor': result['Constructor']['name'],
                    'raceName': r['raceName']
                })
        except:
            continue
    return winners   