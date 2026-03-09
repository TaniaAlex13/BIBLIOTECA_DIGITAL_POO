"""
Servicio que contiene la lógica de negocio del sistema de biblioteca.
"""

from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:

    def __init__(self):
        
        # Diccionario de libros
        # clave: ISBN
        # valor: objeto Libro
        self.libros = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # Conjunto para IDs únicos
        self.ids_usuarios = set()

    # ---------------------------
    # Gestión de libros
    # ---------------------------

    def agregar_libro(self, libro):

        if libro.isbn in self.libros:
            print("El libro ya existe.")
        else:
            self.libros[libro.isbn] = libro
            print("Libro agregado correctamente.")

    def quitar_libro(self, isbn):

        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # ---------------------------
    # Gestión de usuarios
    # ---------------------------

    def registrar_usuario(self, usuario):

        if usuario.id_usuario in self.ids_usuarios:
            print("El usuario ya existe.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado.")

    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # ---------------------------
    # Préstamos
    # ---------------------------

    def prestar_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]

        usuario.prestar_libro(libro)

        del self.libros[isbn]

        print("Libro prestado correctamente.")

    def devolver_libro(self, id_usuario, libro):

        usuario = self.usuarios[id_usuario]

        usuario.devolver_libro(libro)

        self.libros[libro.isbn] = libro

        print("Libro devuelto.")

    # ---------------------------
    # Búsquedas
    # ---------------------------

    def buscar_por_titulo(self, titulo):

        return [l for l in self.libros.values() if l.obtener_titulo().lower() == titulo.lower()]

    def buscar_por_autor(self, autor):

        return [l for l in self.libros.values() if l.obtener_autor().lower() == autor.lower()]

    def buscar_por_categoria(self, categoria):

        return [l for l in self.libros.values() if l.categoria.lower() == categoria.lower()]