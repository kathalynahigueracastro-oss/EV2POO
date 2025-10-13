from datetime import date

class Proyecto:

    def __init__(self, id_proyecto: int, nombre: str, descripcion: str, fecha_inicio: date, fecha_termino: date) -> None:
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
