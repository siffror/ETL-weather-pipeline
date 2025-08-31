import pprint
from etl_pipeline.extract import fetch_weather
from etl_pipeline.transform import transform_weather_data

raw = fetch_weather("Stockholm")
cleaned = transform_weather_data(raw)

pprint.pprint(cleaned)
