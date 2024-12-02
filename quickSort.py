import random
"""
Algoritmo de ordenamiento rápido. Complejidad O(n log n).
Usa el método divide y vencerás para ordenar los elementos.
En promedio, O(n log n), en el peor caso O(n^2).

"""


def quickSort(arr):
    if len(arr) <= 1: # Si el arreglo tiene un elemento o está vacío
        return arr
    else:
        pivot = arr.pop() # Selecciona el último elemento como pivote
        print("Pivote: ", pivot)
    items_greater = [] # Elementos mayores al pivote
    items_lower = [] # Elementos menores al pivote
    for item in arr: # Recorre el arreglo
        if item > pivot: # Si el elemento es mayor que el pivote
            items_greater.append(item) # Lo agrega a la lista de mayores
        else: # Si no
            items_lower.append(item) # Lo agrega a la lista de menores
    return quickSort(items_lower) + [pivot] + quickSort(items_greater) # Ordena los elementos menores y mayores al pivote   

# Arreglo a ordenar aleatorio:
arr = []
while len(arr) < 10:
    arr.append(random.randint(0, 100))

print("Arreglo original: ", arr)

print(quickSort(arr))
