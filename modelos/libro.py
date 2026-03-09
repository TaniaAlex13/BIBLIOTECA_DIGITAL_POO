"""
Modelo que representa un libro dentro del sistema de biblioteca.
Se usa una tupla para almacenar el título y el autor.
"""

class Libro:
    
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla inmutable para almacenar título y autor
        self.info = (titulo, autor)
        
        self.categoria = categoria
        self.isbn = isbn

    def obtener_titulo(self):
        return self.info[0]

    def obtener_autor(self):
        return self.info[1]

    def __str__(self):
        return f"Título: {self.obtener_titulo()}, Autor: {self.obtener_autor()}, Categoría: {self.categoria}, ISBN: {self.isbn}"