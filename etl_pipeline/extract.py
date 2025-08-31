# etl_pipeline/extract.py
import requests
import os
from dotenv import load_dotenv

# Ladda .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def fetch_weather(city="Stockholm", units="metric"):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": units
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # Ger fel om API inte svarar OK
    return response.json()
