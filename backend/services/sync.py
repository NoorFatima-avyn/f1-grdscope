from services.jolpica import get_season_drivers, get_season_races, get_driver_standings
from services.openf1 import get_driver_headshots
from models.database import db

def sync_drivers(year):
    drivers = get_season_drivers(year)
    headshots = get_driver_headshots(year)
    
    for driver in drivers:
        code = driver.get('code', '')
        headshot = headshots.get(code, '')
        
        data = {
            'driver_id': driver.get('driverId'),
            'given_name': driver.get('givenName'),
            'family_name': driver.get('familyName'),
            'code': code,
            'permanent_number': driver.get('permanentNumber'),
            'nationality': driver.get('nationality'),
            'headshot_url': headshot,
            'year': int(year)
        }
        
        db.collection('drivers').document(f"{year}_{driver.get('driverId')}").set(data)
    
    print(f"Synced {len(drivers)} drivers for {year} ✅")

def sync_races(year):
    races = get_season_races(year)
    
    for race in races:
        data = {
            'season': int(year),
            'round': int(race.get('round')),
            'race_name': race.get('raceName'),
            'circuit_name': race.get('Circuit', {}).get('circuitName'),
            'country': race.get('Circuit', {}).get('Location', {}).get('country'),
            'date': race.get('date')
        }
        
        db.collection('races').document(f"{year}_round{race.get('round')}").set(data)
    
    print(f"Synced {len(races)} races for {year} ✅")

def sync_standings(year):
    standings_data = get_driver_standings(year)
    if not standings_data:
        return
    
    standings = standings_data[0].get('DriverStandings', [])
    
    for standing in standings:
        data = {
            'season': int(year),
            'driver_id': standing['Driver']['driverId'],
            'position': int(standing.get('position', 0)),
            'points': float(standing.get('points', 0)),
            'wins': int(standing.get('wins', 0)),
            'constructor': standing['Constructors'][0]['name'] if standing.get('Constructors') else None
        }
        
        db.collection('standings').document(
            f"{year}_{standing['Driver']['driverId']}"
        ).set(data)
    
    print(f"Synced standings for {year} ✅")

def sync_all(years=[2021, 2022, 2023, 2024, 2025]):
    for year in years:
        print(f"Syncing {year}...")
        sync_drivers(year)
        sync_races(year)
        sync_standings(year)
        print(f"Done {year} ✅")
          