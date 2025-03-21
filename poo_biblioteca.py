class Libro:
    #Constructor del objeto
    def __init__(self, _id, _titulo, _autor, _cantidadDisponible, _activo): 
        self.id = _id 
        self.titulo = _titulo 
        self.autor = _autor 
        self.cantidadDisponible = _cantidadDisponible
        self.cantidadPrestada = 0
        self.activo = _activo
    
    #Getter > Accesador
    @property
    def titulo(self):
        return self._titulo
    #Setter > Mutador
    @titulo.setter
    def titulo(self, _valorNuevo):
        #P.O.O Seguro
        if len(_valorNuevo) > 0:
            self._titulo = _valorNuevo
        else:
            raise ValueError("El titulo no puede estar vacio.")

    #metodo conocido como toString
    def __str__(self): 
        return f"{self.titulo} por el autor {self.autor} Disponibles #{self.cantidadDisponible} / Prestados #{self.cantidadPrestada}"

class Biblioteca: 
    def __init__(self, _id): 
        self.id = _id 
        self.libros = [] 

    def agregar_libro(self, _libro): 
        self.libros.append(_libro) 
        print(f"Libro Agregado en biblioteca {self.id} Exitosamente: {_libro}") 

#app 
biblioteca1 = Biblioteca(1) 
biblioteca2 = Biblioteca(2) 
#inicio a la antigua
print("Ingrese un nuevo libro indicando: id, titulo, autor y cantidad disponible")
libro1id = int(input("Ingrese Id: "))
libro1titulo = input("Ingrese Titulo: ")
libro1autor = input("Ingrese Autor: ")
libro1disponibles = int(input("Ingrese cantidad de libros disponibles: "))
libro1 = Libro(libro1id, libro1titulo, libro1autor, libro1disponibles, True)
biblioteca1.agregar_libro(libro1)
#fin a la antigua

#inicio POO
#con el accesador > Getter
print(libro1.titulo)
#con el mutador > Setter
libro1.titulo = "Cien años de Soledad"
print(libro1)
#fin POO

#codigo anterior al 21-03-2025
#libro1: def __init__(self, id, titulo, autor, activo): 
#libro1 = Libro(1, "El Quijote", "Miguel de Cervantes", True) 
#libro2 = Libro(2, "Cien años de soledad", "GGM", True) 
#biblioteca1.agregar_libro(libro1) 
#biblioteca1.agregar_libro(libro2) 
#biblioteca2.agregar_libro(libro2)
