from Dominio.Departamento import Departamento
from Persistencia.DepartamentoDAO import DepartamentoDao
from Reglas import validar_departamento, validar_id, validar_nombre

class ReglasDepartamento:
    def __init__(self):
        self.dao = DepartamentoDao()

    def crear_departamento(self, id_depto: int, nombre: str):
        try:
            # Creamos el objeto primero
            depto = Departamento(id_departamento=id_depto, nombre=nombre)
            
            # Validamos el objeto
            validar_departamento(depto) # Esto lanzará ValueError si algo falla
            
            # Si es válido, lo agregamos a la BD
            self.dao.agregar_departamento(depto)
            return f"Departamento '{nombre}' agregado exitosamente."
        
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al crear departamento: {e}"

    def modificar_departamento(self, indice: int, id_depto: int, nuevo_valor: str):
        try:
            # Validar ID
            validar_id(id_depto)
            
            # Validar valor nuevo según el índice
            if indice == 1:
                validar_nombre(nuevo_valor)
            else:
                return "Índice inválido."
                
            return self.dao.actualizar_departamento(indice, id_depto, nuevo_valor)
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al modificar: {e}"

    def eliminar_departamento(self, id_depto: int):
        try:
            validar_id(id_depto)
            return self.dao.eliminar_departamento(id_depto)
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al eliminar: {e}"

    def buscar_por_codigo(self, id_depto: int):
        try:
            validar_id(id_depto)
            return self.dao.obtener_departamento_por_id(id_depto)
        except ValueError as e:
            return f"Error de validación: {e}"

    def buscar_por_nombre(self, nombre: str):
        try:
            validar_nombre(nombre)
            return self.dao.obtener_departamento_por_nombre(nombre)
        except ValueError as e:
            return f"Error de validación: {e}"

    def mostrar_todos(self):
        return self.dao.mostrar_todos_los_departamentos()