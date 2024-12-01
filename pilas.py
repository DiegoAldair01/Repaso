from dataclasses import dataclass

"""
Las pilas son una estructura de datos que se 
caracterizan por ser una lista ordenada de elementos
donde se usa LIFO (Last In First Out) para procesar
los elementos. Es decir, el último elemento en entrar
"""

pilas = [1, 2, 3, 4, 5, 6]

print(pilas)

# Agregar un elemento al final de la pila
pilas.append(7)
print(pilas)

# Eliminar el último elemento de la pila
pilas.pop()


# Clase Pila
@dataclass
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

# Ejemplo de uso
s = Stack()
s.push(5)
s.push(10)
print(s.pop())  # Salida: 10
print(s.peek()) # Salida: 5


