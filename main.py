"""
Punto de entrada del sistema de biblioteca digital.
Aquí se implementa el menú interactivo para probar el sistema.
No contiene lógica de negocio, solo llamadas al servicio.
"""

from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio


def menu():

    biblioteca = BibliotecaServicio()

    while True:

        print("\n====== SISTEMA DE BIBLIOTECA DIGITAL ======")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro por título")
        print("8. Buscar libro por autor")
        print("9. Buscar libro por categoría")
        print("10. Listar libros prestados de un usuario")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ")

        # -------------------------
        # Añadir libro
        # -------------------------
        if opcion == "1":

            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")

            libro = Libro(titulo, autor, categoria, isbn)

            biblioteca.agregar_libro(libro)

        # -------------------------
        # Quitar libro
        # -------------------------
        elif opcion == "2":

            isbn = input("ISBN del libro a eliminar: ")

            biblioteca.quitar_libro(isbn)

        # -------------------------
        # Registrar usuario
        # -------------------------
        elif opcion == "3":

            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")

            usuario = Usuario(nombre, id_usuario)

            biblioteca.registrar_usuario(usuario)

        # -------------------------
        # Dar de baja usuario
        # -------------------------
        elif opcion == "4":

            id_usuario = input("ID del usuario a eliminar: ")

            biblioteca.eliminar_usuario(id_usuario)

        # -------------------------
        # Prestar libro
        # -------------------------
        elif opcion == "5":

            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")

            biblioteca.prestar_libro(id_usuario, isbn)

        # -------------------------
        # Devolver libro
        # -------------------------
        elif opcion == "6":

            id_usuario = input("ID del usuario: ")

            usuario = biblioteca.usuarios.get(id_usuario)

            if usuario:

                if not usuario.libros_prestados:
                    print("El usuario no tiene libros prestados.")
                else:

                    print("\nLibros prestados:")
                    for i, libro in enumerate(usuario.libros_prestados):
                        print(f"{i+1}. {libro}")

                    indice = int(input("Seleccione número del libro a devolver: ")) - 1

                    libro = usuario.libros_prestados[indice]

                    biblioteca.devolver_libro(id_usuario, libro)

            else:
                print("Usuario no encontrado.")

        # -------------------------
        # Buscar por título
        # -------------------------
        elif opcion == "7":

            titulo = input("Título a buscar: ")

            resultados = biblioteca.buscar_por_titulo(titulo)

            if resultados:
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros.")

        # -------------------------
        # Buscar por autor
        # -------------------------
        elif opcion == "8":

            autor = input("Autor a buscar: ")

            resultados = biblioteca.buscar_por_autor(autor)

            if resultados:
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros.")

        # -------------------------
        # Buscar por categoría
        # -------------------------
        elif opcion == "9":

            categoria = input("Categoría a buscar: ")

            resultados = biblioteca.buscar_por_categoria(categoria)

            if resultados:
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros.")

        # -------------------------
        # Listar libros prestados
        # -------------------------
        elif opcion == "10":

            id_usuario = input("ID del usuario: ")

            usuario = biblioteca.usuarios.get(id_usuario)

            if usuario:

                if not usuario.libros_prestados:
                    print("El usuario no tiene libros prestados.")
                else:

                    print("\nLibros prestados:")
                    for libro in usuario.libros_prestados:
                        print(libro)

            else:
                print("Usuario no encontrado.")

        # -------------------------
        # Salir
        # -------------------------
        elif opcion == "0":

            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()