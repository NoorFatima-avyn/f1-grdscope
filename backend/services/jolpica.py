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