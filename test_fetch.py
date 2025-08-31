import sys
import os

# Lägg till sökväg till din mapp
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from etl_pipeline.extract import fetch_weather
import pprint

weather_data = fetch_weather("Stockholm")
pprint.pprint(weather_data)
