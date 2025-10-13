from Dominio.Departamento import Departamento 
from Persistencia.Conexion import Conexion  

#Crear instancia clase conexion
cnx = Conexion()

class DepartamentoDao: 
    
    @staticmethod
    def agregar_departamento(departamento: Departamento)
     """guarda un departamento en la base de datos"""
     query = "INSERT INTO departamento (Id_departamento, Nombre) VALUES (%s, %s)"
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
        print(f"Ocurrio un error: {e}")
     finally:
        cnx.cerrar_conexion(conexion) 

       @staticmethod
    def obtener_departamento_id(id_departamento): 
       """Obtiene un departamento por su id
       Parametros: 
       Id_departamento: ID del departamento en la base de datos
       Return: Diccionario con los datos del personaje"""
       query = "SELECT * FROM departamento WHERE Id_departamento = %s"
       conexion = cnx.obtener_conexion()
       try:
           with conexion.cursor() as cursor:
              cursor.execute(query, (id_departamento,))
              return cursor.fetchone()
        except Exception as e: 
          print(f"Ocurrio un error: {e}") 
          return None
       finally:
           cnx.cerrar_conexion(conexion) 

        @staticmethod
    def eliminar_departamento(id_departamento): 
       """Elimina un departamento por su id"""
       query = "DELETE * FROM departamento WHERE Id_departamento = %s"
       with conexion.cursor() as cursor: 
               cursor.execute(query, (id_departamento)) 
               conexion.commit()
               return "Departamento eliminado exitosamente"
       except Exception as e: 
           print(f"Ocurrio un error: {e}")
       
