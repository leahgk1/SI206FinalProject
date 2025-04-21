from api_weather_key import API_KEY
import sqlite3
import requests
import time
from datetime import datetime
import pytz

db_name = 'travel_project.db'
base_url = 'https://api.openweathermap.org/data/2.5/weather'

cities = [
    "New York City", "Orlando", "Miami", "Boston", "Washington D.C.",
    "Philadelphia", "Atlanta", "Charleston", "Savannah", "Richmond",
    "Charlotte", "Cleveland", "Baltimore", "Pittsburgh", "Detroit",
    "Jacksonville", "Indianapolis", "Hartford", "Cincinnati", "Providence",
    "Columbus", "Raleigh", "Buffalo", "Augusta", "Tampa"
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
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            timestamp = data["dt"]  # UNIX timestamp

            # convert to EST time
            utc_time = datetime.utcfromtimestamp(timestamp)
            est = pytz.timezone('US/Eastern')
            est_time = utc_time.replace(tzinfo=pytz.utc).astimezone(est)
            formatted_time = est_time.strftime("%Y-%m-%d %I:%M %p")

            # insert city if not already there
            cur.execute("INSERT OR IGNORE INTO Cities (name) VALUES (?)", (city_name,))
            conn.commit()

            # get the city_id from the Cities table
            cur.execute("SELECT id FROM Cities WHERE name = ?", (city_name,))
            city_id = cur.fetchone()[0]

            # avoid duplicate weather records
            cur.execute("SELECT * FROM Weather WHERE city_id = ? AND datetime = ?", (city_id, timestamp))
            if cur.fetchone():
                print(f"Skipping duplicate weather for {city_name} at timestamp {timestamp}")
                continue

            # insert weather data
            cur.execute('''
                INSERT INTO Weather (city_id, temperature, humidity, description, datetime, formatted_time)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (city_id, temperature, humidity, description, timestamp, formatted_time))

            conn.commit()
            print(f"Stored weather for {city_name}: {temperature}°F, {description}, {formatted_time} EST")
            count += 1

        else:
            print(f"Failed to get weather for {city}: {data.get('message', 'Unknown error')}")

        time.sleep(1)  # avoid hitting API rate limit

    conn.close()

if __name__ == "__main__":
    store_weather_data()
