from dataclasses import dataclass

# Listas enlazadas circulares

@dataclass
class Node:
    value: int
    next: 'Node'
    
@dataclass
class CircularLinkedList:
    _size : int
    head: Node
    
    # Constructor de la clase, inicializa la lista enlazada
    def __init__(self) -> None:
        self.size = 0
        self.head = None
    
    # Método para agregar un elemento a la lista enlazada
    def add(self, element: int):
        if self.head is None:
            self.head = Node(element, None)
            self.head.next = self.head
        else:
            currentNode = self.head
            while currentNode.next != self.head:
                currentNode = currentNode.next
            currentNode.next = Node(element, self.head)
        self.size += 1
    
    def add_position(self, position: int, element: int):
        if position == 0:
            self.head = Node(element, self.head)
            currentNode = self.head
            while currentNode.next != self.head:
                currentNode = currentNode.next
            currentNode.next = self.head
        else:
            currentNode = self.head
            for i in range(position-1):
                currentNode = currentNode.next
            currentNode.next = Node(element, currentNode.next)
        self.size += 1
    
    # Método para eliminar un elemento de la lista enlazada
    def delete(self, position: int):
        if position == 0:
            self.head = self.head.next
            currentNode = self.head
            while currentNode.next != self.head:
                currentNode = currentNode.next
            currentNode.next = self.head
        else:
            currentNode = self.head
            for i in range(position-1):
                currentNode = currentNode.next
            currentNode.next = currentNode.next.next
        self.size -= 1
    
    def get(self, position:int) -> int:
        currentNode = self.head
        for i in range(position):
            currentNode = currentNode.next
        return currentNode.value
