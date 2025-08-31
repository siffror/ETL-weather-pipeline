import os
import sqlite3

def save_to_db(data):
    # Bestäm sökväg till databasen i samma mapp som denna fil
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "..", "weather_data.db")
    db_path = os.path.abspath(db_path)  # Gör sökvägen absolut

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    city TEXT,
                    temperature REAL,
                    humidity INTEGER,
                    description TEXT
                )
            """)
            cursor.execute("""
                INSERT INTO weather (city, temperature, humidity, description)
                VALUES (?, ?, ?, ?)
            """, (
                data["city"],
                data["temperature"],
                data["humidity"],
                data["description"]
            ))
            conn.commit()

        print(f"Databasen sparad i: {db_path}")
    except Exception as e:
        print(f"Fel vid databas-skrivning: {e}")
