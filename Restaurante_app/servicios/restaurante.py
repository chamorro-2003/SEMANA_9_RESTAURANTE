from typing import List, Optional, Set
from modelos.producto import Producto
from modelos.usuario import Usuario

# --- Clase de Servicio: Restaurante ---
class Restaurante:
    """Clase de servicio que administra las colecciones y reglas del restaurante."""

    def __init__(self) -> None:
        # Listas internas para almacenar productos y usuarios 
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

    # --- Gestión de Productos ---

    def registrar_producto(self, nuevo_producto: Producto) -> bool:
        """Registra un producto validando la unicidad del código."""
        if self.buscar_producto_por_codigo(nuevo_producto.codigo) is not None:
            return False
        self._productos.append(nuevo_producto)
        return True

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        """Busca y retorna un producto según su código."""
        for prod in self._productos:
            if prod.codigo.lower() == codigo.strip().lower():
                return prod
        return None

    def actualizar_producto(
        self, codigo: str, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float
    ) -> bool:
        """Actualiza los datos de un producto existente."""
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is not None:
            producto.nombre = nuevo_nombre.strip()
            producto.categoria = nueva_categoria.strip()
            producto.precio = nuevo_precio
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto del sistema por su código."""
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is not None:
            self._productos.remove(producto)
            return True
        return False

    def listar_productos(self) -> List[Producto]:
        """Retorna la lista de todos los productos."""
        return self._productos

    # --- Gestión de Usuarios ---

    def registrar_usuario(self, nuevo_usuario: Usuario) -> bool:
        """Registra un usuario validando la unicidad de su identificación."""
        if self.buscar_usuario_por_id(nuevo_usuario.identificacion) is not None:
            return False
        self._usuarios.append(nuevo_usuario)
        return True

    def buscar_usuario_por_id(self, identificacion: str) -> Optional[Usuario]:
        """Busca y retorna un usuario por su identificación."""
        for usr in self._usuarios:
            if usr.identificacion.lower() == identificacion.strip().lower():
                return usr
        return None

    def listar_usuarios(self) -> List[Usuario]:
        """Retorna la lista de usuarios registrados."""
        return self._usuarios

    # --- Funcionalidades Adicionales ---

    def obtener_categorias_unicas(self) -> Set[str]:
        """Extrae un conjunto con las categorías únicas de los productos."""
        return {prod.categoria.title() for prod in self._productos}
