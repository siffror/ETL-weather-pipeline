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

```
ETL-weather-pipeline/
├── main.py               # Kör hela ETL-flödet
├── test_etl.py           # Kör automatiska tester
├── .env                  # API-nyckel (exkluderas från GitHub)
├── etl.log               # Loggfil för flödet
├── weather_data.db       # SQLite-databas
├── .gitignore            # Utesluter känsliga filer
├── README.md             # Dokumentation
└── etl_pipeline/
    ├── __init__.py       # Gör mappen till ett paket
    ├── extract.py        # Hämtar väderdata från API
    ├── transform.py      # Rensar/transformerar datan
    └── load.py           # Sparar datan i SQLite
```

---

## ▶️ Så kör du programmet

### 1. Klona repot

```bash
git clone https://github.com/ditt-användarnamn/ETL-weather-pipeline.git
cd ETL-weather-pipeline
```

### 2. Skapa `.env`-fil

```env
API_KEY=din_api_nyckel
```

### 3. Installera beroenden

```bash
pip install python-dotenv requests
```

### 4. Kör ETL-flödet

```bash
python main.py
```

### 5. Kör tester

```bash
python test_etl.py
```

---

## ⏰ Automatisera körning (Windows Task Scheduler)

1. Öppna **Schemaläggaren** i Windows  
2. Klicka **"Skapa uppgift..."**  
3. Gå till fliken **"Åtgärder"** → Klicka **"Ny..."**

Fyll i följande:

- **Program/script:** `python`  
- **Argument:** `main.py`  
- **Starta i:** `C:\Users\Player1\Desktop\ETL-weather-pipeline`  
- **Tidpunkt:** t.ex. varje dag kl 09:00

---

## 🔐 Säkerhet

- Lägg `.env` och `etl.log` i `.gitignore`  
- ✅ Så att API-nycklar aldrig laddas upp till GitHub!

---

## 🧪 Exempel på logg

```
2025-09-01 16:18:08,749 | INFO | ETL-flöde startar...
2025-09-01 16:18:08,807 | INFO | Data hämtad från API.
2025-09-01 16:18:08,807 | INFO | Data transformerad: {...}
2025-09-01 16:18:08,812 | INFO | Data sparad i databasen.
2025-09-01 16:18:08,813 | INFO | ETL-flöde avslutat utan fel.
```

---

## 👨‍💻 Skapad av

Student på **EC Utbildning – Python för Data Science** (Zakaria)

