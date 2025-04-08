#Leah Kim
import requests
import sqlite3
from datetime import datetime

API_KEY = "" # Trip advisor API requires payment information. Will complete later. 
# Use of tripadvisor api is improbable; will most likely use Yelp api upon discussion with my teammates.
BASE_URL = "https://api.content.tripadvisor.com/api/v1"

def get_city_data(city_name):
    """Get TripAdvisor data for a given city"""
    
    location_search_url = f"{BASE_URL}/location/search"
    params = {
        "key": API_KEY,
        "searchQuery": city_name,
        "language": "en"
    }
    
    try:
        response = requests.get(location_search_url, params=params)
        response.raise_for_status()
        location_data = response.json()
        
        if not location_data.get("data"):
            print(f"No data found for {city_name}")
            return None
            
        location_id = location_data["data"][0]["location_id"]
        
        attractions_url = f"{BASE_URL}/location/{location_id}/attractions"
        params = {
            "key": API_KEY,
            "language": "en"
        }
        
        response = requests.get(attractions_url, params=params)
        response.raise_for_status()
        attractions_data = response.json()
        
        return {
            "city_name": city_name,
            "num_attractions": len(attractions_data.get("data", [])),
            "rating": attractions_data.get("data", [{}])[0].get("rating", "N/A") if attractions_data.get("data") else "N/A"
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {city_name}: {str(e)}")
        return None

def store_city_data():
    """Store city data in SQLite database"""
    conn = sqlite3.connect('travel_project.db')
    cur = conn.cursor()
    
    cur.execute('''CREATE TABLE IF NOT EXISTS CityAttractions
                   (id INTEGER PRIMARY KEY,
                    city_name TEXT,
                    num_attractions INTEGER,
                    rating REAL,
                    datetime TEXT)''')
    
    cities = [
        "New York City", "Orlando", "Miami", "Boston", "Washington D.C.",
        "Philadelphia", "Atlanta", "Charleston", "Savannah", "Richmond",
        "Charlotte", "Cleveland", "Baltimore", "Pittsburgh", "Detroit",
        "Jacksonville", "Indianapolis", "Hartford", "Cincinnati", "Providence",
        "Columbus", "Raleigh", "Buffalo", "Augusta", "Tampa"
    ]
    
    for city in cities:
        city_data = get_city_data(city)
        if city_data:
            cur.execute('''INSERT INTO CityAttractions 
                          (city_name, num_attractions, rating, datetime)
                          VALUES (?, ?, ?, ?)''',
                       (city_data["city_name"],
                        city_data["num_attractions"],
                        city_data["rating"],
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    store_city_data()
