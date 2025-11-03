from conexionBD import *
import hashlib
import datetime

class Usuarios():
    def __init__(self,nombre,apellidos,email,password,fecha):
        self._nombre=nombre
        self._apellidos=apellidos
        self._email=email
        self._password=password
        self._fecha=fecha
    
    @property
    def nombre(self):
         return self._nombre
    @nombre.setter
    def nombre(self,nomb):
         self._nombre=nomb

    @property
    def apellidos(self):
         return self._apellidos
    @apellidos.setter
    def apellidos(self,apell):
         self._apellidos=apell

    @property
    def email(self):
         return self._email
    @email.setter
    def email(self,em):
         self._email=em

    @property
    def password(self):
         return self._password
    @password.setter
    def password(self,passw):
         self._password=passw

    @property
    def fecha(self):
         return self._fecha
    @fecha.setter
    def fecha(self,fec):
         self._fecha=fec

    @staticmethod
    def hash_password(contrasena):
            return hashlib.sha256(contrasena.encode()).hexdigest()
    
    @staticmethod
    def registrar(nombre,apellidos,email,contrasena,fecha):
            try:
                contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
                print(contrasena)
                cursor.execute(
                    "insert into usuarios values(null,%s,%s,%s,%s,%s)",
                    (nombre,apellidos,email,contrasena,fecha)
                )
                conexion.commit()
                return True
            except:
                return False    

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute(
                "select * from usuarios where email=%s and password=%s",
                (email,contrasena)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return None      
        except:
          return None  
       
        

