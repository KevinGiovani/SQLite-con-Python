import sqlite3

def conectar():
    """
    Conexión a la base de datos, en caso de que no existe esta se 
    crea automaticamente

    Returns:
        list: Conexión a la BDD, cursor para operaciones
    """
    conexion = sqlite3.connect('pruebas.db')
    # conexion = sqlite3.connect(':memory') # Con ':memory' la BDD se crea en memoria de modo que una vez que finalice el programa se perderan los datos
    cursor = conexion.cursor()
    return conexion, cursor

def crear_tabla(conexion,cursor):
    """
    Creación de una tabla en caso de que no exista dentro de la base de datos
    a partir de la ejecución de una sentencia de tipo 'create table'

    Args:
        conexion (sqlite3.Connection): Conexión a la BDD
        cursor (sqlite3.Cursor): Cursor para operaciones
    """
    sentencia = """
        CREATE TABLE IF NOT EXISTS usuarios
        (id INTEGER PRIMARY KEY NOT NULL,
        usuario TEXT NOT NULL,
        email TEXT NOT NULL,
        clave TEXT NOT NULL)
    """
    cursor.execute(sentencia)
    conexion.close()
    print("Tabla creada correctamente")

if __name__ == '__main__':
    conexion, cursor = conectar()
    print(type(conexion))
    print(type(cursor))
    crear_tabla(conexion,cursor)