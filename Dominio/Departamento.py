class Departamento:
    def __init__(self, id_departamento: int, nombre: str):
        self._id_departamento = id_departamento
        self._nombre = nombre

    #Getters

    def obtener_id_departamento(self) -> str:
        return self._id_departamento
    
    def obtener_nombre(self) -> str:
        return self._nombre
    
    
    #Setters
      
    def colocar_id_departamento(self, id_departamento: int) -> None:
        self._id_departamento= id_departamento
    
    def colocar_nombre(self, nombre: str) -> None:
        self._nombre = nombre
    