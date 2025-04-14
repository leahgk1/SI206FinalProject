import json
import sqlite3
import pandas as pd

# Step 1: Load JSON data
with open('hotel_prices.json', 'r') as f:
    data = json.load(f)

# Step 2: Flatten the JSON into a list of dictionaries
rows = []
for city, hotels in data.items():
    for hotel_name, price in hotels.items():
        rows.append({'city': city, 'hotel': hotel_name, 'price': price})

# Step 3: Create a DataFrame
df = pd.DataFrame(rows)

# Step 4: Create a SQLite database and insert the data
conn = sqlite3.connect('hotels.db')  # creates file hotels.db
df.to_sql('hotel_prices', conn, if_exists='replace', index=False)

# (Optional) Step 5: Query the database to verify
result = pd.read_sql("SELECT * FROM hotel_prices LIMIT 5;", conn)
print(result)

# Close the connection
conn.close()