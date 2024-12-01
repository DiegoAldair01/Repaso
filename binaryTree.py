from dataclasses import dataclass


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Función para insertar un valor en el árbol
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    # Función recursiva para insertar un valor en el árbol
    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    # Función para buscar un valor en el árbol
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search(current_node.left, value)
        else:
            return self._search(current_node.right, value)

    # Recorrido inorden
    def in_order_traversal(self):
        return self._in_order_traversal(self.root, [])

    def _in_order_traversal(self, current_node, result):
        if current_node is not None:
            self._in_order_traversal(current_node.left, result)
            result.append(current_node.value)
            self._in_order_traversal(current_node.right, result)
        return result

    # Recorrido preorden
    def pre_order_traversal(self):
        return self._pre_order_traversal(self.root, [])

    def _pre_order_traversal(self, current_node, result):
        if current_node is not None:
            result.append(current_node.value)
            self._pre_order_traversal(current_node.left, result)
            self._pre_order_traversal(current_node.right, result)
        return result

    # Recorrido postorden
    def post_order_traversal(self):
        return self._post_order_traversal(self.root, [])

    def _post_order_traversal(self, current_node, result):
        if current_node is not None:
            self._post_order_traversal(current_node.left, result)
            self._post_order_traversal(current_node.right, result)
            result.append(current_node.value)
        return result

    # Función para eliminar un valor del árbol
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, current_node, value):
        if current_node is None:
            return current_node
        if value < current_node.value:
            current_node.left = self._delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete(current_node.right, value)
        else:
            # Caso 1: Nodo hoja
            if current_node.left is None and current_node.right is None:
                return None
            # Caso 2: Nodo con un hijo
            elif current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            # Caso 3: Nodo con dos hijos
            current_node.value = self._min_value(current_node.right)
            current_node.right = self._delete(current_node.right, current_node.value)
        return current_node

    # Función para encontrar el valor mínimo en un subárbol
    def _min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value



    
    
# Ejemplo de uso
# Crear un árbol binario
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(7)


# Buscar valores
print(tree.search(7))  # True
print(tree.search(12)) # False

# Recorridos
print("Inorden:", tree.in_order_traversal())    # [5, 7, 10, 15]
print("Preorden:", tree.pre_order_traversal())  # [10, 5, 7, 15]
print("Postorden:", tree.post_order_traversal())# [7, 5, 15, 10]

# Eliminar un valor
tree.delete(10)
print("Inorden después de eliminar 10:", tree.in_order_traversal())  # [5, 7, 15]
