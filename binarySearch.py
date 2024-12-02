import random
"""
Algoritmo de busqueda binaria. Complejidad O(log n)
El algoritmo de busqueda binaria es un algoritmo de busqueda 
eficiente que se utiliza para encontrar un elemento de una lista 
ordenada de elementos. Funciona comparando el elemento con el valor 
medio del array y descartando la mitad no util del array.
Es necesario que el array este ordenado previamente.
"""

def binarySearch(arr, x):
    low = 0 # Inicializa el límite inferior
    high = len(arr) - 1 # Inicializa el límite superior
    mid = 0 # Inicializa el punto medio

    while low <= high: # Mientras el límite inferior sea menor o igual al límite superior
        mid = (high + low) // 2 # Calcula el punto medio
        if arr[mid] < x: # Si el elemento en el punto medio es menor que x
            low = mid + 1 # El límite inferior es el punto medio + 1
        elif arr[mid] > x: # Si el elemento en el punto medio es mayor que x
            high = mid - 1 # El límite superior es el punto medio - 1
        else:
            return mid
    return -1

# Versión recursiva. Complejidad O(log n)
def binarySearchRecurive(arr, x):
    if len(arr) > 0:
        mid = len(arr) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return mid + binarySearchRecurive(arr[mid:], x)
        else:
            return binarySearchRecurive(arr[:mid], x)
    return -1

# Usamos quicksort para ordenar el array
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
    return quickSort(items_lower) + [pivot] + quickSort(items_greater) 
# Ordena los elementos menores y mayores al pivote   

# Prueba
arr = []
while len(arr) < 10:
    arr.append(random.randint(0, 100))
x = 10
arr = quickSort(arr)
print("Arreglo ordenado: ", arr)
result = binarySearch(arr, x)
if result != -1:
    print("Elemento encontrado en la posicion: ", result)
else:
    print("Elemento no encontrado")