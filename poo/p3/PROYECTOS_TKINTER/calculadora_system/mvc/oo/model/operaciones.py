from conexionBD import *
class Operaciones():
    @staticmethod
    def crear(numero1,numero2,signo,resultado):
        try:
            cursor.execute(
                "insert into operaciones values(null,NOW(),%s,%s,%s,%s)",
                (numero1,numero2,signo,resultado)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def mostrar():
            try:
                cursor.execute("select * from operaciones")
                return cursor.fetchall()
            except:    
                return []

    @staticmethod
    def actualizar(numero1,numero2,signo,resultado,id):
        try:
            cursor.execute("update operaciones set numero1=%s,numero2=%s,signo=%s,resultado=%s where id=%s",(numero1,numero2,signo,resultado,id))
            conexion.commit()
            return True
        except: 
            return False
    
    @staticmethod
    def eliminar(id):
            try:
                cursor.execute(
                    "delete from operaciones where id=%s",
                    (id,)
                ) 
                conexion.commit() 
                return True  
            except:    
                return False
        
