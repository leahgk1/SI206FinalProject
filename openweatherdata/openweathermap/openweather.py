from api_weather_key import API_KEY
import sqlite3
import requests
import time

db_name = 'travel_project.db'
base_url = 'https://api.openweathermap.org/data/2.5/weather'

cities = [
    "New York", "Los Angeles", "Chicago", "Miami", "San Francisco",
    "Las Vegas", "Orlando", "Seattle", "San Diego", "Boston",
    "Denver", "New Orleans", "Atlanta", "Phoenix", "Austin",
    "Portland", "Washington", "Dallas", "Houston", "Philadelphia",
    "Tampa", "Minneapolis", "Nashville", "Charlotte", "Salt Lake City"
]

def store_weather_data():
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    count = 0

    for city in cities:
        if count >= 25:
            print("Reached 25 cities — stopping this run.")
            break

        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'imperial'
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200 and "main" in data:
            city_name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            timestamp = data["dt"]  # for API response

            # insert city into Cities table if it doesn't exist
            cur.execute("INSERT OR IGNORE INTO Cities (name, country) VALUES (?, ?)", (city_name, country))
            conn.commit()

            # get the city_id
            cur.execute("SELECT id FROM Cities WHERE name = ?", (city_name,))
            city_id = cur.fetchone()[0]

            # avoid duplicate weather records for the same timestamp
            cur.execute("SELECT * FROM Weather WHERE city_id = ? AND datetime = ?", (city_id, timestamp))
            if cur.fetchone():
                print(f"Skipping duplicate weather for {city_name} at timestamp {timestamp}")
                continue

            # insert weather data
            cur.execute('''
                INSERT INTO Weather (city_id, temperature, humidity, description, datetime)
                VALUES (?, ?, ?, ?, ?)
            ''', (city_id, temperature, humidity, description, timestamp))

            conn.commit()
            print(f"Stored weather for {city_name}: {temperature}°F, {description}")
            count += 1

        else:
            print(f"Failed to get weather for {city}: {data.get('message', 'Unknown error')}")

        time.sleep(1) # to avoid hitting the API rate limit, sleep for 1 second between requests

    conn.close()

if __name__ == "__main__":
    store_weather_data()

# run this file everyday for 4 days at the same time to stay consistent and make 100 total rows 