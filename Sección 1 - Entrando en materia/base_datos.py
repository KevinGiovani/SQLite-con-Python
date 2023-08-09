import sqlite3

def insertar_datos(conexion, cursor, datos):
    """
    Inserción de datos dentro de la BDD
    Args:
        conexion (sqlite3.Connection): Conexión a la BDD
        cursor (sqlite3.Cursor): Cursor para operaciones
        datos (_type_): Valores a agregar usando la sentencia
    """
    # Diferentes formas de realizar la inserción de datos en la tabla
    # sentencia =  " INSERT INTO usuarios (usuario, email, clave) VALUES ("Rodrigo", "Rodrigo@gmail.com", "ROD44") "
    # sentencia = "INSERT INTO usuarios (usuario, email, clave) VALUES (?, ?, ?)"
    sentencia = "INSERT INTO usuarios VALUES (NULL,?, ?, ?)"
    # cursor.execute(sentencia, datos) # Insertar un dato
    cursor.executemany(sentencia,datos) # Insertar varios datos
    #cursor.execute(sentencia)
    print("Datos insertados correctamente")
    conexion.commit() # Guardar los cambios
    conexion.close()
    

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

if __name__ == '__main__':
    conexion, cursor = conectar()
    # crear_tabla(conexion,cursor)
    #insertar_datos(conexion, cursor)
    #datos = ('Alan', 'alan@gmail.com', 'al2100P') # Insertar 1 dato
    # Insertar varios datos:
    datos = [('Yolanda', 'yolanda@gmail.com', 'y0l4A'),
             ('Esteban','esteban@gmail.com', 'eSt001'),
             ('Andrea','andrea@gmail.com', 'And550B')]
    insertar_datos(conexion, cursor, datos)