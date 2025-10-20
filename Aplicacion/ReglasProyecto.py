from Dominio.Proyecto import Proyecto
from Persistencia.ProyectoDAO import ProyectoDao
from Reglas import validar_proyecto, validar_id, validar_nombre, validar_descripcion, validar_fecha
from datetime import date

class ReglasProyecto:
    def __init__(self):
        self.dao = ProyectoDao()

    def crear_proyecto(self, id_proyecto: int, nombre: str, descripcion: str, fecha_inicio: date, fecha_fin: date, presupuesto: float):
        """ Lo que hace: Crea un nuevo proyecto después de validar los datos.
            Parámetros:
            - id_proy: ID del proyecto.
            - nombre: Nombre del proyecto.
            - descripcion: Descripción del proyecto.
            - fecha_inicio: Fecha de inicio del proyecto.
            - fecha_termino: Fecha de término del proyecto.
            - presupuesto: Presupuesto del proyecto.
            Retorna: Mensaje de éxito o error.
            """
        try:
            proyecto = Proyecto(id_proyecto=id_proyecto, nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, presupuesto=presupuesto)
            validar_proyecto(proyecto)
            self.dao.agregar_proyecto(proyecto)
            return f"Proyecto '{nombre}' agregado exitosamente."
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al crear proyecto: {e}"

    def buscar_por_codigo(self, id_proyecto: int):
        """ Lo que hace: Busca un proyecto por su ID después de validar el ID.
            Parámetros:
            - id_proy: ID del proyecto a buscar.
            Retorna: El proyecto encontrado o un mensaje de error.
            """
        try:
            validar_id(id_proyecto)
            return self.dao.obtener_proyecto_por_id(id_proyecto)
        except ValueError as e:
            return f"Error de validación: {e}"

    def buscar_por_nombre(self, nombre: str):
        """ Lo que hace: Busca un proyecto por su nombre después de validar el nombre.
            Parámetros:
            - nombre: Nombre del proyecto a buscar.
            Retorna: El proyecto encontrado o un mensaje de error.
            """
        try:
            validar_nombre(nombre)
            return self.dao.obtener_proyecto_por_nombre(nombre)
        except ValueError as e:
            return f"Error de validación: {e}"
    
    def eliminar_proyecto(self, id_proyecto: int):
        """ Lo que hace: Elimina un proyecto por su ID después de validar el ID.
            Parámetros:
            - id_proyecto: ID del proyecto a eliminar.
            Retorna: Mensaje de éxito o error.
            """
        try:
            validar_id(id_proyecto)
            self.dao.eliminar_proyecto(id_proyecto)
            return f"Proyecto con ID {id_proyecto}"
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al eliminar proyecto: {e}"
    
    