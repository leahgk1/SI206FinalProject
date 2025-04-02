import sqlite3

def create_tables():
    conn = sqlite3.connect('travel_project.db')
    cur = conn.cursor()

    # create Cities table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            country TEXT
        )
    ''')

    # create Weather table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_id INTEGER,
            temperature REAL,
            humidity INTEGER,
            description TEXT,
            datetime INTEGER,
            FOREIGN KEY(city_id) REFERENCES Cities(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Tables created!")

if __name__ == "__main__":
    create_tables()
