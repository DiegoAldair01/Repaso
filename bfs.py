from collections import deque
"""
Breadth First Search (BFS) algorithm
"""
def bfs(graph, start):
    visited = set() # Conjunto de nodos visitados
    queue = deque([start]) # Cola de nodos por visitar
    result = [] # Lista para almacenar el orden de visita
    
    while queue: # Mientras la cola no esté vacía
        nodo = queue.popleft() 
        if nodo not in visited:
            visited.add(nodo) # Marca el nodo como visitado
            result.append(nodo) # Agrega el nodo al resultado
            # Agrega los nodos adyacentes no visitados
            queue.extend(neighbour for neighbour in graph[nodo] if neighbour not in visited)
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

print(bfs(graph, 'A')) # Salida: ['A', 'B', 'C', 'D', 'E', 'F']


# Busqueda BFS

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs_search(root, target):
    if not root:
        return False
    queue = deque([root])  # Usamos una cola para almacenar nodos a explorar

    while queue:
        current = queue.popleft()  # Sacamos el nodo del frente de la cola
        if current.value == target:
            return True  # Encontramos el valor

        # Agregamos los hijos a la cola si existen
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return False  # Si recorremos todo y no encontramos el valor

# Crear el árbol
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(18)

# Buscar un valor
print("BFS: ", bfs_search(root, 7))  # True
# Buscar un valor que no existe
print("BFS: ", bfs_search(root, 20))  # False

# Buscar indice de un valor
def bfs_search_index(root, target):
    if not root:
        return -1
    queue = deque([(root, 0)])  # Usamos una cola para almacenar nodos a explorar

    while queue:
        current, index = queue.popleft()  # Sacamos el nodo del frente de la cola
        if current.value == target:
            return index  # Encontramos el valor

        # Agregamos los hijos
        if current.left:
            queue.append((current.left, index * 2 + 1))
        if current.right:
            queue.append((current.right, index * 2 + 2))
            
    return -1  # Si recorremos todo y no encontramos el valor

