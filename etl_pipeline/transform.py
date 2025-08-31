# etl_pipeline/transform.py

def transform_weather_data(raw_data):
    try:
        city = raw_data["name"]
        temperature = raw_data["main"]["temp"]
        humidity = raw_data["main"]["humidity"]
        description = raw_data["weather"][0]["description"]

        return {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "description": description
        }

    except Exception as e:
        print(f"Fel i transformation: {e}")
        return None
