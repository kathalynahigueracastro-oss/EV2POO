import datetime

class Proyecto:

    def __init__(self, id_proyecto: str, nombre: str, descripcion: str, fecha_inicio: datetime, fecha_termino: datetime) -> None:
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
