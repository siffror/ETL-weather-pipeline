# 🌦️ ETL Weather Pipeline

Detta är ett automatiserat ETL-flöde (Extract → Transform → Load) i Python som hämtar väderdata från OpenWeather API och sparar det i en SQLite-databas.

---

## 🚀 Funktioner

- 🔑 Hämtar väderdata från OpenWeatherMap med hjälp av API-nyckel (.env)
- 🧹 Rensar och transformerar datan (t.ex. temperatur, luftfuktighet)
- 🗃️ Sparar datan i en lokal SQLite-databas
- 🪵 Loggning och felhantering
- ✅ Separata testfiler för varje steg

---

## 🗂️ Projektstruktur

etl_pipeline/
├── init.py
├── extract.py # Hämta data från API
├── transform.py # Rensa/transformera data
├── load.py # Spara till SQLite

main.py # Kör hela ETL-flödet
test_env.py # Testar att API-nyckel kan läsas in
test_fetch.py # Testar datahämtning
test_transform.py # Testar datatransformation
test_load.py # Testar att spara till databas


---
API_KEY=din_api_nyckel_här
---
## ⚙️ Krav

- Python 3.10+
- `requests`
- `python-dotenv`

Installera beroenden:

```bash
pip install requests python-dotenv
