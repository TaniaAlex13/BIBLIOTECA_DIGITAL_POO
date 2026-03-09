"""
Modelo que representa a un usuario de la biblioteca.
Utiliza una lista para almacenar los libros prestados.
"""

class Usuario:

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        
        # Lista de libros prestados
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros(self):
        return self.libros_prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"