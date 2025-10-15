from datetime import date

class Proyecto:
    def __init__(self, id_proyecto: int, nombre: str, descripcion: str, 
                 fecha_inicio: date, fecha_fin: date, presupuesto: float) -> None:
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.presupuesto = presupuesto

    # === Métodos getter ===
    def obtener_id_proyecto(self):
        return self.id_proyecto

    def obtener_nombre(self):
        return self.nombre

    def obtener_descripcion(self):
        return self.descripcion

    def obtener_fecha_inicio(self):
        return self.fecha_inicio

    def obtener_fecha_fin(self):
        return self.fecha_fin

    def obtener_presupuesto(self):
        return self.presupuesto

    # (opcional) método para mostrar datos formateados
    def __str__(self):
        return (f"Proyecto {self.id_proyecto}: {self.nombre}\n"
                f"Descripción: {self.descripcion}\n"
                f"Inicio: {self.fecha_inicio} | Fin: {self.fecha_fin}\n"
                f"Presupuesto: ${self.presupuesto:,.2f}")
