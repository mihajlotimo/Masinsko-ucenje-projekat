import pandas 
import numpy
import seaborn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor



#Ucitavanje
df = pandas.read_csv("Life_Expectancy_Data.csv")

#Ciscenje imena kolona
df.columns = df.columns.str.strip().str.replace(" ", "_")

print("Kolone u datasetu:\n", df.columns.tolist())

print("\nPrvih 5 redova:\n", df.head())

#Opis statistike
print("\nStatistika:\n", df.describe())

#Dijagram distribucije zivotnog veka
seaborn.histplot(df["Life_expectancy"], kde=True, bins=30)
plt.title("Distribucija životnog veka")
plt.xlabel("Životni vek")
plt.ylabel("Frekvencija")
plt.show()

#Korelacija sa zivotnim vekom
corr = df.corr(numeric_only=True)["Life_expectancy"].sort_values(ascending=False)
print("\nKorelacija sa životnim vekom:\n", corr)

#Izbacivanje nedostajucih vrednosti
df = df.dropna()

#one hot kodovanje
df = pandas.get_dummies(df, columns=["Country", "Status"], drop_first=True)

X = df.drop(columns=["Life_expectancy"])
y = df["Life_expectancy"].values

#Podela na train i test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=29)

#skaliranje
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test) 


#Funkcija regresije
def linearna_regresija_uci(X, y):
    X_b = numpy.c_[numpy.ones((X.shape[0], 1)), X]
    theta = numpy.linalg.pinv(X_b.T @ X_b) @ X_b.T @ y
    return theta

def linearna_regresija_predvidja(X, theta):
    X_b = numpy.c_[numpy.ones((X.shape[0], 1)), X]
    return X_b @ theta


#Treniranje modela
theta = linearna_regresija_uci(X_train_scaled, y_train)

#Predikcija
y_pred = linearna_regresija_predvidja(X_test_scaled, theta)


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nRezultati modela:")
print("MSE:", mse)
print("R²:", r2)

#Prikaz stvarnih i predvidjenih vrednosti
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Stvarni životni vek")
plt.ylabel("Predviđeni životni vek")
plt.title("Stvarni vs Predviđeni životni vek")
plt.show()




#Sklearn linearna regresija
model = LinearRegression()
model.fit(X_train_scaled, y_train)

y_pred_sklearn = model.predict(X_test_scaled)

mse_sklearn = mean_squared_error(y_test, y_pred_sklearn)
r2_sklearn = r2_score(y_test, y_pred_sklearn)

print("\nPoređenje sa sklearn modelom")
print("Moja implementacija:")
print("MSE =", mse)
print("R²  =", r2)

print("\nSklearn implementacija:")
print("MSE =", mse_sklearn)
print("R²  =", r2_sklearn)

#Grafik poredjenja 
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred + numpy.random.normal(0, 0.3, len(y_pred)), label="Moja regresija", alpha=0.6, color='blue')
plt.scatter(y_test, y_pred_sklearn, label="Sklearn regresija", alpha=0.6, color='red')
plt.xlabel("Stvarni životni vek")
plt.ylabel("Predvidjeni životni vek")
plt.title("Poređenje: Moja vs Sklearn linearna regresija")
plt.legend()
plt.show()



rf_model = RandomForestRegressor(n_estimators=100, random_state=29)
rf_model.fit(X_train_scaled, y_train)

# Predikcija
y_pred_rf = rf_model.predict(X_test_scaled)

# Evaluacija
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print("\nRandom Forest rezultati:")
print("MSE =", mse_rf)
print("R²  =", r2_rf)


plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred_sklearn, label="Linearna regresija", alpha=0.6, color='red')
plt.scatter(y_test, y_pred_rf, label="Random Forest", alpha=0.6, color='green')
plt.xlabel("Stvarni životni vek")
plt.ylabel("Predviđeni životni vek")
plt.title("Poređenje: Linearna vs Random Forest regresija")
plt.legend()
plt.show()








# XGBoost model
X_train_sub, X_val, y_train_sub, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=29)

xgb_model = XGBRegressor(
    n_estimators=3000,
    learning_rate=0.01,
    max_depth=10,
    subsample=0.9,
    colsample_bytree=0.9,
    reg_lambda=1.2,
    reg_alpha=0.2,
    random_state=29
)

xgb_model.fit(X_train, y_train)


# Predikcija
y_pred_xgb = xgb_model.predict(X_test)

