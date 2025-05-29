CREATE DATABASE poo;

use poo;

CREATE TABLE rol(
	id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    activo BOOL DEFAULT FALSE
);

INSERT INTO rol VALUE (1, "Unidad de Fomento", TRUE);

SELECT * FROM rol;

import mysql.connector

def mostrarDatos(_lista):
    for reg in _lista:
        print(reg)

class ConexionManager:
    def __init__(self, _host, _username, _password, _database):
        self.host = _host
        self.username = _username
        self.password = _password
        self.database = _database
    def conectarMySQL(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.username,
                password = self.password,
                database = self.database
            )
            # print(f"Se logro la conexion a la BD MySQL")
            return self.connection
        #except mysql.connector.Error as err:
        except Exception as err:
            print(f"Error en la conexion a la BD: {err}")
            return None

class Rol:
    def __init__(self, _id = None, _nombre = None, _activo = None ):
        self.id = _id
        self.nombre = _nombre
        self.activo = _activo
    def __str__(self):
        return f"ROL id: {self.id}\nNombre: {self.nombre}\nActivo: {self.activo}"
    def getAll(self, _conexion):
        try:
            cursor = _conexion.cursor()
            query = "SELECT id, nombre, activo FROM rol"
            cursor.execute(query)
            resultSet = cursor.fetchall()
            cursor.close()
            # podemos trabajar con la lista, pq los resultados de la query estan en RS
            lista = []
            if resultSet:
                # todo bien, existen datos
                for reg in resultSet:
                    fila = Rol(reg[0], reg[1], reg[2])
                    lista.append(fila)
                return lista
            else:
                # Hay problemas o no hay datos
                print(f"Sin Datos en Rol")
                return []
        except mysql.connector.Error as err:
            print(f"Error en getAll rol: {err}")
            return []
    def getById(self, _conexion, _id):
        print(f"buscar por ID: {_id}")
    def add(self, _conexion, _nuevo):
        print(f"Agregar nuevo rol: {_nuevo}")
    def update(self, _conexion, _modificado):
        print(f"Actualizar rol con estos datos: {_modificado}")
    def delete(self, _conexion, _id):
        print(f"Eliminar rol id: {_id}")
    def reactivate(self, _conexion, _id):
        print(f"Reactivar rol id: {_id}")

#APP
#instancia de un objeto
rol1 = Rol(10, "adimistrador", True)
#print (rol1)
#rol1.getAll(None)
#rol1.add(None, rol1)
#rol1.update(None, rol1)
#rol1.delete(None, rol1.id)
#rol1.reactivate(None, rol1.id)
print("------------------------------------------")
conexion = ConexionManager('localhost', 'root', 'admin', 'poo')
conexion = conexion.conectarMySQL()
listaRoles = rol1.getAll(conexion)
mostrarDatos(listaRoles)
print("------------------------------------------")
