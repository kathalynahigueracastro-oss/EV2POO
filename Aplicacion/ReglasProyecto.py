from Dominio.Proyecto import Proyecto
from Persistencia.ProyectoDAO import ProyectoDao
from Reglas import validar_proyecto, validar_id, validar_nombre, validar_descripcion, validar_fecha
from datetime import date

class ReglasProyecto:
    def __init__(self):
        self.dao = ProyectoDao()

    def crear_proyecto(self, id_proy: int, nombre: str, descripcion: str, fecha_inicio: date, fecha_termino: date, presupuesto: float):
        try:
            # Creamos el objeto primero
            proy = Proyecto(id_proyecto=id_proy, nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio, fecha_termino=fecha_termino, presupuesto=presupuesto)
            
            # Validamos el objeto
            validar_proyecto(proy) # Esto lanzará ValueError si algo falla
            
            # Si es válido, lo agregamos a la BD
            self.dao.agregar_proyecto(proy)
            return f"Proyecto '{nombre}' agregado exitosamente."
        
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al crear proyecto: {e}"

    def buscar_por_codigo(self, id_proy: int):
        try:
            validar_id(id_proy)
            return self.dao.obtener_proyecto_por_id(id_proy)
        except ValueError as e:
            return f"Error de validación: {e}"

    def buscar_por_nombre(self, nombre: str):
        try:
            validar_nombre(nombre)
            return self.dao.obtener_proyecto_por_nombre(nombre)
        except ValueError as e:
            return f"Error de validación: {e}"
    
    def eliminar_proyecto(self, id_proyecto: int):
        try:
            validar_id(id_proyecto)
            self.dao.eliminar_proyecto(id_proyecto)
            return f"Proyecto con ID {id_proyecto}"
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al eliminar proyecto: {e}"
    
    