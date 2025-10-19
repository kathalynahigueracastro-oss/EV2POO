from Dominio.Departamento import Departamento 
from Persistencia.Conexion import Conexion  

#Crear instancia clase conexion
cnx = Conexion()
class DepartamentoDao:
      
    @staticmethod
    def agregar_departamento(departamento: Departamento):
        """ Guarda un departamento en la base de datos """
        query = "INSERT INTO departamento (Id_Departamento, Nombre) VALUES (%s, %s)"
        valores = (
            departamento.obtener_id_departamento(),
            departamento.obtener_nombre()
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
    def obtener_departamento_por_id(id_departamento):
        """ Obtiene a un departamento por su id 
        Parámetros:
        id_departamento: ID del departamento en la base de datos
        Return:
        Diccionario con los datos del personaje """

        query = "SELECT * FROM departamento WHERE Id_Departamento = %s"
        conexion = cnx.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(query, (id_departamento,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Ocurrió un Error: {e}")
            return None
        finally:
            cnx.cerrar_conexion(conexion)
            
    @staticmethod
    def obtener_departamento_por_nombre(nombre):
        """ Obtiene a un departamento por su nombre 
        Parámetros:
        nombre: Nombre del departamento en la base de datos
        Return:
        Diccionario con los datos del personaje """

        query = "SELECT * FROM departamento WHERE Nombre = %s"
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

    @staticmethod
    def eliminar_departamento(id_departamento):
        """
        Eliminar departamento de la base de datos basado en su ID

        Parámetros:
        id_departamento: ID del departamento en la base de datos
        Return:
        Mensaje de exito.
        """
        query = "DELETE FROM departamento WHERE Id_Departamento = %s"
        conexion = cnx.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(query, (id_departamento,))
            conexion.commit()
            return "Departamento eliminado exitosamente."
        except Exception as e:
            print(f"Ocurrió un Error: {e}")
            return "Error al eliminar el departamento."
        finally:
            cnx.cerrar_conexion(conexion)

    @staticmethod
    def mostrar_todos_los_departamentos():
         """Obtiene diccionario con los departamentos"""
         query = "SELECT * FROM departamento"
         conexion = cnx.obtener_conexion()
         try:
             with conexion.cursor() as cursor:
                 cursor.execute(query)
                 return cursor.fetchall()
         except Exception as e:
             print(f"Ocurrió un error: {e}")
         finally:
             cnx.cerrar_conexion(conexion)

    @staticmethod
    def actualizar_departamento(indice, id_departamento, nuevo_valor):  
        """Permite al usuario indicar que atributo desea actualizar y actualizarlo en la base de datos
        Parametros: Indica el numero que corresponde a un atributo
        Id_departamento: indica el departamento que desea actualizar
        Return: None
        """
    
        if indice == 1:
            query = "UPDATE departamento SET Nombre = %s WHERE Id_departamento = %s"
        else: 
            return "Indice invalido" 

        conexion = cnx.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(query, (nuevo_valor, id_departamento))
            conexion.commit()
            return "Departamento actualizado exitosamente."
        except Exception as e:
            print(f"Ocurrió un Error: {e}")
            return "Error al actualizar el departamento."
        finally:
            cnx.cerrar_conexion(conexion)