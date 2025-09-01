import os
import logging
from etl_pipeline.extract import fetch_weather
from etl_pipeline.transform import transform_weather_data
from etl_pipeline.load import save_to_db

# Konfigurera logging – skapar etl.log i projektmappen
log_path = os.path.join(os.path.dirname(__file__), 'etl.log')

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)


def main():
    try:
        logging.info("ETL-flöde startar...")

        # Extract
        raw_data = fetch_weather("Stockholm")
        logging.info("Data hämtad från API.")

        # Transform
        cleaned_data = transform_weather_data(raw_data)
        logging.info(f"Data transformerad: {cleaned_data}")

        # Load
        save_to_db(cleaned_data)
        logging.info("Data sparad i databasen.")

        print("Skickar följande data till databasen:", cleaned_data)

        logging.info("ETL-flöde avslutat utan fel.")

    except Exception as e:
        logging.error(f"Fel under ETL-processen: {e}")
        print("❌ Ett fel uppstod. Se etl.log för detaljer.")

if __name__ == "__main__":
    main()

    # Extra info (kan ligga kvar för felsökning)
    db_path = "weather.db"  # Ändra om din databas heter annat
    print(f"Databasen används från: {os.path.abspath(db_path)}")
    print(f"Nuvarande arbetskatalog: {os.getcwd()}")

