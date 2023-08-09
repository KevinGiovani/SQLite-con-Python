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

if __name__ == '__main__':
    con, cursor = conectar()