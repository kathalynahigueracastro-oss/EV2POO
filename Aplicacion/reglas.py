from Dominio.Usuario import Usuario 
from Persistencia.RepositorioUsuarios import RepositorioUsuarios

class Reglas:

    def __init__(self, repositorio: RepositorioUsuarios):
        self.repositorio = repositorio

    def iniciar_sesion(self, correo: str, contrasena: str) -> Usuario:
        usuario_encontrado = self.repositorio.comparar_correo_contrasena(correo, contrasena)
        
        if usuario_encontrado == True:
            return usuario_encontrado
        else:
            return None
    