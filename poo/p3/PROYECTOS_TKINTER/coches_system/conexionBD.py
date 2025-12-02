import mysql.connector
from mysql.connector import Error
try:
    # Conectar con la BD en MySQL (XAMPP)
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_coches'
    )
    # Crear un objeto de tipo cursor que se pueda reutilizar
    cursor = conexion.cursor(buffered=True)
except Error as e:
    # Provide a helpful message for troubleshooting
    print('No se pudo conectar a la base de datos MySQL. Verifique que XAMPP esté ejecutando MySQL y que la base de datos "bd_coches" exista.')
    print('Error:', e)
    raise
