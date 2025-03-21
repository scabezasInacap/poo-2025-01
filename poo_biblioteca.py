class Libro: 

    def __init__(self, _id, _titulo, _autor, _activo): 

        self.id = _id 

        self.titulo = _titulo 

        self.autor = _autor 

        self.activo = _activo 

    def __str__(self): 

        return f"{self.titulo} por el autor {self.autor}" 

 

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

#libro1: def __init__(self, id, titulo, autor, activo): 

libro1 = Libro(1, "El Quijote", "Miguel de Cervantes", True) 

libro2 = Libro(2, "Cien años de soledad", "GGM", True) 

biblioteca1.agregar_libro(libro1) 

biblioteca1.agregar_libro(libro2) 

biblioteca2.agregar_libro(libro2)