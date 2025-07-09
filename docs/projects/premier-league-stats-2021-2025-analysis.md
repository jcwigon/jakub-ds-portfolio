# Premier League Statistics Analysis (2021–2025)

*Date of creation: 2025-06-27*

## Project description

This project presents a comprehensive analysis of data from the English Premier League for the 2021–2025 seasons. The aim was to go through the entire data workflow – from acquisition, through processing and analysis, to visualization of results – using modern programming tools and NoSQL solutions.

**Key components of the project:**

- **NoSQL database:** I used MongoDB to store, efficiently search, and analyze match data. The project also demonstrates how to run queries on a NoSQL database and perform data analysis directly in MongoDB.
- **Python modules and classes:** The codebase is structured as modular Python files and classes, ensuring a clear and easily expandable program architecture.
- **Data acquisition (Open Data):** Match results and statistics were sourced from open data repositories.
- **Data analysis in Pandas:** I performed data exploration, aggregation, and statistical calculations using the Pandas library.
- **Data visualization:** Key findings and trends are presented as clear and informative charts generated in Python.

Through this project, I demonstrate in practice how to build custom Python modules, define classes, use NoSQL databases, acquire data from open sources, as well as analyze and search a MongoDB database, and present results in a clear visual form.

Additionally, as a football enthusiast, I have prepared interesting analyses that answer questions such as:

- Do referees favor home teams?
- Does home advantage really matter?
- Which teams committed the most fouls in particular seasons?
- Is the Premier League becoming more attacking-oriented each year?
- Based on available data, I have also calculated a simplified, popular in modern football xG (Expected Goals) metric.

## Skills

- **Python**  
- **Pandas**  
- **Matplotlib**  
- **MongoDB**  
- **MkDocs**  
- **Git**  
- **Visual Studio Code**  
- **Open Data**  

## Project structure

The project is organized into several Python modules and scripts, each responsible for a specific part of the analysis workflow:

- **main.py** – Entry point of the project; runs the full data analysis pipeline.
- **analiza.py** – Functions for data exploration and cleaning.
- **statystyki.py** – Computes match and season statistics.
- **wizualizacje.py** – Generates plots and visual summaries.
- **pobieranie.py** – Downloads data from open data sources.
- **mongodb_analiza.py** – Analysis and querying of the MongoDB NoSQL database.
- **mongo_utworz_baze.py** – Script for creating and populating the MongoDB database.
- **requirements.txt** – List of required Python packages.
- **README.md** – Project documentation and setup instructions.
- **.csv files** – Example input datasets.

All modules are well documented, and the code follows a modular structure for clarity and easy maintenance.

## Project Workflow

![Project workflow](imgs/pl_workflow.png)

## Main analysis script

Here is the complete Python script used as the entry point for the project:

```python
# tutaj wklej kod z main.py lub wyeksportowanego notebooka
import os
import numpy as np
import pandas as pd
from analiza import AnalyzerMultiSeason
from statystyki import StatystykiSezonu
from wizualizacje import (
    wykres_srednia_goli,
    wykres_faule_kartki,
    wykres_udzial_wygranych,
    wykres_srednia_strzalow,
    wykres_celnosc,
    wykres_celnosc_druzyn,
    wykres_strzaly_druzyn,
    wykres_gole_druzyn_na_sezon,
    wykres_xg_top10
)

# 📂 Wczytaj dane z folderu
folder_path = "C:/Moje/Python proj"
pliki_csv = [plik for plik in os.listdir(folder_path) if plik.endswith(".csv")]

# 🔄 Wczytaj dane i dodaj kolumnę 'Zwyciezca'
analyzer = AnalyzerMultiSeason(folder_path, pliki_csv)
df_all = analyzer.wczytaj_wszystkie_dane()
analyzer.dodaj_kolumne_zwyciezca()

# 📊 Obiekt klasy z analizami
stat = StatystykiSezonu(df_all)

# === ANALIZY TEKSTOWE ===
print("➡️ Średnia liczba goli w sezonie:")
print(stat.srednia_goli_per_sezon(), "\n")
print("-" * 80)

print("➡️ Średnia liczba fauli i kartek:")
print(stat.analiza_faul_kartki(), "\n")
print("-" * 80)

print("➡️ Udział zwycięstw gospodarzy, remisów i gości:")
print(stat.udzial_wygranych_home_away(), "\n")
print("-" * 80)

print("➡️ Średnia liczba strzałów:")
print(stat.srednia_strzalow(), "\n")
print("-" * 80)

print("➡️ Skuteczność strzałów (gole/strzały):")
print(stat.skutecznosc_strzalow(), "\n")
print("-" * 80)

print("➡️ Strzały i skuteczność drużyn:")
print(stat.statystyki_strzalow_druzyn(), "\n")
print("-" * 80)

print("➡️ Liczba goli strzelonych przez drużyny w każdym sezonie:")
print(stat.gole_druzyn_na_sezon(), "\n")
print("-" * 80)

print("➡️ Uproszczony wskaźnik xG na sezon:")
print(stat.xg_per_season(), "\n")
print("-" * 80)

# === WIZUALIZACJE ===

# 1. Średnia goli na sezon
df_gole = stat.srednia_goli_per_sezon()
wykres_srednia_goli(df_gole)
print("\n" + "="*100 + "\n")

# 2. Faule i kartki
df_faul_kartki = stat.analiza_faul_kartki()
wykres_faule_kartki(df_faul_kartki)
print("\n" + "="*100 + "\n")

# 3. Udział zwycięstw
df_udzial = stat.udzial_wygranych_home_away()
wykres_udzial_wygranych(df_udzial)
print("\n" + "="*100 + "\n")

# 4. Średnia liczba strzałów
df_srednia_strzalow = stat.srednia_strzalow()
lista_strzalow = df_srednia_strzalow["Średnia"].astype(float).tolist()
wykres_srednia_strzalow(lista_strzalow)
print("\n" + "="*100 + "\n")

# 5. Skuteczność strzałów
seria_celnosc = stat.skutecznosc_strzalow()
if isinstance(seria_celnosc, pd.Series):
    lista_celnosc = seria_celnosc.astype(float).tolist()
elif isinstance(seria_celnosc, pd.DataFrame) and "Celność [%]" in seria_celnosc.columns:
    lista_celnosc = seria_celnosc["Celność [%]"].astype(float).tolist()
else:
    raise ValueError("Nieoczekiwany format danych dla skuteczności strzałów.")
wykres_celnosc(lista_celnosc)
print("\n" + "="*100 + "\n")

# 6. Strzały i celność drużyn
df_druzyny_strzaly = stat.statystyki_strzalow_druzyn()
wykres_strzaly_druzyn(df_druzyny_strzaly)
print("\n" + "="*100 + "\n")
wykres_celnosc_druzyn(df_druzyny_strzaly)
print("\n" + "="*100 + "\n")

# 7. Gole drużyn na sezon
df_gole_sezon = stat.gole_druzyn_na_sezon()
wykres_gole_druzyn_na_sezon(df_gole_sezon)
print("\n" + "="*100 + "\n")

# 8. xG
df_xg_szeroko = stat.xg_per_season()
wykres_xg_top10(df_xg_szeroko)
print("\n" + "="*100 + "\n")

