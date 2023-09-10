# 2.	Empleando DataFrame: Arreglos

import pandas as pd

data = {'Texto': ["Valor 1", "Valor 2", "Valor 3", "Valor 4", "Valor 5", "Valor 6"],
        'Valor': [1, 2, 3, 4, 5, 6]}


df = pd.DataFrame(data)

print("Dataframe original")

print(df)

print("\nDataframe con columnas cambiadas")

df = df[['Valor', 'Texto']]

print(df)
