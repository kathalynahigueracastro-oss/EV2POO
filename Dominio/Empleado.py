from datetime import date
from Dominio.Departamento import Departamento 

class Empleado:
    def __init__(self, id_empleado: int, nombre: str, correo: str, direccion: str, contrasena: str, rol: str, fecha_contrato: date, telefono: str, salario: int, departamento: Departamento) -> None:
        self._id_empleado = id
        self._nombre = nombre
        self._correo = correo
        self._direccion = direccion
        self._contrasena = contrasena
        self._rol = rol 
        self._fecha_contrato = fecha_contrato
        self._telefono = telefono
        self._salario = salario
        self._departamento = departamento

    #Getters

    def obtener_id_empleado(self) -> str:
        return self._id_empleado
    
    def obtener_nombre(self) -> str:
        return self._nombre
    
    def obtener_correo(self) -> str:
        return self._correo
    
    def obtener_direccion(self) -> str:
        return self._direccion
    
    def obtener_contrasena(self) -> str:
        return self._contrasena
    
    def obtener_rol(self) -> str:
        return self._rol
    
    def obtener_fecha_contrato(self) -> date:
        return self._fecha_contrato
    
    def obtener_telefono(self) -> str:
        return self._telefono
    
    def obtener_salario(self) -> int:
        return self._salario
    
    def obtener_departamento(self) -> Departamento:
        return self._departamento
    
    #Setters
      
    def colocar_id_empleado(self, id_empleado: int) -> None:
        self._id_empleado = id_empleado
    
    def colocar_nombre(self, nombre: str) -> None:
        self._nombre = nombre
    
    def colocar_correo(self, correo: str) -> None:
        self._correo = correo
    
    def colocar_direccion(self, direccion: str) -> None:
        self._direccion = direccion
    
    def colocar_contrasena(self, contrasena: str) -> None:
        self._contrasena = contrasena
    
    def colocar_rol(self, rol: str) -> None:
        self._rol = rol
    
    def colocar_fecha_contrato(self, fecha_contrato: date) -> None:
        self._fecha_contrato = fecha_contraro 

    def colocar_telefono(self, telefono: str) -> None:
        self._telefono = telefono 

    def colocar_salario(self, salario: int) -> None:
        self._salario = salario 
    
    def colocar_departamento(self, departamento: Departamento) -> None:
        self._departamento = departamento 
        
    