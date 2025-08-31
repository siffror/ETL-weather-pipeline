from dotenv import load_dotenv
import os

# Ladda miljövariabler från .env-filen
load_dotenv()

# Läs API-nyckeln
api_key = os.getenv("OPENWEATHER_API_KEY")

# Skriv ut den
print(f"Din API-nyckel är: {api_key}")
