import pandas as pd

df = pd.read_csv('titanic.csv')

print("==================== Punto 1 =====================\n")
print(df.head())

print("\n==================== Punto 2 =====================\n")
print(df.describe())

print("\n==================== Punto 3 =====================\n")
filtrar = df[(df['Pclass'] == 3) & (df['Sex'] == 'male') & (df['Age'] < 20)]
print(filtrar)

print("\n==================== Punto 4 =====================\n")
print(df.sort_values(by='Age', ascending=True))




