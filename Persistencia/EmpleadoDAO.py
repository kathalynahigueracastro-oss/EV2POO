from Dominio.Empleado import Empleado
from Persistencia.Conexion import Conexion

#Crear instancia clase conexion
cnx = Conexion()

class EmpleadoDao:

    @staticmethod
    def agregar_empleado(empleado:Empleado):
        """ Guarda un empleado en la base de datos """
        query = "INSERT INTO empleado (Id_Empleado, Nombre, Correo, Direccion, Contraseña, Rol) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (
            Empleado.obtener_id_empleado(),
            Empleado.obtener_nombre(),
            Empleado.obtener_correo(),
            Empleado.obtener_direccion(),
            Empleado.obtener_contrasena(),
            Empleado.obtener_rol()
        )

        conexion = cnx.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(query, valores)
            conexion.commit()
        except Exception as e:
            print(f"Ocurrió un Error: {e}")
        finally:
            cnx.cerrar_conexion(conexion)

    @staticmethod
    def obtener_empleado_por_id(id_empleado):
        """ Obtiene a un empleado por su id 
        Parámetros:
        id_empleado: ID del empleado en la base de datos
        Return:
        Diccionario con los datos del personaje """

        query = "SELECT * FROM empleado WHERE Id_empleado = %s"
        conexion = cnx.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(query, (id_empleado,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Ocurrió un Error: {e}")
            return None
        finally:
            cnx.cerrar_conexion(conexion)
    
    def eliminar_empleado(id_empleado):
        """
        Eliminar empleado de la base de datos basado en su ID

        Parámetros:
        id_empleado: ID del empleado en la base de datos
        Return:
        Mensaje de exito.
        """

        query = "DELETE FROM empleado WHERE Id_empleado = %s"
        conexion = cnx.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(query, (id_empleado,))
            conexion.commit()
            return "Empleado Eliminado Correctamente"
        except Exception as e:
            print(f"Ocurrió un Error: {e}")
        
    @staticmethod
    def mostrar_todo_empleados():
        """Obtiene diccionario con los empleados
    Parametros: None
    Return: Diccionario con toda la informacion de empleados"""
        query = "SELECT * FROM empleado"
        conexion = cnx.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            print(f"Ocurrió un error: {e}")
        finally:
            cnx.cerrar_conexion()
    
    @staticmethod
    def actualizar_empleado(indice):
        



        
