from dataclasses import dataclass
"""
Colas son una estructura de datos que se caracterizan 
por ser una lista ordenada de elementos donde se usa 
FIFO (First In First Out) para procesar los elementos. 
Es decir, el primer elemento en entrar es el primero en salir
"""

# Usamos una colección deque para implementar una cola
from collections import deque

cola = deque()
print("Tipo: ", type(cola))

cola = deque(["Pepe", "Juan", "Luis", "Ana", "Diego"])
print(cola)
cola.append("María")
print(cola)
cola.append("Carlos")
print(cola)
cola.popleft()
print(cola)



# Implementación de una cola
@dataclass
class cola:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    # Retorna el primer elemento de la cola
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

# Ejemplo de uso
q = cola()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())  # Salida: 1
print(q.peek())     # Salida: 2
