from datetime import date
from Dominio.Empleado import Empleado
from Dominio.Departamento import Departamento
from Dominio.Proyecto import Proyecto
import re

#=== Validaciones ===#
def _no_vacio(valor,campo):
    """
    Lo que hace: Revisa que un campo no esté vacío. Usa .strip() para eliminar espacios en blanco.
    Parametros: 
    - valor: El valor a validar.
    - campo: El nombre del campo (para mensajes de error).
    Retorna: El valor si es válido.
    Lanza: ValueError si el valor está vacío.
    """
    if not valor.strip():
        raise ValueError(f"El campo {campo} no puede estar vacío.")
    return valor

def id_valido(id):
    """
    Lo que hace: Valida que un ID sea un número entero positivo.
    Parámetros:
    - id: El ID a validar.
    Retorna: El ID si es válido.
    Lanza: ValueError si el ID no es un número entero positivo.
    """
    if not isinstance(id, int) or id <= 0:
        raise ValueError("El ID debe ser un número entero positivo.")
    return id

def _rol_valido(rol):
    """"
    Lo que hace: Valida que un rol sea uno de los permitidos en la lista.
    Parámetros:
    - rol: El rol a validar.
    Retorna: El rol si es válido.
    Lanza: ValueError si el rol no es válido.
    """
    roles_permitidos = ['Supervisor', 'Administrador', 'Empleado']
    if rol not in roles_permitidos:
        raise ValueError(f"El rol {rol} no es válido. Roles permitidos: {', '.join(roles_permitidos)}")
    return rol

def _email_valido(correo):
    """
    Lo que hace: Valida que un correo tenga un formato válido usando una expresión regular.
    usa re.match para verificar el formato.
    Parámetros:
    - correo: El correo a validar.
    Retorna: El correo si es válido.
    Lanza: ValueError si el correo no tiene un formato válido.
    """
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", str(correo)):
        raise ValueError("Correo con formato inválido.")
    return correo

def _password_valida(contrasena, minimo=6):
    """
    Lo que hace: Revisa que la contraseña no esté vacía y tenga al menos un número mínimo de caracteres.
    Parámetros:
    - contrasena: La contrasena a validar.
    - minimo: El número mínimo de caracteres requerido.
    Retorna: La contrasena si es válida.
    Lanza: ValueError si la contrasena no cumple con los requisitos.
    """
    if contrasena is None or len(contrasena) < minimo:
        raise ValueError(f"La contraseña debe tener al menos {minimo} caracteres.")
    return contrasena

def _fecha_valida(fecha_str):
    """
    Lo que hace: Valida que una fecha tenga el formato correcto (YYYY-MM-DD).
    Parámetros:
    - fecha_str: La fecha en formato string a validar.
    Retorna: La fecha como objeto date si es válida.
    Lanza: ValueError si la fecha no tiene un formato válido.
    """
    try:
        fecha = date.fromisoformat(fecha_str)
        return fecha
    except ValueError:
        raise ValueError("Fecha con formato inválido. Use YYYY-MM-DD.")
    
def _fecha_inicio_menor_termino(fecha_inicio, fecha_termino):
    """
    Lo que hace: Valida que la fecha de inicio sea anterior a la fecha de término.
    Parámetros:
    - fecha_inicio: La fecha de inicio como objeto date.
    - fecha_termino: La fecha de término como objeto date.
    Retorna: True si la fecha de inicio es anterior a la fecha de término.
    Lanza: ValueError si la fecha de inicio no es anterior a la fecha de término
    """
    if fecha_inicio >= fecha_termino:
        raise ValueError("La fecha de inicio debe ser anterior a la fecha de término.")
    return True
   
   
   #=== Validaciones por entidad ===#

def validar_descripcion(descripcion: str) -> str:
    """
    Lo que hace: Valida que una descripción no esté vacía.
    Parámetros:
    - descripcion: La descripción a validar.
    Retorna: La descripción si es válida.
    Lanza: ValueError si la descripción está vacía.
    """
    descripcion = _no_vacio(descripcion, "Descripción")
    return descripcion

