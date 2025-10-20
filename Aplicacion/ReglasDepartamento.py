from Dominio.Departamento import Departamento
from Persistencia.DepartamentoDAO import DepartamentoDao
from Reglas import validar_departamento, validar_id, validar_nombre

class ReglasDepartamento:
    def __init__(self):
        self.dao = DepartamentoDao()

    def crear_departamento(self, id_departamento: int, nombre: str):
        """ Lo que hace: Crea un nuevo departamento después de validar los datos.
            Parámetros:
            - id_depto: ID del departamento.
            - nombre: Nombre del departamento.
            Retorna: Mensaje de éxito o error.
            """
        try:
            departamento = Departamento(id_departamento=id_departamento, nombre=nombre)
            validar_departamento(departamento) 
            self.dao.agregar_departamento(departamento)
            return f"Departamento '{nombre}' agregado exitosamente."
        
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al crear departamento: {e}"

    def modificar_departamento(self, indice: int, id_departamento: int, nuevo_valor: str):
        """ Lo que hace: Modifica un departamento existente después de validar los datos.
            Parámetros:
            - indice: Índice del campo a modificar (1 para nombre).
            - id_depto: ID del departamento a modificar.
            - nuevo_valor: Nuevo valor para el campo.
            Retorna: Mensaje de éxito o error.
            """
        try:
            validar_id(id_departamento)
            if indice == 1:
                validar_nombre(nuevo_valor)
            else:
                return "Índice inválido."
                
            return self.dao.actualizar_departamento(indice, id_departamento, nuevo_valor)
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al modificar: {e}"

    def eliminar_departamento(self, id_departamento: int):
        """ Lo que hace: Elimina un departamento por su ID después de validar el ID.
            Parámetros:
            - id_depto: ID del departamento a eliminar.
            Retorna: Mensaje de éxito o error.
            """
        try:
            validar_id(id_departamento)
            return self.dao.eliminar_departamento(id_departamento)
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al eliminar: {e}"

    def buscar_por_codigo(self, id_departamento: int):
        """ Lo que hace: Busca un departamento por su ID después de validar el ID.
            Parámetros:
            - id_depto: ID del departamento a buscar.
            Retorna: El departamento encontrado o un mensaje de error.
            """
        try:
            validar_id(id_departamento)
            return self.dao.obtener_departamento_por_id(id_departamento)
        except ValueError as e:
            return f"Error de validación: {e}"

    def buscar_por_nombre(self, nombre: str):
        """ Lo que hace: Busca un departamento por su nombre después de validar el nombre.
            Parámetros:
            - nombre: Nombre del departamento a buscar.
            Retorna: El departamento encontrado o un mensaje de error.
            """
        try:
            validar_nombre(nombre)
            return self.dao.obtener_departamento_por_nombre(nombre)
        except ValueError as e:
            return f"Error de validación: {e}"

    def mostrar_todos(self):
        return self.dao.mostrar_todos_los_departamentos()