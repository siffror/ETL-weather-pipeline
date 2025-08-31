import logging
from etl_pipeline.extract import fetch_weather
from etl_pipeline.transform import transform_weather_data
from etl_pipeline.load import save_to_db

# Konfigurera logging
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def main():
    try:
        logging.info("ETL-flöde startar...")

        # Extract
        raw_data = fetch_weather("Stockholm")
        logging.info("Data hämtad.")

        # Transform
        cleaned_data = transform_weather_data(raw_data)
        logging.info("Data transformerad.")

        # Load
        save_to_db(cleaned_data)
        logging.info("Data sparad i databasen.")

        # Visa vilken data som skickas till databasen
        print("Skickar följande data till databasen:", cleaned_data)

        logging.info("ETL-flöde avslutat utan fel.")

    except Exception as e:
        logging.error(f"Fel under ETL-processen: {e}")

if __name__ == "__main__":
    main()
import os
# Ange sökvägen till databasen, t.ex. om den används i save_to_db
db_path = "weather.db"  # Ändra till rätt sökväg om nödvändigt
print(f"Databasen används från: {os.path.abspath(db_path)}")
print(f"Nuvarande arbetskatalog: {os.getcwd()}")