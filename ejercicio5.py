    # 5.	Empleando DataFrame: 
    # a.	Genere un arreglo con las ventas del primer trimestre del año e imprima los datos
    # b.	Imprima el numero de registros y el número de campos
    # c.	Genere un arreglo numérico con las ventas del primer trimestre del año, imprima la media, la correlación,
    #       el valor más bajo, el valor más alto, la mediana, la desviación estándar, solo la primera columna del dataset, 
    #       las 2 primeras columnas, primera fila y última columna y los valores de la primera fila	

import numpy as np
import pandas as pd

# Leer el archivo CSV en un DataFrame
df = pd.read_csv('Ventas.csv', ';')

# a. Filtrar las ventas del primer trimestre (enero, febrero y marzo)
primer_trimestre = df[df['Meses'].isin(['Enero', 'Febrero', 'Marzo'])]

# Imprimir los datos del primer trimestre
print("Ventas del primer trimestre del año:")
print(primer_trimestre)

# b. Imprimir el número de registros y el número de campos
num_registros, num_campos = primer_trimestre.shape
print("Número de registros:", num_registros)
print("Número de campos:", num_campos)

# c. Generar un arreglo numérico con las ventas del primer trimestre del año
ventas_np = primer_trimestre['Monto'].to_numpy(dtype=float)

# Imprimir las ventas del primer trimestre como un arreglo NumPy
print("\nVentas del primer trimestre:")
print(ventas_np)

# Calcular la media, correlación, valor mínimo, valor máximo, mediana y desviación estándar
media = np.mean(ventas_np)
correlacion = np.corrcoef(primer_trimestre['Meses'].index, ventas_np)[0, 1]
valor_minimo = np.min(ventas_np)
valor_maximo = np.max(ventas_np)
mediana = np.median(ventas_np)
desviacion_estandar = np.std(ventas_np)

print("\nMedia:", media)
print("Correlacion:", correlacion)
print("Valor minimo:", valor_minimo)
print("Valor maximo:", valor_maximo)
print("Mediana:", mediana)
print("Desviacion estandar:", desviacion_estandar)

# Imprimir solo la primera columna del dataset
print("\nPrimera columna del dataset:")
print(primer_trimestre.iloc[:, 0])

# Imprimir las 2 primeras columnas
print("\nLas 2 primeras columnas:")
print(primer_trimestre.iloc[:, :2])

# Imprimir primera fila
print("\nPrimera fila:")
print(primer_trimestre.iloc[0, :])

# Imprimir última columna
print("\nUltima columna:")
print(primer_trimestre.iloc[:, -1])

# Imprimir los valores de la primera fila como un arreglo NumPy
print("\nValores de la primera fila:")
print(primer_trimestre.iloc[0, :].values)
