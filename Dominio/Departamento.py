class Departamento:
    def __init__(self, id_departamento: int, nombre: str, gerente: str) -> None:
        self._id_departamento = id_departamento
        self._nombre = nombre
        self._gerente = gerente 

#=== Getters===#
    """ Lo que hace: Obtiene los atributos de las clases. 
        Retorna: Los atributos de la clase.
    """
    def obtener_id_departamento(self) -> str:
        return self._id_departamento
    
    def obtener_nombre(self) -> str:
        return self._nombre
    
    def obtener_gerente(self) -> str:
        return self._gerente
    
    
#=== Setters ===#
    """ Lo que hace: Coloca los atributos de las clases.
        Parámetros:
        - id_departamento: ID del departamento.
        - nombre: Nombre del departamento.
        - gerente: Gerente del departamento.
    """
    def colocar_id_departamento(self, id_departamento: int) -> None:
        self._id_departamento= id_departamento
    
    def colocar_nombre(self, nombre: str) -> None:
        self._nombre = nombre
    
    def colocar_gerente(self, gerente:str) -> None:
        self._gerente = gerente
    