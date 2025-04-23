import requests
import sqlite3
import time
import os

def setup_database():
    conn = sqlite3.connect('travel_project.db')
    cursor = conn.cursor()
    
    # Create cities table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        country TEXT DEFAULT 'United States'
    )
    ''')
    
    # Create attractions table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS attractions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_id INTEGER,
        name TEXT,
        rating REAL,
        review_count INTEGER,
        category TEXT,
        address TEXT,
        FOREIGN KEY (city_id) REFERENCES cities(id),
        UNIQUE(city_id, name)
    )
    ''')
    
    conn.commit()
    return conn

def get_city_id(conn, city_name):
    cursor = conn.cursor()
    
    # Check if the city exists
    cursor.execute("SELECT id FROM cities WHERE name = ?", (city_name,))
    result = cursor.fetchone()
    
    if result:
        return result[0]
    else:
        # Add the city if it doesn't exist
        cursor.execute("INSERT INTO cities (name) VALUES (?)", (city_name,))
        conn.commit()
        return cursor.lastrowid

def get_attractions_count(conn, city_id):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM attractions WHERE city_id = ?", (city_id,))
    return cursor.fetchone()[0]

def get_city_attractions(city, limit=25, offset=0):
    api_key = "DzE-oei4RJDLRzqWo3m2zxB1e7vP0uX86f7TbacR3caO0VrID2JvCCPeKAMa8BSxDHQKn5q1TwsWt1IMFIrhYR0xFmukU2jtzNZsWghALSyGuYrkpB5Z0cfF9RD_Z3Yx"
    url = "https://api.yelp.com/v3/businesses/search"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Ensure limit is at most 25 per project requirements
    if limit > 25:
        limit = 25
        
    params = {
        "location": city,
        "categories": "landmarks,museums,tours",
        "limit": limit,
        "offset": offset,
        "sort_by": "rating"
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None
    
    data = response.json()
    
    attractions = []
    for business in data.get('businesses', []):
        category = business['categories'][0]['title'] if business.get('categories') else "Unknown"
        address = ", ".join(business.get('location', {}).get('display_address', []))
        
        attractions.append({
            "name": business.get('name', ''),
            "rating": business.get('rating', 0.0),
            "review_count": business.get('review_count', 0),
            "category": category,
            "address": address
        })

    return {
        "city": city,
        "attractions": attractions
    }

def store_attractions(conn, city_name, attractions_data):
    cursor = conn.cursor()
    
    # Get or create city ID
    city_id = get_city_id(conn, city_name)
    
    # Insert attractions
    attractions_added = 0
    for attraction in attractions_data.get('attractions', []):
        try:
            cursor.execute("""
            INSERT INTO attractions (city_id, name, rating, review_count, category, address)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (
                city_id,
                attraction.get('name', ''),
                attraction.get('rating', 0.0),
                attraction.get('review_count', 0),
                attraction.get('category', ''),
                attraction.get('address', '')
            ))
            attractions_added += 1
        except sqlite3.IntegrityError:
            # Skip duplicates
            pass
    
    conn.commit()
    return attractions_added

def collect_city_attractions(city, target_count=100):
    conn = setup_database()
    city_id = get_city_id(conn, city)
    
    # Get current count of attractions
    current_count = get_attractions_count(conn, city_id)
    print(f"Currently have {current_count} attractions for {city}")
    
    # If we already have enough attractions, we're done
    if current_count >= target_count:
        print(f"Already have {current_count} attractions for {city}, which meets the target of {target_count}")
        conn.close()
        return current_count
    
    # Calculate how many more we need
    remaining = target_count - current_count
    offset = current_count
    total_added = 0
    
    # Collect attractions in batches of 25 until we reach the target
    while remaining > 0:
        batch_size = min(25, remaining)
        print(f"Collecting {batch_size} attractions for {city} (offset: {offset})")
        
        attractions_data = get_city_attractions(city, limit=batch_size, offset=offset)
        
        if attractions_data and attractions_data.get('attractions'):
            added = store_attractions(conn, city, attractions_data)
            total_added += added
            remaining -= added
            offset += batch_size
            
            # If we didn't add any attractions in this batch, we're probably out of results
            if added == 0:
                print(f"No new attractions found for {city}")
                break
            
            # Wait a moment to avoid API rate limits
            if remaining > 0:
                time.sleep(1)
        else:
            print(f"No attractions data returned for {city}")
            break
    
    final_count = get_attractions_count(conn, city_id)
    print(f"Finished collecting attractions for {city}. Total count: {final_count}")
    conn.close()
    
    return final_count

if __name__ == "__main__":
    # Get city input from user
    city = input("Enter a city name to collect attractions data: ")
    collect_city_attractions(city) 