def validar_nombre(nombre: str) -> str:
    """
    Lo que hace: Valida que un nombre no esté vacío.
    Parámetros:
    - nombre: El nombre a validar.
    Retorna: El nombre si es válido.
    Lanza: ValueError si el nombre está vacío.
    """
    nombre = _no_vacio(nombre, "Nombre")
    return nombre

def validar_id(id: int) -> int:
    """
    Lo que hace: Valida que un ID sea un número entero positivo.
    Parámetros:
    - id: El ID a validar.
    Retorna: El ID si es válido.
    Lanza: ValueError si el ID no es un número entero positivo.
    """
    id = id_valido(id)
    return id

def validar_rol(rol: str) -> str:
    """
    Lo que hace: Valida que un rol sea uno de los permitidos.
    Parámetros:
    - rol: El rol a validar.
    Retorna: El rol si es válido.
    Lanza: ValueError si el rol no es válido.
    """
    rol = _rol_valido(rol)
    return rol

def validar_contrasena(contrasena: str, minimo=6) -> str:
    """
    Lo que hace: Valida que una contraseña no esté vacía y tenga al menos un número mínimo de caracteres.
    Parámetros:
    - contrasena: La contrasena a validar.
    - minimo: El número mínimo de caracteres requerido.
    Retorna: La contrasena si es válida.
    Lanza: ValueError si la contrasena no cumple con los requisitos.
    """
    contrasena = _no_vacio(contrasena, "Contraseña")
    contrasena = _password_valida(contrasena, minimo)
    return contrasena

def validar_correo(correo: str) -> str:
    """
    Lo que hace: Valida que un correo no esté vacío y tenga un formato válido.
    Parámetros:
    - correo: El correo a validar.
    Retorna: El correo si es válido.
    Lanza: ValueError si el correo no cumple con los requisitos.
    """
    correo = _no_vacio(correo, "Correo")
    correo = _email_valido(correo)
    return correo

def validar_fecha(fecha_str: str) -> date:
    """
    Lo que hace: Valida que una fecha tenga el formato correcto (YYYY-MM-DD).
    Parámetros:
    - fecha_str: La fecha en formato string a validar.
    Retorna: La fecha como objeto date si es válida.
    Lanza: ValueError si la fecha no tiene un formato válido.
    """
    fecha = _fecha_valida(fecha_str)
    return fecha

def validar_fechas(fecha_inicio_str: str, fecha_termino_str: str) -> tuple[date, date]:
    """
    Lo que hace: Valida que las fechas de inicio y término tengan el formato correcto (YYYY-MM-DD) y que la fecha de inicio sea anterior a la fecha de término.
    Parámetros:
    - fecha_inicio_str: La fecha de inicio en formato string a validar.
    - fecha_termino_str: La fecha de término en formato string a validar.
    Retorna: Una tupla con las fechas como objetos date si son válidas.
    Lanza: ValueError si alguna fecha no tiene un formato válido o si la fecha de inicio no es anterior a la fecha de término.
    """
    fecha_inicio = _fecha_valida(fecha_inicio_str)
    fecha_termino = _fecha_valida(fecha_termino_str)
    _fecha_inicio_menor_termino(fecha_inicio, fecha_termino)
    return fecha_inicio, fecha_termino

def validar_direccion(direccion: str) -> str:
    """
    Lo que hace: Valida que una dirección no esté vacía.
    Parámetros:
    - direccion: La dirección a validar.
    Retorna: La dirección si es válida.
    Lanza: ValueError si la dirección está vacía.
    """
    direccion = _no_vacio(direccion, "Dirección")
    return direccion

def validar_registro_tiempo(horas: float) -> float:
    """
    Lo que hace: Valida que las horas registradas sean un número positivo.
    Parámetros:
    - horas: Las horas a validar.
    Retorna: Las horas si son válidas.
    Lanza: ValueError si las horas no son un número positivo.
    """
    if not isinstance(horas, (int, float)) or horas <= 0:
        raise ValueError("Las horas registradas deben ser un número positivo.")
    return horas