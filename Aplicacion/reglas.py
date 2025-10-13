from datetime import date
from Dominio.Empleado import Empleado
from Dominio.Departamento import Departamento
from Dominio.Proyecto import Proyecto
import re

#Validaciones
def _no_vacio(valor,campo):
    """Valida que un campo no esté vacío."""
    if not valor.strip():
        raise ValueError(f"El campo {campo} no puede estar vacío.")
    return valor

def id_valido(id):
    """Valida que el ID sea un número positivo."""
    if not isinstance(id, int) or id <= 0:
        raise ValueError("El ID debe ser un número entero positivo.")
    return id

def _rol_valido(rol):
    """Valida que el rol sea uno de los permitidos."""
    roles_permitidos = ['Supervisor', 'Administrador', 'Empleado']
    if rol not in roles_permitidos:
        raise ValueError(f"El rol {rol} no es válido. Roles permitidos: {', '.join(roles_permitidos)}")
    return rol

def _email_valido(correo):
    """Valida que un correo tenga un formato válido."""
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", str(correo)):
        raise ValueError("Correo con formato inválido.")
    return correo

def _password_valida(contrasena, minimo=6):
    """Valida que una contraseña tenga al menos un número mínimo de caracteres."""
    if contrasena is None or len(contrasena) < minimo:
        raise ValueError(f"La contraseña debe tener al menos {minimo} caracteres.")
    return contrasena

def _fecha_valida(fecha_str):
    """Valida que una fecha tenga el formato correcto (YYYY-MM-DD)."""
    try:
        fecha = date.fromisoformat(fecha_str)
        return fecha
    except ValueError:
        raise ValueError("Fecha con formato inválido. Use YYYY-MM-DD.")
    
def _fecha_inicio_menor_termino(fecha_inicio, fecha_termino):
    """Valida que la fecha de inicio sea anterior a la fecha de término."""
    if fecha_inicio >= fecha_termino:
        raise ValueError("La fecha de inicio debe ser anterior a la fecha de término.")
    return True
   
#Validaciones por entidad  

def validar_empleado(empleado: Empleado) -> Empleado: 
    """Valida los datos de un empleado."""
    empleado.id_empleado = _no_vacio(str(empleado.id_empleado), "ID Empleado")
    empleado.nombre = _no_vacio(empleado.nombre, "Nombre")
    empleado.correo = _no_vacio(empleado.correo, "Correo")
    empleado.direccion = _no_vacio(empleado.direccion, "Dirección")
    empleado.contrasena = _no_vacio(empleado.contrasena, "Contraseña")
    empleado.rol = _rol_valido(empleado.rol)
    return empleado   

def validar_departamento(departamento: Departamento) -> Departamento:
    """Valida los datos de un departamento."""
    departamento.id_departamento = id_valido(departamento.id_departamento)
    departamento.nombre = _no_vacio(departamento.nombre, "Nombre")
    return departamento

def validar_proyecto(proyecto: Proyecto) -> Proyecto:
    """Valida los datos de un proyecto."""
    proyecto.id_proyecto = id_valido(proyecto.id_proyecto)
    proyecto.nombre = _no_vacio(proyecto.nombre, "Nombre")
    proyecto.descripcion = _no_vacio(proyecto.descripcion, "Descripción")
    proyecto.fecha_inicio = _fecha_valida(proyecto.fecha_inicio)
    proyecto.fecha_termino = _fecha_valida(proyecto.fecha_termino)
    _fecha_inicio_menor_termino(proyecto.fecha_inicio, proyecto.fecha_termino)
    return proyecto

def validar_descripcion(descripcion: str) -> str:
    """Valida que una descripción no esté vacía."""
    descripcion = _no_vacio(descripcion, "Descripción")
    return descripcion

def validar_nombre(nombre: str) -> str:
    """Valida que un nombre no esté vacío."""
    nombre = _no_vacio(nombre, "Nombre")
    return nombre

def validar_id(id: int) -> int:
    """Valida que un ID sea un número positivo."""
    id = id_valido(id)
    return id

def validar_rol(rol: str) -> str:
    """Valida que un rol sea uno de los permitidos."""
    rol = _rol_valido(rol)
    return rol

def validar_contrasena(contrasena: str, minimo=6) -> str:
    """Valida que una contraseña tenga al menos un número mínimo de caracteres."""
    contrasena = _no_vacio(contrasena, "Contraseña")
    contrasena = _password_valida(contrasena, minimo)
    return contrasena

def validar_correo(correo: str) -> str:
    """Valida que un correo tenga un formato válido."""
    correo = _no_vacio(correo, "Correo")
    correo = _email_valido(correo)
    return correo

def validar_fecha(fecha_str: str) -> date:
    """Valida que una fecha tenga el formato correcto (YYYY-MM-DD)."""
    fecha = _fecha_valida(fecha_str)
    return fecha

def validar_fechas(fecha_inicio_str: str, fecha_termino_str: str) -> tuple[date, date]:
    """Valida que la fecha de inicio sea anterior a la fecha de término."""
    fecha_inicio = _fecha_valida(fecha_inicio_str)
    fecha_termino = _fecha_valida(fecha_termino_str)
    _fecha_inicio_menor_termino(fecha_inicio, fecha_termino)
    return fecha_inicio, fecha_termino

def validar_direccion(direccion: str) -> str:
    """Valida que una dirección no esté vacía."""
    direccion = _no_vacio(direccion, "Dirección")
    return direccion

def validar_registro_tiempo(horas: float) -> float:
    """Valida que las horas registradas sean un número positivo."""
    if not isinstance(horas, (int, float)) or horas <= 0:
        raise ValueError("Las horas registradas deben ser un número positivo.")
    return horas










