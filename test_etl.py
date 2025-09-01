import unittest
from etl_pipeline.extract import fetch_weather
from etl_pipeline.transform import transform_weather_data
from etl_pipeline.load import save_to_db

class TestETL(unittest.TestCase):

    def test_fetch_weather(self):
        data = fetch_weather("Stockholm")
        self.assertIn("main", data)
        self.assertIn("weather", data)

    def test_transform_weather_data(self):
        raw = fetch_weather("Stockholm")
        cleaned = transform_weather_data(raw)
        self.assertIn("temperature", cleaned)
        self.assertIn("humidity", cleaned)

    def test_save_to_db(self):
        dummy = {
            "city": "Stockholm",
            "temperature": 20.0,
            "humidity": 50,
            "description": "clear sky"
        }
        try:
            save_to_db(dummy)
        except Exception as e:
            self.fail(f"save_to_db failed: {e}")

if __name__ == '__main__':
    unittest.main()
