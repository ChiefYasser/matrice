import pandas as pd
from sklearn.preprocessing import StandardScaler
# Charger le fichier Excel
df = pd.read_excel("data_tp3.xlsx")
# Afficher les 5 premières lignes
print(df.head())

# Nombre de lignes et colonnes
print(df.shape)

# Noms des colonnes
print(df.columns)

# Types des données
print(df.dtypes)
df_numeric = df.select_dtypes(include=['int64', 'float64'])

print(df_numeric.head())


scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_numeric)

print(X_scaled)

# Moyenne des variables
moyenne = df_numeric.mean()

# Écart-type des variables
ecart_type = df_numeric.std(ddof=0)  # ddof=0 pour ACP

print("Moyenne :")
print(moyenne)

print("\nÉcart-type :")
print(ecart_type)