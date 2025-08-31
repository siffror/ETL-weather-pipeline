import os 
from etl_pipeline.extract import fetch_weather
from etl_pipeline.transform import transform_weather_data
from etl_pipeline.load import save_to_db

raw = fetch_weather("Stockholm")
clean = transform_weather_data(raw)
save_to_db(clean)
