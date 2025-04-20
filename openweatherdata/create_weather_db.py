import sqlite3

def create_tables():
    conn = sqlite3.connect('travel_project.db')
    cur = conn.cursor()

    # create cities table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            country TEXT
        )
    ''')

    # create weather table with formatted_time column
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_id INTEGER,
            temperature REAL,
            humidity INTEGER,
            description TEXT,
            datetime INTEGER,
            formatted_time TEXT,
            FOREIGN KEY(city_id) REFERENCES Cities(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Tables created!")

if __name__ == "__main__":
    create_tables()
