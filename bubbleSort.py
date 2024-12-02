# Algortimo de ordenamiento burbuja. Complejidad O(n^2)

def bubbleSort(arr):
    n = len(arr) # Tamaño del arreglo
    for i in range(n): # Recorre el arreglo
        print("Arreglo: ", arr)
        for j in range(n-i-1): # Recorre el arreglo - i - 1 veces, 
            #para no comparar elementos ya ordenados
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # Intercambia los elementos
    return arr

arr = [64, 34, 25, 12, 22, 11, 9]
print(bubbleSort(arr))




