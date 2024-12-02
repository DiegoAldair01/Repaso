import random
"""
Algoritmo de ordenamiento por mezcla. 
Usa el método divide y vencerás para ordenar los elementos. 
Divide el arreglo en dos mitades, ordena las mitades y luego las mezcla.
Complejidad O(n log n) -> División: log n, Mezcla: n
"""

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 # Encuentra el punto medio
        L = arr[:mid] # Divide la lista en dos mitades
        R = arr[mid:]
        print("Arreglo L: ", L)
        print("Arreglo R: ", R)
        mergeSort(L) # Ordena la primera mitad
        mergeSort(R) # Ordena la segunda mitad

        i = j = k = 0 # Índices para recorrer L, R y arr

        # Copia los datos a los arreglos temporales L[] y R[]
        while i < len(L) and j < len(R): # Mientras haya elementos en L y R
            if L[i] < R[j]: # Si el elemento de L es menor que el de R
                arr[k] = L[i] # El elemento de L se copia en arr
                i += 1  # Siguiente elemento de L
            else:   # Si no
                arr[k] = R[j] # El elemento de R es el siguiente
                j += 1 # Siguiente elemento de R
            k += 1 # Siguiente elemento de arr
            print("Arreglo A: ", arr)

        # Verifica si quedaron elementos en L o R para copiar
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            print("Arreglo C: ", arr)

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            print("Arreglo D: ", arr)
    return arr



# Arreglo a ordenar aleatorio:
arr = []
while len(arr) < 10:
    arr.append(random.randint(0, 100))

print(mergeSort(arr))
