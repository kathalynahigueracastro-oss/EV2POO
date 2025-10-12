from Dominio.Usuario import Usuario

class RepositorioUsuarios:
    # Datos de prueba para simular registros de la base de datos
    usuarios = [
        Usuario(1, "suarez.valentinab@ecotech.com", "Valentina", "Calle A", "555-1234", "valen91", "Administrador"),
        Usuario(2, "mariadelcarmen93@ecotech.com", "María", "Calle B", "555-5678", "empleado456", "Empleado")
    ]

    def comparar_correo_contrasena(self, correo, contrasena) -> str:
        for usuario in self.usuarios:
            if usuario.correo == correo and usuario.contrasena == contrasena:
                return usuario
            return None