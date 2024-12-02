# Estructura de datos: Tabla de Hash
# Las tablas de hash son una estructura de datos que 
# permite almacenar elementos en una colección.

# Función hash
# La función hash es una función que toma una clave y
# devuelve un índice en la tabla de hash.

# Colisiones
# Las colisiones ocurren cuando dos claves diferentes
# tienen el mismo valor hash.

# Resolución de colisiones
# Hay varias formas de resolver colisiones:
# - Encadenamiento
# - Direccionamiento abierto
# - Rehashing
# - Doble hash

# Encadenamiento
# En el encadenamiento, cada celda de la tabla de hash
# es una lista enlazada. Cuando hay una colisión, los
# elementos con la misma clave hash se agregan a la lista.

# Implementación de una tabla de hash con encadenamiento en Python
# Creamos una clase HashTable que tiene un método hash
# para calcular el índice de la tabla de hash y un método
# insert para insertar elementos en la tabla.



# Clase HashTable
class HashTable:
    def __init__(self, size):
        self.size = size  # Tamaño de la tabla hash
        self.table = [None] * size  # Lista para almacenar los buckets

    def hash_function(self, key):
        """Genera un índice hash para una clave"""
        return hash(key) % self.size

    def insert(self, key, value):
        """Inserta un nuevo registro (clave, valor)"""
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []  # Crear una lista para encadenamiento si no existe
        # Si la clave ya existe, actualiza el valor
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])  # Agregar la nueva clave-valor

    def search(self, key):
        """Busca un registro por clave"""
        index = self.hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]  # Devuelve el valor asociado
        return None  # Si no se encuentra la clave

    def delete(self, key):
        """Elimina un registro por clave"""
        index = self.hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    self.table[index].remove(pair)
                    return True
        return False  # Si no se encuentra la clave

    def display(self):
        """Muestra el contenido de la tabla hash"""
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Índice {i}: {bucket}")
            else:
                print(f"Índice {i}: Vacío")

    
"""
# Crear una tabla hash con tamaño 10
ht = HashTable(10)

# Insertar registros
ht.insert("U123", {"name": "Daniela", "age": 25, "city": "Monterrey"})
ht.insert("U456", {"name": "Carlos", "age": 30, "city": "Guadalajara"})
ht.insert("U789", {"name": "Mariana", "age": 22, "city": "CDMX"})

# Buscar un registro
print("Buscar U123:", ht.search("U123"))  # {'name': 'Daniela', 'age': 25, 'city': 'Monterrey'}

# Eliminar un registro
ht.delete("U456")
print("Buscar U456:", ht.search("U456"))  # None

# Mostrar la tabla completa
ht.display()
"""

# Crear una tabla con tamaño pequeño para aumentar la probabilidad de colisiones
ht = HashTable(3)

# Insertar registros
ht.insert("U123", {"name": "Daniela", "age": 25, "city": "Monterrey"})
ht.insert("U456", {"name": "Carlos", "age": 30, "city": "Guadalajara"})
ht.insert("U789", {"name": "Mariana", "age": 22, "city": "CDMX"})

# Buscar un registro
print("Buscar U123:", ht.search("U123"))  # {'name': 'Daniela', 'age': 25, 'city': 'Monterrey'}
print("U123 está en el índice:", ht.hash_function("U123"))  # 0
# Mostrar la tabla completa
ht.display()

    