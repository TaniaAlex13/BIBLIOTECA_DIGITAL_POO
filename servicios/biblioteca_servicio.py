"""
Servicio que contiene la lógica de negocio del sistema de biblioteca.
Aquí se gestionan los libros, usuarios, préstamos, devoluciones y búsquedas.
"""

from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:

    def __init__(self):

        # Diccionario de libros disponibles
        # clave: ISBN
        # valor: objeto Libro
        self.libros = {}

        # Diccionario de usuarios registrados
        self.usuarios = {}

        # Conjunto para mantener IDs únicos
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

        # eliminar del catálogo disponible
        del self.libros[isbn]

        print("Libro prestado correctamente.")

    def devolver_libro(self, id_usuario, libro):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]

        usuario.devolver_libro(libro)

        # volver a agregar al catálogo
        self.libros[libro.isbn] = libro

        print("Libro devuelto correctamente.")

    # ---------------------------
    # Búsquedas
    # ---------------------------

    def buscar_por_titulo(self, titulo):

        resultados = []

        for libro in self.libros.values():

            if titulo.lower() in libro.obtener_titulo().lower():
                resultados.append(libro)

        return resultados

    def buscar_por_autor(self, autor):

        resultados = []

        for libro in self.libros.values():

            if autor.lower() in libro.obtener_autor().lower():
                resultados.append(libro)

        return resultados

    def buscar_por_categoria(self, categoria):

        resultados = []

        for libro in self.libros.values():

            if categoria.lower() in libro.categoria.lower():
                resultados.append(libro)

        return resultados

    # ---------------------------
    # Listar catálogo completo
    # ---------------------------

    def listar_libros(self):

        if not self.libros:
            print("No hay libros disponibles en el catálogo.")
            return

        print("\nLibros disponibles en la biblioteca:")

        for libro in self.libros.values():
            print(libro)