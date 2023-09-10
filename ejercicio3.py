# 3.	Lea el archivo Ventas.csv e imprima los datos
import numpy as np
import pandas as pd
from numpy import genfromtxt

arr = genfromtxt('Ventas.csv', delimiter=';', dtype=str)
print("Usando numpy")
print(arr)

print("\nUsando pandas")
df = pd.read_csv('Ventas.csv' , ';')

print(df)
