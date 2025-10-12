import pymysql

class Conexion:
    def __init__(self): 
        """ Administra la conexion con la base de datos, sus atributos son los datos de la base de datos """
        self.host = "localhost"
        self.user = "mydb_user"
        self.password = "ChuW4nn1ng"
        self.base_datos = "mydb"
    
    def obtener_conexion(self):
        try:
            conexion = pymysql.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.base_datos,
                cursorclass = pymysql.cursors.DictCursor
            )
            return conexion
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            raise

    def cerrar_conexion(self, conexion):
        if conexion: #Si la conexion existe, o es True
            conexion.close()