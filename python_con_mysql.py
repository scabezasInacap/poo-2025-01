# base de datos
# CREATE DATABASE `inacap_poo_ejemplo`;
# CREATE USER 'inacap_poo'@'localhost' IDENTIFIED BY '1n4c4p.2025';
# GRANT ALL PRIVILEGES ON `inacap_poo_ejemplo`.* TO 'inacap_poo'@'localhost';
# FLUSH PRIVILEGES;
# CREATE TABLE indicadores(
#   id INT PRIMARY KEY,
#   nombre VARCHAR(50) NOT NULL,
#   codigo VARCHAR(10) NOT NULL UNIQUE,
#   valor  DECIMAL(10,2) NOT NULL,
#   activo BOOLEAN NOT NULL DEFAULT FALSE
# );
# INSERT INTO indicadores (id, nombre, codigo, valor, activo)  VALUES (1, "Unidad de Fomento", "UF", 39000, TRUE)

import mysql.connector

class InidicadorMonetario:
    # constructor con parametros
    def __init__(self, _id=None, _nombre=None, _codigo=None, _valor=None, _activo=None):
        self.id = _id
        self.nombre = _nombre
        self.codigo = _codigo
        self.valor = _valor
        self.activo = _activo
    def __str__(self):
        estadoActivo = True if self.activo else False
        return f"----\nID: {self.id}\nNombre: {self.nombre}\nCodigo: {self.codigo}\nValor: {self.valor}\nActivo: {estadoActivo}"
    #funciones propias
    def getAll(self, db_conexion):
        try:
            cursor = db_conexion.cursor()
            query = "SELECT id, nombre, codigo, valor, activo FROM indicadores"
            cursor.execute(query)
            resultado = cursor.fetchall()
            cursor.close()
            lista = []
            if resultado:
                for registro in resultado:

                    uno = InidicadorMonetario(registro[0], registro[1], registro[2], registro[3], registro[4])
                    lista.append(uno)
                return lista
                
            else:
                print("No hay resultados en getALL")
                return []
        except mysql.connector.Error as err:
            print(f"Error con getALL: {err}")
            return []

class DatabaseManager:
    def __init__(self, _host, _user, _password, _database):
        self.host = _host
        self.user = _user
        self.password = _password
        self.database = _database
    
    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            print(f"Conexion exitosa")
            return self.connection
        except mysql.connector.Error as err:
            print(f"Error en la BD: {err}")
            return None
        
    def desconectar(self, _conexion):
        if _conexion and _conexion.is_connected():
            _conexion.close()
            print("Conexion a la BD cerrada")


# APP
# Antes de ejecutar el APP: corroborar por el terminal los siguientes comandos
# > pip --version
# Si tiene resultados, entonces tiene pip instalado, sino hay que instalar
# pip install mysql-connector-python
# una vez instalado, podremos seguir ejecutando el codigo
# tenemos que tener las clases IndicadorMontario y DatabaseManager creadas

# definimos los parametros de conexion (host, user, pass, db)
db_manager = DatabaseManager('localhost', 'root', '', 'inacap_poo_ejemplo')
# db_manager = DatabaseManager('localhost', 'inacap_poo', '1n4c4p.2025', 'inacap_poo_ejemplo')
conexion = db_manager.conectar()

im = InidicadorMonetario()
lista = im.getAll(conexion) #retorna una lista

print("ESTOS SON TODOS LOS REGISTROS")
print("=============================")
for reg in lista:
    print(reg)
print("=============================")

# una vez conectada, al final del proceso, se debe desconectar
db_manager.desconectar(conexion)
