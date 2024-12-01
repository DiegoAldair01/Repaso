from dataclasses import dataclass

@dataclass
class Node:
    value: int
    next: 'Node'
    prev: 'Node'

@dataclass
class DoubleLinkedList:
    _size : int
    head: Node
    tail: Node
    
    # Constructor de la clase, inicializa la lista enlazada
    def __init__(self) -> None:
        self.size = 0
        self.head = None
        self.tail = None
    
    # Método para agregar un elemento a la lista enlazada
    def add(self, position: int, element: int):
        if position == 0:
            self.head = Node(element, self.head, None)
            if self.size == 0:
                self.tail = self.head
        elif position == self.size:
            self.tail.next = Node(element, None, self.tail)
            self.tail = self.tail.next
        else:
            currentNode = self.head
            for i in range(position-1):
                currentNode = currentNode.next
            currentNode.next = Node(element, currentNode.next, currentNode)
        self.size += 1
        
    # Método para eliminar un elemento de la lista enlazada
    def delete(self, position: int):
        if position == 0:
            self.head = self.head.next
            self.head.prev = None
        elif position == self.size-1:
            self.tail = self.tail.prev
            self.tail.next = None
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
    
