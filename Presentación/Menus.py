from Dominio.Usuario import Usuario
from Aplicacion.reglas import Reglas
from Persistencia.RepositorioUsuarios import RepositorioUsuarios

repositorio_usuarios = RepositorioUsuarios() 
servicio_reglas = Reglas(repositorio = repositorio_usuarios) 

class log_in():
       

    def __init__(self, servicio_reglas):
        self.servicio = servicio_reglas

    def mostrar_login(self):
        print("\n=== INICIO DE SESIÓN ===")
    correo = input("Ingrese su Correo: ")
    contrasena = input("Ingrese su Contraseña: ")
    usuario_autenticado = self.servicio.iniciar_sesion(correo, contrasena)
    
    if usuario_autenticado:
        print
        (f" Log in Exitoso /n Bienvenido {usuario_autenticado.nombre} ")
    else:
        print(f"Usuario no encontrado")