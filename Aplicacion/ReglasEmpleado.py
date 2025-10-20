from Dominio.Empleado import Empleado
from Persistencia.EmpleadoDAO import EmpleadoDao
from Reglas import validar_empleado, validar_id, validar_nombre, validar_correo, validar_direccion, validar_contrasena, validar_rol

class ReglasEmpleado:
    def __init__(self):
        self.dao = EmpleadoDao()

    def crear_empleado(self, id_emp: int, nombre: str, correo: str, direccion: str, contrasena: str, rol: str):
        """ Lo que hace: Crea un nuevo empleado después de validar los datos.
            Parámetros:
            - id_emp: ID del empleado.
            - nombre: Nombre del empleado.
            - correo: Correo del empleado.
            - direccion: Dirección del empleado.
            - contrasena: Contraseña del empleado.
            - rol: Rol del empleado.
            Retorna: Mensaje de éxito o error.
            """
        try:
            emp = Empleado(id_empleado=id_emp, nombre=nombre, correo=correo, direccion=direccion, contrasena=contrasena, rol=rol)
            validar_empleado(emp) 
            self.dao.agregar_empleado(emp)
            return f"Empleado '{nombre}' agregado exitosamente."
        
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al crear empleado: {e}"

    def modificar_empleado(self, indice: int, id_emp: int, nuevo_valor: str):
        """ Lo que hace: Modifica un empleado existente después de validar los datos.
            Parámetros:
            - indice: Índice del campo a modificar (1 para nombre, 2 para correo, 3 para dirección, 4 para contraseña, 5 para rol).
            - id_emp: ID del empleado a modificar.
            - nuevo_valor: Nuevo valor para el campo.
            Retorna: Mensaje de éxito o error.
            """
        try:
            validar_id(id_emp)
            if indice == 1:
                validar_nombre(nuevo_valor)
            elif indice == 2:
                validar_correo(nuevo_valor)
            elif indice == 3:
                validar_direccion(nuevo_valor)
            elif indice == 4:
                validar_contrasena(nuevo_valor)
            elif indice == 5:
                validar_rol(nuevo_valor)
            else:
                return "Índice inválido."
                
            return self.dao.actualizar_empleado(indice, id_emp, nuevo_valor)
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al modificar: {e}"