class Usuario:
    def __init__(self, id: int, nombre: str, correo: str, direccion: str, telefono: str, contrasena: str, rol: str) -> None:
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.contrasena = contrasena
        self.rol = rol 
