from conexionBD import *
class Notas():
    def __init__(self,id_user,titulo,descripcion,fecha):
        self._id_user=id_user
        self._titulo=titulo
        self._descripcion=descripcion
        self._fecha=fecha

    @property
    def id_user(self):
        return self._id_user
    @id_user.setter
    def id_user(self,id):
        self._id_user=id

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self,titu):
        self._titulo=titu

    @property
    def descripcion(self):
        return self._descripcion
    @descripcion.setter
    def descripcion(self,desc):
        self._descripcion=desc

    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self,fec):
        self._fecha=fec


    @staticmethod
    def crear(usuario_id,titulo,descripcion,fecha):
        try:
            cursor.execute(
                "insert into notas values(null,%s,%s,%s,%s)",
                (usuario_id,titulo,descripcion,fecha)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def mostrar(usuario_id):
            try:
                cursor.execute("select * from notas where usuario_id=%s",(usuario_id,))
                return cursor.fetchall()
            except:    
                return []

    @staticmethod
    def actualizar(titulo,descripcion,fecha,id):
        try:
            cursor.execute("update notas set titulo=%s,descripcion=%s,fecha=%s where id=%s",(titulo,descripcion,fecha,id))
            conexion.commit()
            return True
        except: 
            return False
    
    @staticmethod
    def eliminar(id):
            try:
                cursor.execute(
                    "delete from notas where id=%s",
                    (id,)
                ) 
                conexion.commit() 
                return True  
            except:    
                return False
        
