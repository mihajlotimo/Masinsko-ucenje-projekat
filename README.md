# Mašinsko učenje — Projekat: Predviđanje životnog veka

Kratak opis
----------
Ovaj projekat koristi skup podataka Life_Expectancy_Data.csv da prikaže jednostavan tok analize i osnovne linearne regresije u Pythonu. Uključuje:
- čitanje i osnovno čišćenje podataka,
- vizualizaciju (distribucija, scatter plot poređenja),
- implementaciju linearne regresije "iz nule" (normalna jednačina),
- poređenje sa sklearn.linear_model.LinearRegression,
- evaluaciju modela pomoću MSE i R².

Struktura repozitorijuma
------------------------
- `Life_Expectancy_Data.csv` — ulazni skup podataka (staviti u root ili `data/` folder)
- `src/` — (opciono) može sadržati skripte; trenutni glavni skript je primer koji ste poslali
- `notebooks/` — (opciono) Jupyter notebook-ovi za eksperimentisanje
- `requirements.txt` — popis Python zavisnosti
- `README.md` — ovaj fajl

Zahtevi
-------
- Python 3.8+
- Preporučene biblioteke:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn

Možete instalirati zavisnosti lokalno:
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```
Ako nema `requirements.txt`, instalirajte direktno:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

Kako pokrenuti skript
---------------------
1. Postavite fajl `Life_Expectancy_Data.csv` u root repozitorijuma ili u `data/` folder i prilagodite put u skriptu ako treba.
2. Pokrenite Python skript koji ste napisali (npr. `life_expectancy_analysis.py`):
```bash
python life_expectancy_analysis.py
```
Skript:
- učitava CSV,
- čisti nazive kolona (zamena razmaka sa `_`),
- prikazuje osnovne statistike i prvih 5 redova,
- crta histogram distribucije `Life_expectancy`,
- računa korelaciju numeričkih kolona sa `Life_expectancy`,
- uklanja redove sa nedostajućim vrednostima (`dropna()`),
- pravi X (bez `Country`, `Status`, `Life_expectancy`) i y,
- deli podatke na train/test,
- uči lin. regresiju sopstvenom implementacijom (normalna jednačina),
- pravi predikcije i meri MSE i R²,
- upoređuje rezultate sa sklearn-ovom implementacijom,
- crta poređenje predikcija.

Objašnjenje ključnih delova koda
--------------------------------
- Čišćenje kolona:
  - `df.columns = df.columns.str.strip().str.replace(" ", "_")` — olakšava pristup kolonama.
- Obrada nedostajućih vrednosti:
  - Trenutno se koristi `df.dropna()` što uklanja sve redove sa bar jednom NA vrednošću — to može znatno smanjiti skup podataka.
- Model "iz nule":
  - Funkcija koristi normalnu jednačinu: theta = (X_b^T X_b)^(-1) X_b^T y.
  - Ova metoda radi dobro za manje, dobro-posedne matrice, ali može biti numerički nestabilna ako je X^T X singularan.
- Poređenje sa sklearn:
  - Sklearn-ova `LinearRegression()` koristi optimizovane i numerički robusnije metode; očekujte vrlo slične rezultate ako nema numeričkih problema.

Ograničenja i preporuke za poboljšanje
-------------------------------------
- dropna() može izbaciti previše podataka — razmotrite imputaciju (npr. mean/median/knn) ili analizu kolona sa puno nedostataka.
- Skaliranje i normalizacija: neke kolone mogu imati različite skale — isprobajte StandardScaler ili MinMaxScaler.
- Kategorizacija: `Country` i `Status` su kategorizijske kolone — možete ih enkodovati (OneHotEncoder, Target Encoding) ako treba da budu deo X.
- Regularizacija: za bolje opšteenje, koristiti Ridge/Lasso.
- Numerička stabilnost: umesto normalne jednačine, koristiti gradient descent ili sklearn koji su optimizovani za velike i kolinearne setove.
- Validacija: koristiti cross-validation (K-Fold) umesto samo jedne podele train/test.
- Istraživačka analiza (EDA): dublja vizualizacija korelacija, heatmap, outlier detekcija.

Primer dodatnih komandi
-----------------------
Pokretanje Jupyter-a:
```bash
jupyter lab
# ili
jupyter notebook
```
Ako želite sačuvati zavisnosti u `requirements.txt`:
```bash
pip freeze > requirements.txt
```

Doprinos i verzionisanje
------------------------
- Ako želite da doprinesete, napravite fork, novu granu `feature/ime` i pošaljite Pull Request.
- Dodajte opis promena i, po mogućstvu, male testove ili primer pokretanja.

Licenca
-------
Dodajte LICENSE fajl (npr. MIT) ako želite da omogućite drugima da koriste i menjaju kod.

Kontakt
-------
Autor repo-a: @mihajlotimo  
Ako želite, dopunite README sa e‑mail adresom ili linkovima do prezentacije/izveštaja.
