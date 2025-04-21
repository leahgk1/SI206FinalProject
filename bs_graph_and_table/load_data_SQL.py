import json
import sqlite3
import pandas as pd

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def flatten_json_to_rows(data):
    """Convert nested city-hotel-price JSON into a flat list of dictionaries."""
    rows = []
    for city, hotels in data.items():
        for hotel_name, price in hotels.items():
            rows.append({'city': city, 'hotel': hotel_name, 'price': price})
    return rows

def create_dataframe(rows):
    """Convert list of dictionaries to a pandas DataFrame."""
    return pd.DataFrame(rows)

def insert_dataframe_to_sqlite(df, db_path, table_name):
    """Insert DataFrame into a SQLite database."""
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    return conn  # Return connection if further use needed

def query_and_print_sample(conn, table_name, limit=5):
    """Query and print a sample of the database table."""
    query = f"SELECT * FROM {table_name} LIMIT {limit};"
    result = pd.read_sql(query, conn)
    print(result)

def main():
    data = load_json('hotel_prices.json')
    rows = flatten_json_to_rows(data)
    df = create_dataframe(rows)
    conn = insert_dataframe_to_sqlite(df, 'hotels.db', 'hotel_prices')
    query_and_print_sample(conn, 'hotel_prices')
    conn.close()

if __name__ == "__main__":
    main()
