from Dominio.Empleado import Empleado
from Persistencia.EmpleadoDAO import EmpleadoDao
from Reglas import validar_empleado, validar_id, validar_nombre, validar_correo, validar_direccion, validar_contrasena, validar_rol
from 

class ReglasEmpleado:
    def __init__(self):
        self.dao = EmpleadoDao()

    def crear_empleado(self, id_emp: int, nombre: str, correo: str, direccion: str, contrasena: str, rol: str):
        try:
            # Creamos el objeto primero
            emp = Empleado(id_empleado=id_emp, nombre=nombre, correo=correo, direccion=direccion, contrasena=contrasena, rol=rol)
            
            # Validamos el objeto
            validar_empleado(emp) # Esto lanzará ValueError si algo falla
            
            # Si es válido, lo agregamos a la BD
            self.dao.agregar_empleado(emp)
            return f"Empleado '{nombre}' agregado exitosamente."
        
        except ValueError as e:
            return f"Error de validación: {e}"
        except Exception as e:
            return f"Error al crear empleado: {e}"

    def modificar_empleado(self, indice: int, id_emp: int, nuevo_valor: str):
        try:
            # Validar ID
            validar_id(id_emp)
            
            # Validar valor nuevo según el índice
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