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

### 🔑 Skaffa API-nyckel

För att kunna hämta väderdata behöver du en API-nyckel från [OpenWeatherMap](https://home.openweathermap.org/).

1. Skapa ett konto (gratis)
2. Logga in och skapa en API-nyckel
3. Spara den i en `.env`-fil i projektmappen:

```env
API_KEY=din_api_nyckel

```

## 🧠 Om projektet

Det här projektet är ett automatiserat ETL-flöde byggt i Python. Flödet hämtar väderdata från OpenWeatherMap API, transformerar datan till en ren struktur och sparar den i en lokal SQLite-databas.

Syftet är att visa hur man bygger ett stabilt och återanvändbart ETL-flöde i Python, med fokus på:

Struktur (moduluppdelning: extract, transform, load)

Felhantering och loggning

Automatisering (kan köras schemalagt)

Testbarhet med unittest

🔄 Så hänger det ihop

Extract (hämtning)
extract.py hämtar väderdata via ett API-anrop med hjälp av en API-nyckel från .env.

Transform (rensa/strukturera)
transform.py rensar och omformaterar rådata till ett enklare format.

Load (spara)
load.py sparar den transformerade datan i en SQLite-databas (weather_data.db).

main.py styr hela flödet och loggar varje steg i etl.log.

test_etl.py innehåller tester som verifierar att varje steg fungerar som förväntat.

🧪 Hur man använder projektet

Skapa en .env-fil med din API-nyckel:
```
API_KEY=din_api_nyckel
```

Installera beroenden:
```
pip install python-dotenv requests
```

Kör hela flödet:
```
python main.py
```
Kör tester:
```
python test_etl.py
```

## 👨‍💻 Skapad av

Student på **EC Utbildning / Data Science** (Zakaria)
