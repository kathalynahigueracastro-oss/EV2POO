from Dominio.Empleado import Empleado
from Persistencia.EmpleadoDAO import EmpleadoDao
from Reglas import validar_empleado, validar_id, validar_nombre, validar_correo, validar_direccion, validar_contrasena, validar_rol
from datetime import date 




class ReglasEmpleado:
    def __init__(self):
        self.dao = EmpleadoDao()

    def agregar_empleado(self, id_empleado: int, nombre: str, correo: str, direccion: str, contrasena: str, rol: str, telefono: str, fecha_contratacion: date, salario: int, id_departamento: int):
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
            empleado = Empleado(id_empleado = id_empleado, nombre=nombre, correo=correo, direccion=direccion, contrasena=contrasena, rol=rol, telefono = telefono, fecha_contratacion = fecha_contratacion, salario = salario, id_departamento = id_departamento)
            validar_empleado(empleado) 
            self.dao.agregar_empleado(empleado)
            return f"Empleado '{nombre}' agregado exitosamente."
        
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al crear empleado: {e}"

    def modificar_empleado(self, indice: int, id_empleado: int, nuevo_valor: str):
        """ Lo que hace: Modifica un empleado existente después de validar los datos.
            Parámetros:
            - indice: Índice del campo a modificar (1 para nombre, 2 para correo, 3 para dirección, 4 para contraseña, 5 para rol).
            - id_emp: ID del empleado a modificar.
            - nuevo_valor: Nuevo valor para el campo.
            Retorna: Mensaje de éxito o error.
            """
        try:
            validar_id(id_empleado)
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
                
            return self.dao.actualizar_empleado(indice, id_empleado, nuevo_valor)
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al modificar: {e}"