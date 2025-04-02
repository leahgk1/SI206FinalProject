import sqlite3

# connect to the SQLite database
conn = sqlite3.connect('travel_project.db')
cur = conn.cursor()

# join Cities and Weather to calculate average temperature per city. creates one big table with all the information needed
cur.execute('''
    SELECT Cities.name, AVG(Weather.temperature)
    FROM Weather
    JOIN Cities ON Weather.city_id = Cities.id
    GROUP BY Cities.name
    ORDER BY AVG(Weather.temperature) DESC
''')

results = cur.fetchall()

# write the results to a text file
with open("average_temperatures.txt", "w") as f:
    f.write("Average Temperature by City (°F):\n\n")
    for city, avg_temp in results:
        line = f"{city}: {avg_temp:.2f}°F"
        print(line)        # also print to terminal to verify
        f.write(line + "\n")

conn.close()
print("Results saved to average_temperatures.txt")
