from db import coleccion_libros
from bson.objectid import ObjectId

#   FUNCIONES CRUD

def agregar_libro(titulo, autor, genero, estado):
    if estado not in ("leído", "no leído"):
        print(" Estado inválido.")
        return
    libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "estado": estado
    }
    result = coleccion_libros.insert_one(libro)
    print(f" Libro agregado con ID: {result.inserted_id}")


def actualizar_libro(id_libro, campo, nuevo_valor):
    try:
        result = coleccion_libros.update_one(
            {"_id": ObjectId(id_libro)},
            {"$set": {campo: nuevo_valor}}
        )
        if result.matched_count == 0:
            print(" No se encontró un libro con ese ID.")
        else:
            print(" Libro actualizado correctamente.")
    except Exception:
        print(" Error: ID inválido.")


def eliminar_libro(id_libro):
    try:
        result = coleccion_libros.delete_one({"_id": ObjectId(id_libro)})
        if result.deleted_count == 0:
            print(" No se encontró un libro con ese ID.")
        else:
            print(" Libro eliminado correctamente.")
    except Exception:
        print(" Error: ID inválido.")


def ver_libros():
    libros = list(coleccion_libros.find())
    if libros:
        print("\n LISTADO DE LIBROS:")
        for libro in libros:
            print(f"[{libro['_id']}] '{libro['titulo']}' - {libro['autor']} | Género: {libro['genero']} | Estado: {libro['estado']}")
    else:
        print(" No hay libros registrados.")


def buscar_libros(campo, valor):
    filtro = {campo: {"$regex": valor, "$options": "i"}}
    libros = list(coleccion_libros.find(filtro))
    if libros:
        print("\n RESULTADOS DE BÚSQUEDA:")
        for libro in libros:
            print(f"[{libro['_id']}] '{libro['titulo']}' - {libro['autor']} | Género: {libro['genero']} | Estado: {libro['estado']}")
    else:
        print(" No se encontraron coincidencias.")



#   MENÚ PRINCIPAL

def menu():
    while True:
        print("\n======  MENÚ BIBLIOTECA ======")
        print("1. Agregar nuevo libro")
        print("2. Actualizar información de un libro")
        print("3. Eliminar libro")
        print("4. Ver listado de libros")
        print("5. Buscar libros")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            estado = input("Estado (leído / no leído): ").lower()
            agregar_libro(titulo, autor, genero, estado)

        elif opcion == "2":
            ver_libros()
            id_libro = input("ID del libro a actualizar: ")
            campo = input("Campo a actualizar (titulo, autor, genero, estado): ").lower()
            nuevo_valor = input("Nuevo valor: ")
            actualizar_libro(id_libro, campo, nuevo_valor)

        elif opcion == "3":
            ver_libros()
            id_libro = input("ID del libro a eliminar: ")
            eliminar_libro(id_libro)

        elif opcion == "4":
            ver_libros()

        elif opcion == "5":
            campo = input("Buscar por (titulo, autor, genero): ").lower()
            valor = input("Valor de búsqueda: ")
            buscar_libros(campo, valor)

        elif opcion == "6":
            print(" Saliendo del programa. ¡Hasta pronto!")
            break

        else:
            print(" Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
