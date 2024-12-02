# Algoritmo de ordenación por inserción. Complejidad O(n^2)
import random

def insertionSort(arr):
    n = len(arr) # Tamaño del arreglo
    for i in range(1, n): # Recorre el arreglo
        print("Arreglo: ", arr)
        key = arr[i] # Elemento a comparar
        j = i-1 # Elemento anterior
        while j >= 0 and key < arr[j]: # Mientras la llave sea menor que el elemento anterior
            arr[j+1] = arr[j] # Intercambia los elementos
            j -= 1
        arr[j+1] = key
    return arr

# Arreglo a ordenar aleatorio:
arr = []
while len(arr) < 10:
    arr.append(random.randint(0, 100))

print(insertionSort(arr))