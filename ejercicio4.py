# 4.	Empleando DataFrame: Genere 2 arreglos de 6 elementos de texto con 
# sus respectivos valores numéricos e imprima los datos, agregue el arreglo 
# 2 sobre el arreglo 1 e imprima los datos

import pandas as pd

data = {'Texto': ["Valor 1", "Valor 2", "Valor 3", "Valor 4", "Valor 5", "Valor 6"],
        'Valor': [1, 2, 3, 4, 5, 6]}

data2 = {'Texto': ["Valor 7", "Valor 8", "Valor 9", "Valor 10", "Valor 11", "Valor 12"],
        'Valor': [7, 8, 9, 10, 11, 12]}

df = pd.DataFrame(data)

df2 = pd.DataFrame(data2)

print("Dataframe original 1")
print(df)
print("\nDataframe original 2")
print(df2)

arr3 = pd.concat([df, df2], ignore_index=True)

print("\nDataframe junto:")
print(arr3)
