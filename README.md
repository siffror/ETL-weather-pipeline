# ☁️ ETL Weather Pipeline

Ett automatiserat ETL-flöde i Python som hämtar väderdata från OpenWeatherMap, transformerar det och sparar det i en SQLite-databas.

---

## 🔧 Funktioner

- 🔑 Läser API-nyckel från `.env`-fil
- 🌐 Hämtar live-väderdata via OpenWeatherMap API
- 🧹 Transformerar datan till ren form
- 💾 Lagrar väderdata i SQLite-databas
- 🪵 Loggar flödet i `etl.log`
- ✅ Inkluderar automatiska tester med `unittest`

---

## 📂 Projektstruktur



ETL-weather-pipeline/
├── main.py               # Kör hela ETL-flödet
├── test_etl.py           # Kör automatiska tester
├── .env                  # API-nyckel (exkluderas från GitHub)
├── etl.log               # Loggfil för flödet
├── weather_data.db       # SQLite databas
├── README.md             # Dokumentation
├── .gitignore            # Utesluter känsliga filer
└── etl_pipeline/
    ├── __init__.py       # Gör mappen till ett paket
    ├── extract.py        # Hämtar väderdata från API
    ├── transform.py      # Rensar/transformerar datan
    └── load.py           # Sparar datan i SQLite


---

## ▶️ Så kör du programmet

1. Klona repot:
```bash
git clone https://github.com/ditt-användarnamn/ETL-weather-pipeline.git


API_KEY=din_api_nyckel

pip install python-dotenv requests

python main.py

python test_etl.py

Ran 3 tests in X.XXXs
OK


```

⏰ Automatisera körning (Windows Task Scheduler)

Öppna Schemaläggaren i Windows

Klicka "Skapa uppgift..."

Gå till fliken Åtgärder → Klicka "Ny..."

Fyll i:

Program/script:
python

Argument:
main.py

Starta i:
(Sökväg till din projektmapp, t.ex.)
C:\Users\Player1\Desktop\ETL-weather-pipeline

Välj t.ex. att den ska köras varje dag kl 09:00


🔐 Säkerhet

Glöm inte att .env och etl.log ska finnas i .gitignore så att API-nycklar aldrig laddas upp till GitHub!


2025-09-01 16:18:08,749 | INFO | ETL-flöde startar...
2025-09-01 16:18:08,807 | INFO | Data hämtad från API.
2025-09-01 16:18:08,807 | INFO | Data transformerad: {...}
2025-09-01 16:18:08,812 | INFO | Data sparad i databasen.
2025-09-01 16:18:08,813 | INFO | ETL-flöde avslutat utan fel.

👨‍💻 Skapad av

Student på EC Utbildning – Python för Data Science (ZAKARIA)


