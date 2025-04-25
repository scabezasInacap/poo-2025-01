class Departamento: 
    def __init__(self, id, nombre, gerente, activo): 
        self._id = id 
        self._nombre = nombre 
        self._gerente = gerente 
        self._activo = activo

    #encapsulamiento: accesadores (getters) y mutadores (setters)
    def getId(self): return self._id
    def setId(self, nuevo): self._id = nuevo

    def getNombre(self): return self._nombre
    def setNombre(self, nuevo): self._nombre = nuevo

    def getGerente(self): return self._nombre
    def setGerente(self, nuevo): self._gerente = nuevo

    def getActivo(self): return self._activo
    def setActivo(self, nuevo): self._activo = nuevo

    #toString para mostrar
    def __str__(self):
        return f"[Departamento id: {self._id} - nombre: {self._nombre} - gerente: {self._gerente}]"
