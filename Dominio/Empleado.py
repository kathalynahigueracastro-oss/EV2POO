class Empleado:
    def __init__(self, id_empleado: int, nombre: str, correo: str, direccion: str, contrasena: str, rol: str) -> None:
        self._id_empleado = id
        self._nombre = nombre
        self._correo = correo
        self._direccion = direccion
        self._contrasena = contrasena
        self._rol = rol 

    #Getters

    def obtener_id_empleado(self) -> str:
        return self._id
    
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

