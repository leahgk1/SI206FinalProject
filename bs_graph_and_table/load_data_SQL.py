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

def create_filtered_dataframe(rows, db_path, table_name, limit=25):
    """Filter out already-inserted rows and return up to 25 new entries."""
    df_all = pd.DataFrame(rows)
    conn = sqlite3.connect(db_path)
    
    # Ensure table exists
    conn.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        city TEXT,
        hotel TEXT,
        price REAL,
        UNIQUE(city, hotel)
    );
    """)
    
    # Read existing city-hotel combinations
    existing_df = pd.read_sql(f"SELECT city, hotel FROM {table_name};", conn)
    conn.close()

    # Remove duplicates already in database
    if not existing_df.empty:
        df_filtered = df_all.merge(existing_df, on=['city', 'hotel'], how='left', indicator=True)
        df_filtered = df_filtered[df_filtered['_merge'] == 'left_only'].drop(columns=['_merge'])
    else:
        df_filtered = df_all

    return df_filtered.head(limit)

def insert_dataframe_to_sqlite(df, db_path, table_name):
    """Insert DataFrame into a SQLite database using INSERT OR IGNORE."""
    conn = sqlite3.connect(db_path)
    for _, row in df.iterrows():
        conn.execute(f"""
        INSERT OR IGNORE INTO {table_name} (city, hotel, price)
        VALUES (?, ?, ?);
        """, (row['city'], row['hotel'], row['price']))
    conn.commit()
    return conn

def query_and_print_sample(conn, table_name, limit=5):
    """Query and print a sample of the database table."""
    query = f"SELECT * FROM {table_name} LIMIT {limit};"
    result = pd.read_sql(query, conn)
    print(result)

def main():
    data = load_json('hotel_prices.json')
    rows = flatten_json_to_rows(data)
    df_new = create_filtered_dataframe(rows, 'hotels.db', 'hotel_prices', limit=25)
    conn = insert_dataframe_to_sqlite(df_new, 'hotels.db', 'hotel_prices')
    query_and_print_sample(conn, 'hotel_prices')
    conn.close()

if __name__ == "__main__":
    main()
