import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"

def get_season_drivers(year):
    url = f"{BASE_URL}/{year}/drivers.json"
    response = requests.get(url)
    data = response.json()
    drivers = data['MRData']['DriverTable']['Drivers']
    return drivers