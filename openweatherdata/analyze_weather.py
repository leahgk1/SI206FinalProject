import sqlite3


conn = sqlite3.connect('travel_project.db')
cur = conn.cursor()

# average temp per city
cur.execute('''
    SELECT Cities.name, AVG(Weather.temperature)
    FROM Weather
    JOIN Cities ON Weather.city_id = Cities.id
    GROUP BY Cities.name
    ORDER BY AVG(Weather.temperature) DESC
''')

avg_temp_results = cur.fetchall()

# average humidity per city
cur.execute('''
    SELECT Cities.name, AVG(Weather.humidity)
    FROM Weather
    JOIN Cities ON Weather.city_id = Cities.id
    GROUP BY Cities.name
    ORDER BY AVG(Weather.humidity) ASC
''')

avg_humidity_results = cur.fetchall()

# most common weather per city
cur.execute('''
    SELECT Cities.name, Weather.description, COUNT(*) as freq
    FROM Weather
    JOIN Cities ON Weather.city_id = Cities.id
    GROUP BY Cities.name, Weather.description
    ORDER BY Cities.name, freq DESC
''')

# store most common condition per city
condition_by_city = {}
for city, desc, freq in cur.fetchall():
    if city not in condition_by_city:
        condition_by_city[city] = (desc, freq)

# write into text file
with open("weather_analysis.txt", "w") as f:
    f.write("Average Temperature by City (°F):\n\n")
    for city, avg_temp in avg_temp_results:
        line = f"{city}: {avg_temp:.2f}°F"
        print(line)
        f.write(line + "\n")

    f.write("\nAverage Humidity by City (%):\n\n")
    for city, avg_humidity in avg_humidity_results:
        line = f"{city}: {avg_humidity:.2f}%"
        print(line)
        f.write(line + "\n")

    f.write("\nMost Common Weather Condition by City:\n\n")
    for city, (desc, freq) in condition_by_city.items():
        line = f"{city}: {desc} ({freq} times)"
        print(line)
        f.write(line + "\n")

conn.close()
print("\nResults saved to weather_analysis.txt") # check it all worked