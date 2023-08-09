import sqlite3

def actualizar_datos(conexion,cursor,usuario,id):
    """
    Modificación de datos(nombre del usuario) a partir del ID ingresado
    
    Args:
        conexion (sqlite3.Connection): Conexión a la BDD
        cursor (sqlite3.Cursor): Cursor para operaciones
        usuario (str): Nuevo nombre del usuario
        id (int): Identificador del usuario al que se realizara el cambio
    """
    sentencia = f"UPDATE usuarios SET usuario='{usuario}' WHERE id={id}"
    cursor.execute(sentencia)
    conexion.commit()
    print(f"\nDato actualizo de la fila con ID:{id}")
    
def mostrar_datos(datos):
    """
    Muestra los datos por fila en la terminal
    
    Args:
        datos (list): _description_
    """
    for fila in datos:
        print(fila)
    
def consultar_datos_id(cursor,id):
    """
    Realiza la consulta de datos a partir de un ID ingresado
    como parametro

    Args:
        cursor (sqlite3.Cursor): Cursor para operaciones
        id (_type_): Identificador de una fila de datos en 'usuarios'

    Returns:
        sqlite3.Cursor: Fila de los datos consultados por ID
    """
    sentencia = f"SELECT usuario,email FROM usuarios WHERE id={id}"
    resultado = cursor.execute(sentencia)
    return resultado

def consultar_datos02(cursor):
    """
    Realiza la consulta de datos especificos dentro de la tabla 'usuarios' 
    con limite de 3 columnas

    Args:
        cursor (sqlite3.Cursor): Cursor para operaciones
    """
    sentencia = "SELECT id,usuario,email FROM usuarios LIMIT 3"
    resultado = cursor.execute(sentencia)
    return resultado

def consultar_datos01(cursor):
    """
    Realiza la consulta de todos los datos de la tabla 'usuarios'
    
    Args:
        cursor (sqlite3.Cursor): Cursor para operaciones
    """
    sentencia = "SELECT * FROM usuarios"
    resultado = cursor.execute(sentencia)
    # print(cursor.fetchall()) # Devuelve todas las filas de una consulta
    # print(cursor.fetchone()) # Devuelve unicamente una fila
    # print(cursor.fetchmany(3)) # Recibe como argumento un número para las filas máximas al recorrer consultas.
    # print(resultado)
    return resultado
        
def insertar_datos(conexion, cursor, datos):
    """
    Inserción de datos dentro de la BDD
    Args:
        conexion (sqlite3.Connection): Conexión a la BDD
        cursor (sqlite3.Cursor): Cursor para operaciones
        datos (list): Valores a agregar usando la sentencia
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
    #conexion.close()
    
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
    #conexion.close()
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
    # insertar_datos(conexion, cursor, datos)
    
    print("CONSULTAS:\n'SELECT * FROM usuarios':")
    mostrar_datos(consultar_datos01(cursor))
    
    print("\n'SELECT id, usuario, email FROM usuarios':")
    resultado = consultar_datos02(cursor)
    for fila in resultado:
        print("ID:", fila[0], end=" ")
        print("Usuario:", fila[1], end=" ")
        print("Email:", fila[2])
    
    print("\nConsultar por ID:\n'SELECT usuario,email FROM usuarios WHERE id=4'")
    mostrar_datos(consultar_datos_id(cursor,4))
    
    actualizar_datos(conexion,cursor,"Armando", 1)

    conexion.close()