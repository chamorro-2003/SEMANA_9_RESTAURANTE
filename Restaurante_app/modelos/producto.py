class Producto:
    """Representa un producto general en el restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo.strip()
        self.nombre: str = nombre.strip()
        self.categoria: str = categoria.strip()
        self.precio: float = precio

    def mostrar_informacion(self) -> str:
        """Devuelve una representación legible del producto."""
        return (
            f"[CÓD: {self.codigo}] Producto: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f}"
        )
