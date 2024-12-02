"""
Depth First Search (DFS) algorithm
DFS es un algoritmo de búsqueda no informada 
que se utiliza para recorrer o buscar elementos 
en un grafo o árbol. El algoritmo comienza en un
nodo inicial y explora todos los nodos adyacentes
antes de retroceder. DFS se implementa utilizando
una pila para almacenar los nodos por visitar. 
En cada iteración, se extrae un nodo de la pila y
se marcan los nodos adyacentes no visitados para
ser explorados posteriormente. El algoritmo termina
cuando la pila está vacía o se han visitado todos
los nodos alcanzables desde el nodo inicial.S
"""

def dfs(graph, start):
    visited = set() # Conjunto de nodos visitados
    stack = [start] # Pila de nodos por visitar
    result = [] # Lista para almacenar el orden de visita
    
    while stack: # Mientras la pila no esté vacía
        nodo = stack.pop() 
        if nodo not in visited:
            visited.add(nodo) # Marca el nodo como visitado
            result.append(nodo) # Agrega el nodo al resultado
            # Agrega los nodos adyacentes no visitados
            stack.extend(neighbour for neighbour in reversed(graph[nodo]) if neighbour not in visited)
    return result # Devuelve el orden de visita

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(dfs(graph, 'A')) # Salida: ['A', 'C', 'F', 'E', 'B', 'D']


def dfs_recursive(graph, nodo, visited=None, result=None):
    if visited is None: # Si el conjunto de nodos visitados no está inicializado
        visited = set() # Conjunto de nodos visitados
    if result is None: # Si la lista de resultados no está inicializada
        result = [] # Lista para almacenar el orden de visita
        
    visited.add(nodo) # Marca el nodo como visitado
    result.append(nodo) # Agrega el nodo al resultado
    
    for neighbour in graph[nodo]: # Recorre los nodos adyacentes
        if neighbour not in visited: # Si el nodo no ha sido visitado
            dfs_recursive(graph, neighbour, visited, result) # Llama recursivamente a la función
    return result # Devuelve el orden de visita


# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(dfs_recursive(graph, 'A')) # Salida: ['A', 'B', 'D', 'E', 'F', 'C']


# Busqueda DFS

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs_search_recursive(node, target):
    if not node:
        return False
    if node.value == target:
        return True  # Encontramos el valor
    # Buscamos en el subárbol izquierdo y derecho
    return dfs_search_recursive(node.left, target) or dfs_search_recursive(node.right, target)

# Crear el árbol
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(18)

# Buscar un valor (recursiva)
print("DFS Recursiva: ", dfs_search_recursive(root, 7))  # True
print("DFS Recursiva: ", dfs_search_recursive(root, 20))  # False

# Buscar indice de un valor
def dfs_search_index(node, target, index=0):
    if not node:
        return -1
    if node.value == target:
        return index  # Devuelve el índice del valor
    # Buscamos en el subárbol izquierdo y derecho
    left_index = dfs_search_index(node.left, target, index + 1)
    right_index = dfs_search_index(node.right, target, index + 1)
    return max(left_index, right_index)  # Devuelve el índice máximo




