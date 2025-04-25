from departamento import Departamento
from empleado import Empleado

# APP
d1 = Departamento(1,'TI', 'Seba Cabezas', True)
# print(d1)
#empleado1 es una instancia de un objeto Empleado
empleado1 = Empleado(111, "Sebastian", "Calle 1", 95618, "scabezas@inacap.cl", "08/06/1987", 1234, True)
# print(empleado1) #va por el toString (__str__)

empleado1.setDepartamento(d1)

print(f"El empleado {empleado1.getId()} trabaja en el departamento: {empleado1.getDepartamento().getNombre()}")
# print(empleado1.getId())
# empleado1.setId(123)
# print(empleado1.getId())
