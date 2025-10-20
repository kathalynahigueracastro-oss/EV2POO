from Dominio.Empleado import Empleado
from Persistencia.Conexion import Conexion

#Crear instancia clase conexion
cnx = Conexion()

class EmpleadoDao:

    @staticmethod
    def agregar_empleado (empleado:Empleado):
        """ Guarda un empleado en la base de datos """
        query = "INSERT INTO empleado (Id_Empleado, Nombre, Correo, Direccion, Contraseña, Rol, Fecha_contrato, Telefono, Salario, Departamento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (
            empleado.obtener_id_empleado(),
            empleado.obtener_nombre(),
            empleado.obtener_correo(),
            empleado.obtener_direccion(),
            empleado.obtener_contrasena(),
            empleado.obtener_rol(),
            empleado.obtener_fecha_contrato(),
            empleado.obtener_telefono(),
            empleado.obtener_salario(),
            empleado.obtener_departamento().obtener_id_departamento()
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
        
    @staticmethod
    def obtener_empleado_por_nombre(nombre):
        """ Obtiene a un empleado por su nombre 
        Parámetros:
        nombre: Nombre del empleado en la base de datos
        Return:
        Diccionario con los datos del personaje """

        query = "SELECT * FROM empleado WHERE Nombre = %s"
        conexion = cnx.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre,))
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
        Return: Mensaje de exito.
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
    def actualizar_empleado(indice, nuevo_valor, id_empleado):
        """Permite al usuario indicar que atributo desea actualizar y actualizarlo en la base de datos.
        Parametros: 
        Indice: Indica el numero que corresponde a un atributo
        Id_empleado: indica que empleado desea actualizar.
        Return: Mensaje de exito """
        
        if indice == 1:
            query = "UPDATE empleado SET Nombre = %s WHERE Id_empleado= %s"
        elif indice == 2:
            query = "UPDATE empleado SET Correo = %s WHERE Id_empleado = %s"
        elif indice == 3:
            query = "UPDATE proyecto SET Direccion = %s WHERE Id_empleado = %s"
        elif indice == 4:
            query = "UPDATE proyecto SET Contrasena = %s WHERE Id_empleado = %s"
        elif indice == 5:
            query = "UPDATE proyecto SET Rol = %s WHERE Id_empleado = %s"
        elif indice == 6:
            query = "UPDATE proyecto SET Fecha_contrato = %s WHERE Id_empleado = %s"
        elif indice == 7:
            query = "UPDATE proyecto SET Telefono = %s WHERE Id_empleado = %s"
        elif indice == 8:
            query = "UPDATE proyecto SET Salario = %s WHERE Id_empleado = %s"
        elif indice == 9:
            query = "UPDATE proyecto SET Departamento = %s WHERE Id_empleado = %s"
        else:
            return "Indice Invalido"
        
        conexion = cnx.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(query, (nuevo_valor, id_empleado))
            conexion.commit()
            return "Empleado actualizado exitosamente."
        except Exception as e:
            print(f"Ocurrió un Error: {e}")
            return "Error al actualizar el proyecto."
        finally:
            cnx.cerrar_conexion(conexion) 




        
