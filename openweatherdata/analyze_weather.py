import sqlite3
import matplotlib.pyplot as plt
from collections import Counter

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

# bar chart for average temperature by city
cities_temp = [city for city, temp in avg_temp_results]
temps = [temp for city, temp in avg_temp_results]

plt.figure(figsize=(12, 8))
plt.barh(cities_temp, temps, edgecolor='black')
plt.xlabel("Average Temperature (°F)")
plt.title("Average Temperature by City (Spring Snapshot)")
plt.gca().invert_yaxis()  # So hottest cities appear at top
plt.tight_layout()
plt.savefig("average_temperature_chart.png")
plt.show()


# bar chart for most common weather conditions overall
conn = sqlite3.connect('travel_project.db')
cur = conn.cursor()
cur.execute('SELECT description FROM Weather')
descriptions = [row[0] for row in cur.fetchall()]
conn.close()

# count occurrences
condition_counts = Counter(descriptions)
labels = list(condition_counts.keys())
values = list(condition_counts.values())

plt.figure(figsize=(10, 6))
plt.bar(labels, values, edgecolor='black')
plt.xticks(rotation=45, ha='right')
plt.ylabel("Frequency")
plt.title("Most Common Weather Conditions Across All Cities")
plt.tight_layout()
plt.savefig("weather_condition_frequency.png")
plt.show()

# bar chart for average humidity by city 
cities_humidity = [city for city, humidity in avg_humidity_results]
humidity_values = [humidity for city, humidity in avg_humidity_results]

plt.figure(figsize=(12, 8))
plt.barh(cities_humidity, humidity_values, color='skyblue', edgecolor='black')
plt.xlabel("Average Humidity (%)")
plt.title("Average Humidity by City (Spring Snapshot)")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("average_humidity_chart.png")
plt.show()

print("\nResults saved to weather_analysis.txt") # check it all worked
