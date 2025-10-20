from datetime import date

class Proyecto:
    """ Lo que hace: Representa un proyecto con sus atributos y métodos.
    Parámetros:
    - id_proyecto: ID del proyecto.
    - nombre: Nombre del proyecto.
    - descripcion: Descripción del proyecto.
    - fecha_inicio: Fecha de inicio del proyecto.
    - fecha_fin: Fecha de fin del proyecto.
    - presupuesto: Presupuesto del proyecto.
    Retorna: Una instancia de la clase Proyecto.
    """
    def __init__(self, id_proyecto: int, nombre: str, descripcion: str, fecha_inicio: date, fecha_fin: date, presupuesto: int) -> None:
        self._id_proyecto = id_proyecto
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._presupuesto = presupuesto

    # === Métodos getter ===#
    """ Lo que hace: Obtiene los atributos de las clases. 
        Retorna: Los atributos de la clase.
    """
    
    def obtener_id_proyecto(self):
        return self._id_proyecto

    def obtener_nombre(self):
        return self._nombre

    def obtener_descripcion(self):
        return self._descripcion

    def obtener_fecha_inicio(self):
        return self._fecha_inicio

    def obtener_fecha_fin(self):
        return self._fecha_fin

    def obtener_presupuesto(self):
        return self._presupuesto 


    # === Métodos setter ===#
    """ Lo que hace: Coloca los atributos de las clases.
        Parámetros:
        - id_proyecto: ID del proyecto.
        - nombre: Nombre del proyecto.
        - descripcion: Descripción del proyecto.
        - fecha_inicio: Fecha de inicio del proyecto.
        - fecha_fin: Fecha de fin del proyecto.
        - presupuesto: Presupuesto del proyecto.
    """
    
    def colocar_id_proyecto(self, id_proyecto: int) -> None:
        self._id_proyecto = id_proyecto
        
    def colocar_nombre(self, nombre: str) -> None:
        self._nombre = nombre
        
    def colocar_descripcion(self, descripcion: str) -> None:
        self._descripcion = descripcion
        
    def colocar_fecha_inicio(self, fecha_inicio: date) -> None:
        self._fecha_inicio = fecha_inicio
        
    def colocar_fecha_fin(self, fecha_fin: date) -> None:
        self._fecha_fin = fecha_fin
        
    def colocar_presupuesto(self, presupuesto: float) -> None:
        self._presupuesto = presupuesto
        
