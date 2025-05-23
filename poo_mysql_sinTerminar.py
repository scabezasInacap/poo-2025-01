#-- user: root -- pass: admin
#-- BD: poo
# CREATE DATABASE poo;

#use poo;

#CREATE TABLE indicadores(
#	id INT PRIMARY KEY,
#    nombre VARCHAR(50) NOT NULL,
#    codigo VARCHAR(10) NOT NULL UNIQUE,
#    valor INT NOT NULL,
#    activo BOOL DEFAULT FALSE
#);
# INSERT INTO indicadores VALUE (1, "Unidad de Fomento", "UF", 38000, TRUE);
# SELECT * FROM indicadores;

# biblioteca
import mysql.connector

def mostrarDatos(_lista):
    for reg in _lista:
        print(reg)

class IndicadorMonetario:
    # constructor con paramatros
    def __init__(self, _id = None, _nombre = None, _codigo = None, _valor = None, _activo = None):
        self.id = _id
        self.nombre = _nombre
        self.codigo = _codigo
        self.valor = _valor
        self.activo = _activo
    def __str__(self):
        # return "id: " + self.id + " nombre: " + self.nombre
        # Mostramos todos los atributos de la clase
        return f"Indicador Monetario ID: {self.id}\nNombre: {self.nombre}\nCodigo: {self.codigo}\nValor: ${self.valor}\nActivo: {self.activo}"
    def getAll(self, db_connection):
        try:
            cursor = db_connection.cursor()
            query = "SELECT id, nombre, codigo, valor, activo FROM indicadores"
            cursor.execute(query)
            resultSet = cursor.fetchall()
            cursor.close()
            # podemos trabajar con la lista, pq los resultados de la query estan en RS
            lista = []
            if resultSet:
                # todo bien, existen datos
                for reg in resultSet:
                    fila = IndicadorMonetario(reg[0], reg[1], reg[2], reg[3], reg[4])
                    lista.append(fila)
                return lista
            else:
                # Hay problemas o no hay datos
                print(f"Sin Datos en Indicador Monetario")
                return []
        except mysql.connector.Error as err:
            print(f"Error en getAll: {err}")
            return []
    def add(self, db_connection, _nuevo): #agregar
        try:
            nuevoId = len(self.getAll(db_connection)) + 1
            cursor = db_connection.cursor()
            query = f"INSERT INTO indicadores (id, nombre, codigo, valor, activo) VALUES ({nuevoId},'{_nuevo.nombre}', '{_nuevo.codigo}', {_nuevo.valor}, {_nuevo.activo})"
            #print(query)
            cursor.execute(query)
            db_connection.commit()
            #resultSet = cursor.fetchall()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error en add: {err}")
            return None
    
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
            print(f"Se logro la conexion a la BD MySQL")
            return self.connection
        #except mysql.connector.Error as err:
        except Exception as err:
            print(f"Error en la conexion a la BD: {err}")
            return None

# APP
# nueva instancia del objeto
indicador = IndicadorMonetario()
conexion = ConexionManager('localhost', 'root', 'admin', 'poo')
conexion = conexion.conectarMySQL()
listaIndicadores = indicador.getAll(conexion)
# mostrarDatos(listaIndicadores)
#agregar un nuevo valor
indicador2 = IndicadorMonetario(0, 'Unidad Tributaria Mensual', 'UTM', 60000, True)
if indicador.add(conexion, indicador2):
    # listaIndicadores.append(indicador2) # no esta bien hacer esto
    listaIndicadores = indicador.getAll(conexion)
    print("Nuevo registro agregado exitosamente")
mostrarDatos(listaIndicadores)


# SIN BASE DE DATOS
#indicador1 = IndicadorMonetario(1, 'Unidad de Fomento', 'UF', 39000, True)
#indicador2 = IndicadorMonetario(2, 'Unidad Tributaria Mensual', 'UTM', 60000, True)
#lista = []
#lista.append(indicador1)
#lista.append(indicador2)
#print(indicador1)
#print(indicador2)

#for indi in lista:
#    print(indi)


# Haga una lista de 3 indicadores
