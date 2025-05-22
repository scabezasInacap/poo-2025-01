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
            resultSet = cursor.fetchAll()
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
        except mysql.connector.Error as err:
            print(f"Error en la conexion a la BD: {err}")
            return None

# APP
# nueva instancia del objeto
indicador1 = IndicadorMonetario(1, 'Unidad de Fomento', 'UF', 39000, True)
indicador2 = IndicadorMonetario(2, 'Unidad Tributaria Mensual', 'UTM', 60000, True)
lista = []
lista.append(indicador1)
lista.append(indicador2)
#print(indicador1)
#print(indicador2)

for indi in lista:
    print(indi)


# Haga una lista de 3 indicadores
