# 1.	Empleando Series: Arreglos e índices (2 modalidades)

import numpy as np
from numpy import random

arr = np.array(["Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis"], dtype='U20')

for i in range(len(arr)):
    arr[i] = arr[i] + " Editado"

arr2 = np.array([["Uno", "Dos", "Tres"], [1, 2, 3]])

arr3 = np.array([], dtype='i')

for i in range(0,10):
    arr3 = np.append(arr3, random.randint(100))

print('Arreglo 1:', arr)
print('Arreglo 2:', arr2)
print('Arreglo 3:', arr3)
print('Arreglo 3, los 5 primeros:', arr3[:5])
print('Arreglo 3, los 5 ultimos:', arr3[5:])
print('Arreglo 3, los 2 primeros:', arr3[:2])
print('Arreglo 3, los 2 ultimos:', arr3[2:])
