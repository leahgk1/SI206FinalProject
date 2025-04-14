import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to your database
conn = sqlite3.connect('hotels.db')  # Make sure this file is in your working directory

# Step 2: Query average prices by city
query = """
SELECT city, AVG(price) AS average_price
FROM hotel_prices
GROUP BY city
ORDER BY average_price DESC
"""
df_avg_prices = pd.read_sql(query, conn)

# Step 3: Close the connection
conn.close()

# Step 4: Plot the data using matplotlib
plt.figure(figsize=(12, 6))  # size of the graph
plt.bar(df_avg_prices['city'], df_avg_prices['average_price'])
plt.xticks(rotation=90)  # rotate city names for readability
plt.xlabel('City')
plt.ylabel('Average Hotel Price ($)')
plt.title('Average Hotel Prices by City')
plt.tight_layout()  # makes sure labels fit in the frame
plt.savefig('average_hotel_prices.png')
plt.show()