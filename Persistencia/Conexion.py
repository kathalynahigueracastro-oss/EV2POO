import pymysql

class Conexion:
    def __init__(self): 
        """ Administra la conexion con la base de datos, sus atributos son los datos de la base de datos"""
        self.host = "localhost"
        self.user = "GE_EchoTech_user"
        self.password = "Caiceo$_123"
        self.base_datos = "gestion_empleados_echotech"
    
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
            print(f"Error (Holy): {e}")
            raise

    def cerrar_conexion(self, conexion):
        if conexion: #Si la conexion existe, o es True
            conexion.close()