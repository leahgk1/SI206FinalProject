import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def connect_to_db(db_path='hotels.db'):
    """Requirement: Must have a valid SQLite database file.
    Method: Establishes a connection to the SQLite database.
    Effect: Returns a connection object."""
    return sqlite3.connect(db_path)

def get_average_prices_by_city(conn):
    """Requirement: Database must contain a 'hotel_prices' table with 'city' and 'price' columns.
    Method: Executes an SQL query to compute average hotel prices by city.
    Effect: Returns a DataFrame with city and average_price."""
    query = """
    SELECT city, AVG(price) AS average_price
    FROM hotel_prices
    GROUP BY city
    ORDER BY average_price DESC
    """
    return pd.read_sql(query, conn)

def plot_average_prices(df, output_file='average_hotel_prices.png'):
    """Requirement: DataFrame with 'city' and 'average_price' columns.
    Method: Uses matplotlib to create and save a bar chart of average prices by city.
    Effect: Displays and saves the plot as a PNG file."""
    plt.figure(figsize=(12, 6))
    plt.bar(df['city'], df['average_price'])
    plt.xticks(rotation=90)
    plt.xlabel('City')
    plt.ylabel('Average Hotel Price ($)')
    plt.title('Average Hotel Prices by City')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()

def main():
    conn = connect_to_db()
    df_avg_prices = get_average_prices_by_city(conn)
    conn.close()
    plot_average_prices(df_avg_prices)

if __name__ == "__main__":
    main()
