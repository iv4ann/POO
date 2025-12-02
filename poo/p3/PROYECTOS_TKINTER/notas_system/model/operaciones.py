import mysql.connector
from mysql.connector import Error
from datetime import date

class operaciones:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",       
                user="root",            
                password="",            
                database="bd_notas"     
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la BD bd_notas")
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")

    
    def registrar_usuario(self, nombre, apellidos, email, password):
        try:
            cursor = self.connection.cursor()
            sql = """INSERT INTO usuarios (nombre, apellidos, email, password, fecha) 
                     VALUES (%s, %s, %s, %s, %s)"""
            valores = (nombre, apellidos, email, password, date.today())
            cursor.execute(sql, valores)
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error al registrar usuario: {e}")
            return False

    def login_usuario(self, email, password):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT id, nombre FROM usuarios WHERE email=%s AND password=%s"
            cursor.execute(sql, (email, password))
            usuario = cursor.fetchone()
            cursor.close()
            if usuario:
                return usuario[0], usuario[1]  # id y nombre
            return None
        except Error as e:
            print(f"Error en login: {e}")
            return None

   
    def guardar_nota(self, usuario_id, titulo, descripcion):
        try:
            cursor = self.connection.cursor()
            sql = """INSERT INTO notas (usuario_id, titulo, descripcion, fecha) 
                     VALUES (%s, %s, %s, %s)"""
            valores = (usuario_id, titulo, descripcion, date.today())
            cursor.execute(sql, valores)
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error al guardar nota: {e}")
            return False

    def obtener_notas(self, usuario_id):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT id, titulo, descripcion, fecha FROM notas WHERE usuario_id=%s"
            cursor.execute(sql, (usuario_id,))
            notas = cursor.fetchall()
            cursor.close()
            return notas
        except Error as e:
            print(f"Error al obtener notas: {e}")
            return []

    def actualizar_nota(self, usuario_id, nota_id, titulo, descripcion):
        try:
            cursor = self.connection.cursor()
            sql = """UPDATE notas 
                     SET titulo=%s, descripcion=%s 
                     WHERE id=%s AND usuario_id=%s"""
            valores = (titulo, descripcion, nota_id, usuario_id)
            cursor.execute(sql, valores)
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error al actualizar nota: {e}")
            return False

    def eliminar_nota(self, usuario_id, nota_id):
        try:
            cursor = self.connection.cursor()
            sql = "DELETE FROM notas WHERE id=%s AND usuario_id=%s"
            cursor.execute(sql, (nota_id, usuario_id))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error al eliminar nota: {e}")
            return False


# Instancia global para usar directamente en Vistas
operaciones = operaciones()