# Evaluacija
mse_xgb = mean_squared_error(y_test, y_pred_xgb)
r2_xgb = r2_score(y_test, y_pred_xgb)

print("\nXGBoost rezultati:")
print("MSE =", mse_xgb)
print("R²  =", r2_xgb)

# Poređenje svih modela
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred_sklearn, label="Linearna regresija", alpha=0.6, color='red')
plt.scatter(y_test, y_pred_rf, label="Random Forest", alpha=0.6, color='green')
plt.scatter(y_test, y_pred_xgb, label="XGBoost", alpha=0.6, color='orange')
plt.xlabel("Stvarni životni vek")
plt.ylabel("Predviđeni životni vek")
plt.title("Poređenje: Linearna, Random Forest i XGBoost regresija")
plt.legend()
plt.show()






print("\nPokrećem ablaciju (uklanjam jedan po jedan feature)...")

features = X_train.columns.tolist()
results = []

for f in features:
    # Uklanjanje jednog feature-a
    X_train_ablate = X_train.drop(columns=[f])
    X_test_ablate = X_test.drop(columns=[f])

    # Skaliranje
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_ablate)
    X_test_scaled = scaler.transform(X_test_ablate)

    # Treniranje linearne regresije (tvoja verzija)
    theta = linearna_regresija_uci(X_train_scaled, y_train)
    y_pred_ablate = linearna_regresija_predvidja(X_test_scaled, theta)

    # Evaluacija
    mse_ablate = mean_squared_error(y_test, y_pred_ablate)
    r2_ablate = r2_score(y_test, y_pred_ablate)

    results.append({
        "Feature_removed": f,
        "MSE": mse_ablate,
        "R2": r2_ablate
    })
    print(f"Uklonjen {f:<30} → MSE: {mse_ablate:.3f}, R²: {r2_ablate:.3f}")

# Analiza rezultata
results_df = pandas.DataFrame(results)
results_df["R2_drop"] = r2_sklearn - results_df["R2"]  # pad u R²
results_df = results_df.sort_values("R2_drop", ascending=False)

print("\nTop 10 feature-a po uticaju na tačnost modela:")
print(results_df.head(10))





# Nova analiza ablacije po grupama atributa

print("\nPokrećem grupisanu ablaciju (npr. uklanjam sve Country kolone odjednom)...")

# Definiši grupe kolona koje zajedno čine jedan atribut
groups = {
    "Country": [c for c in X_train.columns if c.startswith("Country_")],
    "Status": [c for c in X_train.columns if c.startswith("Status_")]
}

# Dodaj sve ostale kolone koje nisu deo nijedne grupe
for col in X_train.columns:
    if not any(col in v for v in groups.values()):
        groups[col] = [col]

# Pokreni ablaciju po grupama
group_results = []

for name, cols in groups.items():
    X_train_ablate = X_train.drop(columns=cols)
    X_test_ablate = X_test.drop(columns=cols)

    # Skaliranje
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_ablate)
    X_test_scaled = scaler.transform(X_test_ablate)

    # Treniranje i predviđanje
    theta = linearna_regresija_uci(X_train_scaled, y_train)
    y_pred_ablate = linearna_regresija_predvidja(X_test_scaled, theta)

    # Evaluacija
    mse_ablate = mean_squared_error(y_test, y_pred_ablate)
    r2_ablate = r2_score(y_test, y_pred_ablate)

    r2_drop = r2_sklearn - r2_ablate

    group_results.append({
        "Feature_group_removed": name,
        "MSE": mse_ablate,
        "R2": r2_ablate,
        "R2_drop": r2_drop
    })

    print(f"Uklonjen {name:<20} → MSE: {mse_ablate:.3f}, R² drop: {r2_drop:.4f}")

# Pretvori u DataFrame
group_results_df = pandas.DataFrame(group_results).sort_values("R2_drop", ascending=False)

# Prikaz atributa po uticaju
print("\nAtributi po uticaju na tačnost modela:")
print(group_results_df)

# Crtanje grafikona
plt.figure(figsize=(8,5))
plt.bar(group_results_df["Feature_group_removed"].head(10), group_results_df["R2_drop"].head(10), color="teal")
plt.title("Uticaj atributa na tačnost modela (grupisana ablacija)")
plt.ylabel("Pad R² pri uklanjanju atributa")
plt.xlabel("Atribut")
plt.xticks(rotation=45)
plt.show()
