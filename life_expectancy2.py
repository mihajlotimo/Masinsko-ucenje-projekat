import pandas 
import numpy
import seaborn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

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


X = df.drop(columns=["Life_expectancy", "Country", "Status"])
y = df["Life_expectancy"].values

#Podela na train i test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=29)


#Funkcija regresije
def linearna_regresija_uci(X, y):
    X_b = numpy.c_[numpy.ones((X.shape[0], 1)), X]
    theta = numpy.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
    return theta

def linearna_regresija_predvidja(X, theta):
    X_b = numpy.c_[numpy.ones((X.shape[0], 1)), X]
    return X_b @ theta


#Treniranje modela
theta = linearna_regresija_uci(X_train.values, y_train)

#Predikcija
y_pred = linearna_regresija_predvidja(X_test.values, theta)


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
model.fit(X_train, y_train)

y_pred_sklearn = model.predict(X_test)

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