import random
# Algortimo de ordanamiento por selección. Complejidad O(n^2)

def selectionSort(arr):
    n = len(arr) # Tamaño del arreglo
    for i in range(n): # Recorre el arreglo
        print("Arreglo: ", arr)
        min_idx = i # Índice del elemento mínimo
        for j in range(i+1, n): # Recorre el arreglo desde i+1 hasta n
            if arr[min_idx] > arr[j]: # Si el elemento mínimo es mayor que el elemento actual
                min_idx = j # El elemento mínimo es el actual
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # Intercambia los elementos
    return arr

# Arreglo a ordenar aleatorio:
arr = []
while len(arr) < 10:
    arr.append(random.randint(0, 100))

print(selectionSort(arr))