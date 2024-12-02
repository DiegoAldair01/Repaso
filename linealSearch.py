# Algoritmo de busqueda lineal. COMPLEJIDAD O(n)

def linealSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            print("Elemento encontrado en la posicion: ", i)
            return i
    print("Elemento no encontrado")
    return -1


# Prueba
arr = [2, 3, 4, 10, 40]
x = 11
linealSearch(arr, x) # 3
