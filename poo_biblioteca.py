class Libro:
    def __init__(self): 
            self.id = 1
            self.titulo = "Sin Título" 
            self.autor = "Sin Autor" 
            self.cantidadDisponible = 0
            self.cantidadPrestada = 0
            self.activo = False
    def __str__(self): 
        return f"{self.titulo} por el autor {self.autor} Disponibles #{self.cantidadDisponible} / Prestados #{self.cantidadPrestada}"
    @property
    def id(self): #getter
         return self._id
    @id.setter
    def id(self, _nuevo):
        if _nuevo > 0:
              self._id = _nuevo
        else:
             raise ValueError("El ID no puede ser cero o negativo.")
    @property
    def titulo(self):
         return self._titulo
    @titulo.setter
    def titulo(self, _nuevo):
        if len(_nuevo) > 0:
            self._titulo = _nuevo
        else:
            raise ValueError("El TITULO no puede ser vacio.") 

class Biblioteca: 
    def __init__(self, _id): #self obligatorio
        self.id = _id 
        self.libros = [] 
    def agregar_libro(self, _libro): 
        self.libros.append(_libro) #el libro del parametro es agregado al arreglo de libros
        print(f"Libro Agregado en biblioteca {self.id} Exitosamente: {_libro}") 
#app 
biblioteca1 = Biblioteca(1) 
biblioteca2 = Biblioteca(2) 
#inicio POO
print("POO Ingrese un nuevo libro indicando: id, titulo, autor y cantidad disponible")
#instancia del objeto
libro1 = Libro()
libro1.id = int(input("Ingrese Id: "))
libro1.titulo = input("Ingrese Titulo: ")
print(libro1)
