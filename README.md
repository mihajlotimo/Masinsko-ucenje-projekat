# Predviđanje životnog veka — life_expectancy2.py

Kratak opis
----------
Ovaj repo sadrži jednostavan projekat za analizu i predviđanje životnog veka koristeći linearne regresije. Glavni skript `life_expectancy2.py` učitava `Life_Expectancy_Data.csv`, radi osnovno čišćenje podataka, vizualizacije i trenira linearnu regresiju (sopstvena implementacija i poređenje sa sklearn).

Sadržaj repozitorijuma
----------------------
- `life_expectancy2.py` — glavni Python skript
- `Life_Expectancy_Data.csv` — dataset sa podacima o očekivanom životnom veku
- `README.md` — ovaj fajl

Zahtevi
-------
- Python 3.8+
- Biblioteke:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn

Instalacija
----------
Preporučeno je virtuelno okruženje:
```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1

pip install pandas numpy matplotlib seaborn scikit-learn
```

Pokretanje
---------
1. Uveri se da su `life_expectancy2.py` i `Life_Expectancy_Data.csv` u istom folderu repozitorijuma (root), ili prilagodi put do CSV-a u skriptu.
2. Pokreni:
```bash
python life_expectancy2.py
```
Skript će:
- učitati CSV iz `Life_Expectancy_Data.csv` i očistiti nazive kolona (zamena razmaka sa `_`),
- ispisati prve redove i osnovnu statistiku,
- prikazati histogram ciljne varijable (`Life_expectancy`),
- ukloniti redove sa nedostajućim vrednostima (koristi `dropna()`),
- podeliti podatke na train/test,
- učiti linearnu regresiju sopstvenom implementacijom (normalna jednačina),
- porediti rezultate sa sklearn-ovom `LinearRegression`,
- prikazati metrike MSE i R² i nekoliko grafika.

Preporuke i napomene
--------------------
- dropna() može da ukloni veliki broj redova — razmisli o imputaciji ako je to problem.
- Ako je X^T X singularan (kolinearnost), normalna jednačina može biti numerički nestabilna — razmotri Ridge ili sklearn implementaciju.
- Možeš premestiti `Life_Expectancy_Data.csv` u `data/` folder i skriptu postaviti `pandas.read_csv("data/Life_Expectancy_Data.csv")`.
- Dodaj `requirements.txt` komandom `pip freeze > requirements.txt` kad želiš da zamrzneš verzije biblioteka.
- Ako želiš, mogu predložiti male izmene skripta: imputaciju, enkodovanje kategorija, skaliranje i cross-validation.

Kako da ubaciš dataset
----------------------
Ako želiš da dataset bude u repozitorijumu, možeš ga dodati putem GitHub web interfejsa: "Add file" → "Upload files" i izabrati `Life_Expectancy_Data.csv`. Ako želiš da i njega ubacim, potrebno je da mi dostaviš sadržaj CSV-a.

Doprinos
-------
Ako želiš da menjamo fajlove direktno preko GitHub-a, mogu napraviti novu granu sa predloženim promenama i otvoriti PR.

Licenca
-------
Dodaj LICENSE fajl (npr. MIT) ako želiš da drugi koriste kod.

Kontakt
-------
Repo autor: @mihajlotimo
