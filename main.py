import pandas as pd
import numpy as np


file_path = "data_tp3.xlsx"   
X_df = pd.read_excel(file_path)

print("Matrice X :")
print(X_df)
print()


X = X_df.values
n, p = X.shape


mean = np.mean(X, axis=0)
std = np.std(X, axis=0, ddof=1)  

print("Moyenne des variables :")
print(mean)
print()

print("Écart-type des variables :")
print(std)
print()


X_cr = (X - mean) / std

print("Matrice centrée réduite :")
print(X_cr)
print()


R = np.corrcoef(X, rowvar=False)

print("Matrice de corrélation :")
print(R)
print()


coeffs = np.poly(R)

print("Polynôme caractéristique :")
print(coeffs)
print()


valeurs_propres, vecteurs_propres = np.linalg.eig(R)

print("Valeurs propres :")
print(valeurs_propres)
print()


print("Vecteurs propres (colonnes) :")
print(vecteurs_propres)
print()
