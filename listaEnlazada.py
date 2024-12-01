from dataclasses import dataclass

@dataclass
class Node:
    value: int
    next: 'Node'
    
@dataclass
class LinkedList:
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
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = Node(element, None)
        self.size += 1
    
    def add_position(self, position: int, element: int):
        if position == 0:
            self.head = Node(element, self.head)
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
        else:
            currentNode = self.head
            for i in range(position-1): # Se detiene en el nodo anterior al que se quiere eliminar
                currentNode = currentNode.next
            currentNode.next = currentNode.next.next
        self.size -= 1
        
    def get(self, position:int) -> int:
        currentNode = self.head
        for i in range(position):
            currentNode = currentNode.next
        return currentNode.value
    
    def getSize(self) -> int:
        return self.size



example = LinkedList()

for i in range(100):
    example.add(i)

for i in range(example.getSize()):
    print(example.get(i))


