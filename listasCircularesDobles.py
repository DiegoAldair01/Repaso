from dataclasses import dataclass

# Listas enlazadas circulares dobles

@dataclass
class Node:
    value: int
    next: 'Node'
    prev: 'Node'

@dataclass
class CircularDoubleLinkedList:
    _size : int
    head: Node
    
    # Constructor de la clase, inicializa la lista enlazada
    def __init__(self) -> None:
        self.size = 0
        self.head = None
    
    # Método para agregar un elemento a la lista enlazada
    def add(self, position: int, element: int):
        if position == 0:
            self.head = Node(element, self.head, None)
            if self.size == 0:
                self.head.next = self.head
                self.head.prev = self.head
        elif position == self.size:
            self.head.prev.next = Node(element, self.head, self.head.prev)
            self.head.prev = self.head.prev.next
        else:
            currentNode = self.head
            for i in range(position-1):
                currentNode = currentNode.next
            currentNode.next = Node(element, currentNode.next, currentNode)
            currentNode.next.next.prev = currentNode.next
        self.size += 1
        
    # Método para eliminar un elemento de la lista enlazada
    def delete(self, position: int):
        if position == 0:
            self.head = self.head.next
            self.head.prev = self.head.prev.prev
            self.head.prev.next = self.head
        elif position == self.size-1:
            self.head.prev = self.head.prev.prev
            self.head.prev.next = self.head
        else:
            currentNode = self.head
            for i in range(position-1): # Se detiene en el nodo anterior al que se quiere eliminar
                currentNode = currentNode.next
            currentNode.next = currentNode.next.next
            currentNode.next.prev = currentNode
        self.size -= 1
    
    def get(self, position:int) -> int:
        currentNode = self.head
        for i in range(position):
            currentNode = currentNode.next
        return currentNode.value