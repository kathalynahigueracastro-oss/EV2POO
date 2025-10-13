from Dominio.Empleado import Empleado
from Persistencia.Conexion import Conexion

#Crear instancia clase conexion
cnx = Conexion()

class EmpleadoDao:
    def agregar_empleado(empleado:Empleado)
    """ Guarda un empleado en la base de datos """
    query = "INSERT INTO empleado (Id_Empleado, Nombre, Correo, Direccion, Contraseña, Rol) VALUES (%s, %s, %s, %s, %s, %s)"