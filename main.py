"""
Punto de entrada del sistema.
Aquí solo se ejecuta el programa y se interactúa con el usuario.
No debe existir lógica de negocio.
"""

from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio


def menu():

    biblioteca = BibliotecaServicio()

    while True:

        print("\n--- SISTEMA BIBLIOTECA ---")
        print("1. Añadir libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Buscar libro por título")
        print("5. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":

            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")

            libro = Libro(titulo, autor, categoria, isbn)

            biblioteca.agregar_libro(libro)

        elif opcion == "2":

            nombre = input("Nombre usuario: ")
            id_usuario = input("ID usuario: ")

            usuario = Usuario(nombre, id_usuario)

            biblioteca.registrar_usuario(usuario)

        elif opcion == "3":

            id_usuario = input("ID usuario: ")
            isbn = input("ISBN libro: ")

            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "4":

            titulo = input("Título a buscar: ")

            resultados = biblioteca.buscar_por_titulo(titulo)

            for libro in resultados:
                print(libro)

        elif opcion == "5":

            print("Saliendo...")
            break

        else:

            print("Opción inválida")


if __name__ == "__main__":
    menu()