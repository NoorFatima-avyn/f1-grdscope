import requests

BASE_URL = "https://api.openf1.org/v1"

def get_driver_headshots(year):
    url = f"{BASE_URL}/drivers?session_key=latest"
    response = requests.get(url)
    data = response.json()
    
    headshots = {}
    for driver in data:
        if not isinstance(driver, dict):
            continue
        abbr = driver.get('name_acronym', '')
        headshot = driver.get('headshot_url', '')
        if abbr and headshot:
            headshots[abbr] = headshot
    
    return headshots