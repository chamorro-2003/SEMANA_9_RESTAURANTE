from typing import Tuple, Dict, Callable
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

# TUPLA (tuple): Estructura estable e inmutable para las opciones del menú
OPCIONES_MENU: Tuple[str, ...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías",
    "9. Salir",
)

# Instancia del servicio que centraliza la administración
servicio: Restaurante = Restaurante()


def ejecutar_registrar_producto() -> None:
    print("\n--- Registrar Producto ---")
    cod: str = input("Código único: ").strip()
    if not cod:
        print("[¡Error!]: El código no puede estar vacío.")
        return
    nom: str = input("Nombre: ").strip()
    cat: str = input("Categoría: ").strip()

    try:
        prec: float = float(input("Precio ($): "))
        if prec <= 0:
            print("[¡Error!]: El precio debe ser mayor a cero.")
            return
    except ValueError:
        print("[¡Error!]: Debe ingresar un valor numérico para el precio.")
        return

    prod: Producto = Producto(cod, nom, cat, prec)
    if servicio.registrar_producto(prod):
        print("¡Producto registrado con éxito!")
    else:
        print(f"[¡Error!]: Ya existe un producto con el código '{cod}'.")


def ejecutar_buscar_producto() -> None:
    print("\n--- Buscar Producto ---")
    cod: str = input("Ingrese el código a buscar: ").strip()
    prod = servicio.buscar_producto_por_codigo(cod)
    if prod:
        print("\nProducto encontrado:")
        print(prod.mostrar_informacion())
    else:
        print(f"[¡Aviso!]: No se encontró ningún producto con el código '{cod}'.")


def ejecutar_actualizar_producto() -> None:
    print("\n--- Actualizar Producto ---")
    cod: str = input("Ingrese el código del producto a actualizar: ").strip()
    prod = servicio.buscar_producto_por_codigo(cod)
    if not prod:
        print(f"[¡Aviso!]: No existe un producto con el código '{cod}'.")
        return

    print(f"Producto actual: {prod.mostrar_informacion()}")
    nuevo_nom: str = (
        input("Nuevo nombre (presione Enter para conservar): ").strip() or prod.nombre
    )
    nueva_cat: str = (
        input("Nueva categoría (presione Enter para conservar): ").strip()
        or prod.categoria
    )

    precio_input = input("Nuevo precio ($) (presione Enter para conservar): ").strip()
    try:
        nuevo_prec: float = float(precio_input) if precio_input else prod.precio
        if nuevo_prec <= 0:
            print("[¡Error!]: El precio debe ser un número positivo.")
            return
    except ValueError:
        print("[¡Error!]: Formato de precio inválido.")
        return

    if servicio.actualizar_producto(cod, nuevo_nom, nueva_cat, nuevo_prec):
        print("¡Producto actualizado correctamente!")


def ejecutar_eliminar_producto() -> None:
    print("\n--- Eliminar Producto ---")
    cod: str = input("Ingrese el código del producto a eliminar: ").strip()
    if servicio.eliminar_producto(cod):
        print("¡Producto eliminado con éxito!")
    else:
        print(f"[¡Aviso!]: No se encontró el producto con el código '{cod}'.")


def ejecutar_listar_productos() -> None:
    print("\n--- Lista de Productos ---")
    productos = servicio.listar_productos()
    if not productos:
        print("No hay productos registrados en el sistema.")
    else:
        for p in productos:
            print(p.mostrar_informacion())


def ejecutar_registrar_usuario() -> None:
    print("\n--- Registrar Usuario ---")
    ident: str = input("Identificación / Cédula: ").strip()
    if not ident:
        print("[¡Error!]: La identificación es obligatoria.")
        return
    nom: str = input("Nombre completo: ").strip()
    correo: str = input("Correo electrónico: ").strip()

    usr: Usuario = Usuario(ident, nom, correo)
    if servicio.registrar_usuario(usr):
        print("¡Usuario registrado con éxito!")
    else:
        print(f"[¡Error!]: Ya existe un usuario con la identificación '{ident}'.")


def ejecutar_listar_usuarios() -> None:
    print("\n--- Lista de Usuarios ---")
    usuarios = servicio.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for u in usuarios:
            print(u.mostrar_informacion())


def ejecutar_mostrar_categorias() -> None:
    print("\n--- Categorías Registradas ---")
    categorias = servicio.obtener_categorias_unicas()
    if not categorias:
        print("No existen categorías registradas.")
    else:
        print("Categorías únicas disponibles:")
        for c in categorias:
            print(f" • {c}")


def main() -> None:
    # Mapa de acciones: Diccionario que asocia cada opción del menú con su función correspondiente
    mapa_acciones: Dict[str, Callable[[], None]] = {
        "1": ejecutar_registrar_producto,
        "2": ejecutar_buscar_producto,
        "3": ejecutar_actualizar_producto,
        "4": ejecutar_eliminar_producto,
        "5": ejecutar_listar_productos,
        "6": ejecutar_registrar_usuario,
        "7": ejecutar_listar_usuarios,
        "8": ejecutar_mostrar_categorias,
    }

    while True:
        print("\n" + "=" * 40)
        print("        SISTEMA DE RESTAURANTE")
        print("=" * 40)
        for op in OPCIONES_MENU:
            print(op)
        print("=" * 40)

        opcion: str = input("Seleccione una opción (1-9): ").strip()

        if opcion == "9":
            print("\n¡Gracias por utilizar el sistema! Hasta pronto.")
            break
        elif opcion in mapa_acciones:
            mapa_acciones[opcion]()
        else:
            print("[Error]: Opción inválida. Ingrese un número entre 1 y 9.")


if __name__ == "__main__":
    main()
