class Usuario:
    """Representa la información general de una persona registrada en el sistema."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion.strip()
        self.nombre: str = nombre.strip()
        self.correo: str = correo.strip()

    def mostrar_informacion(self) -> str:
        """Devuelve los datos estructurados del usuario."""
        return (
            f"[ID: {self.identificacion}] Usuario: {self.nombre} | "
            f"Correo: {self.correo}"
        )
