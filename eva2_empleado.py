class Empleado:
    #constructor con parámetros
    def __init__(self, id, nombre, direccion, telefono, correo, fecha_inicio, salario, activo):
        self._id:int = id
        self._nombre:str = nombre
        self._direccion:str = direccion
        self._telefono:str = telefono
        self._correo:str = correo
        self._fecha_inicio = fecha_inicio
        self._salario:int = salario
        self._activo: bool = activo
        # pertenece a un departamento
        self._departamento = None
        # puede estar en mas de un proyecto
        self._proyectos = []
    
    #encapsulamiento: accesadores (getters) y mutadores (setters)
    def getId(self): return self._id
    def setId(self, nuevo): self._id = nuevo

    def getNombre(self): return self._nombre
    def setNombre(self, nuevo): self._nombre = nuevo

    def getDireccion(self): return self._direccion
    def setDireccion(self, nuevo): self._direccion = nuevo

    def getTelefono(self): return self._telefono
    def setTelefono(self, nuevo): self._telefono = nuevo

    def getCorreo(self): return self._correo
    def setCorreo(self, nuevo): self._correo = nuevo

    def getFechaInicio(self): return self._fecha_inicio
    def setFechaInicio(self, nuevo): self._fecha_inicio = nuevo

    def getSalario(self): return self._salario
    def setSalario(self, nuevo): self._salario = nuevo

    def getActivo(self): return self._activo
    def setActivo(self, nuevo): self._activo = nuevo

    def getDepartamento(self): return self._departamento
    def setDepartamento(self, nuevo): self._departamento = nuevo

    def getProyectos(self): return self._proyectos
    def setProyectos(self, nuevo): self._proyectos = nuevo

    #toString para mostrar
    def __str__(self):
        return f"Empleado [id: {self._id}]\n[nombre: {self._nombre}]\n[direccion: {self._direccion}]"
