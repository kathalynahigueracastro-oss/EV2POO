from Dominio.Proyecto import Proyecto
from Persistencia.Conexion import Conexion

#Crear instancia clase conexion
cnx = Conexion()

class ProyectoDao:

    @staticmethod
    def agregar_proyecto(proyecto: Proyecto):
        """ Guarda un proyecto en la base de datos """
        query = "INSERT INTO proyecto (Id_Proyecto, Nombre, Descripcion, Fecha_Inicio, Fecha_Fin, Presupuesto) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (
            proyecto.obtener_id_proyecto(),
            proyecto.obtener_nombre(),
            proyecto.obtener_descripcion(),
            proyecto.obtener_fecha_inicio(),
            proyecto.obtener_fecha_fin(),
            proyecto.obtener_presupuesto()
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
    def obtener_proyecto_por_id(id_proyecto):
        """ Obtiene a un proyecto por su id 
        Parámetros:
        id_proyecto: ID del proyecto en la base de datos
        Return:
        Diccionario con los datos del personaje """

        query = "SELECT * FROM proyecto WHERE Id_Proyecto = %s"
        conexion = cnx.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(query, (id_proyecto,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Ocurrió un Error: {e}")
            return None
        finally:
            cnx.cerrar_conexion(conexion)
    
    @staticmethod
    def obtener_proyecto_por_nombre(nombre):
        """ Obtiene a un proyecto por su nombre 
        Parámetros:
        nombre: Nombre del proyecto en la base de datos
        Return:
        Diccionario con los datos del personaje """

        query = "SELECT * FROM proyecto WHERE Nombre = %s"
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
    def eliminar_proyecto(id_proyecto):
        """
        Elimina un proyecto de la base de datos basado en su ID.
    
        Parámetros:
        id_proyecto: ID del proyecto en la base de datos.
        Return:
        Mensaje de éxito o error.
        """
        query = "DELETE FROM proyecto WHERE Id_Proyecto = %s"
        conexion = cnx.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(query, (id_proyecto,))
                conexion.commit()
                return "Proyecto eliminado exitosamente."
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return "Error al eliminar el proyecto."
        finally:
            cnx.cerrar_conexion(conexion)

    @staticmethod
    def mostrar_todos_los_proyectos():
        """Obtiene diccionario con los proyectos
        Parametros: None
        Return: Diccionario con toda la informacion de proyectos"""
        query = "SELECT * FROM proyecto"
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
    def actualizar_proyecto(indice, id_proyecto, nuevo_valor):
        """Actualiza un atributo específico de un proyecto en la base de datos.
        Parámetros:
        indice: Indica el número que corresponde a un atributo.
        id_proyecto: ID del proyecto a actualizar.
        nuevo_valor: Nuevo valor para el atributo seleccionado.
        Return:
        Mensaje de éxito o error.
        """
        # Asegurar que indice sea entero
        try:
            indice = int(indice)
        except ValueError:
            return "El índice debe ser un número."

        # Determinar qué columna actualizar
        if indice == 1:
            query = "UPDATE proyecto SET Nombre = %s WHERE Id_Proyecto = %s"
        elif indice == 2:
            query = "UPDATE proyecto SET Descripcion = %s WHERE Id_Proyecto = %s"
        elif indice == 3:
            query = "UPDATE proyecto SET Fecha_Inicio = %s WHERE Id_Proyecto = %s"
        elif indice == 4:
            query = "UPDATE proyecto SET Fecha_Fin = %s WHERE Id_Proyecto = %s"
        elif indice == 5:
            query = "UPDATE proyecto SET Presupuesto = %s WHERE Id_Proyecto = %s"
        else:
            return "Índice inválido."

        conexion = cnx.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(query, (nuevo_valor, id_proyecto))
            conexion.commit()
            return f"Proyecto {id_proyecto} actualizado exitosamente."
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return "Error al actualizar el proyecto."
        finally:
            cnx.cerrar_conexion(conexion)



    