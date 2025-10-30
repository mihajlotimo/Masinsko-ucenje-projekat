# Predviđanje životnog veka — life_expectancy2.py

Uvod
----
U ovom projektu analiziram skup podataka Life_Expectancy_Data.csv i koristim linearnu regresiju za predviđanje očekivanog životnog veka. Cilj je prikazati ceo tok rada: učitavanje i čišćenje podataka, osnovna vizualizacija, treniranje modela, evaluacija i poređenje moje implementacije sa implementacijom iz scikit‑learna.

Fajlovi u repozitorijumu
------------------------
- `life_expectancy2.py` — glavni Python skript koji izvodi sve korake analize i modeliranja.
- `Life_Expectancy_Data.csv` — dataset koji se koristi u skriptu.
- `README.md` — ovaj fajl.

Kratak opis postupka u skriptu
------------------------------
1. Učitavanje CSV fajla:
   - pandas.read_csv("Life_Expectancy_Data.csv")
2. Čišćenje imena kolona:
   - uklanjanje vodećih/zaostalih razmaka i zamena razmaka sa donjim crticama.
3. Ispis osnovnih informacija:
   - nazivi kolona, prvih 5 redova i deskriptivna statistika.
4. Vizualizacija:
   - histogram distribucije kolone `Life_expectancy`.
5. Korelaciona analiza:
   - računanje korelacija numeričkih kolona sa `Life_expectancy`.
6. Priprema podataka:
   - uklanjanje redova sa nedostajućim vrednostima (`dropna()`),
   - definisanje X (bez `Country`, `Status`, `Life_expectancy`) i y (`Life_expectancy`).
7. Podela podataka:
   - train/test podela (test_size=0.2, random_state=29).
8. Implementacija i treniranje modela:
   - moja implementacija linearne regresije pomoću normalne jednačine,
   - predikcija na test skupu.
9. Evaluacija:
   - izračunavanje MSE i R² za moju implementaciju.
10. Poređenje:
    - treniranje sklearn.linear_model.LinearRegression i upoređivanje metrike (MSE, R²).
11. Vizualni prikazi:
    - scatter plot stvarnih vs predviđenih vrednosti i poređenje moje i sklearn regresije.

Zahtevi i instalacija
----------------------
Potrebno:
- Python 3.8 ili noviji
- biblioteke: pandas, numpy, matplotlib, seaborn, scikit-learn

Preporučeni koraci:
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
Uveriti se da su `life_expectancy2.py` i `Life_Expectancy_Data.csv` u istom folderu (root repozitorijuma), pa pokrenuti:
```bash
python life_expectancy2.py
```
Skript će otvoriti grafike i ispisati metrike (MSE i R²) za moju implementaciju i za sklearn model.

Rezultati
---------
Skripta ispisuje osnovne statistike i korelacije, zatim izlazne metrike (MSE i R²) i crta grafikone koji prikazuju stvarne i predviđene vrednosti za test skup. Detaljni numerički rezultati zavise od sadržaja `Life_Expectancy_Data.csv` i trenutne obrade podataka.

## Rezultati modela

Rezultati moje regresije:
- MSE: 12.413014602718393
- R²: 0.8322967952061454

### Poređenje sa sklearn modelom

Uporedio sam moju implementaciju regresije sa sklearn implementacijom. Rezultati su praktično isti:

Moja implementacija:
- MSE = 12.413014602718393
- R²  = 0.8322967952061454

Sklearn implementacija:
- MSE = 12.413014603039072
- R²  = 0.832296795201813

Zaključak: moja regresija i sklearn regresija daju iste rezultate.

### Poređenje sa Random Forest

Uporedio sam regresiju sa Random Forest modelom. Random Forest postiže znatno bolje rezultate:

Random Forest rezultati:
- MSE = 2.658773272727277
- R²  = 0.9640792496482714

Zaključak: Random Forest model daje bolje performanse (manji MSE i viši R²) u poređenju sa linearnom regresijom koju sam implementirao.


Autor
-----
Mihajlo Timo (korisničko ime: @mihajlotimo)
