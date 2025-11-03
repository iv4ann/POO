from conexionBD import *
from model import coches,cochesBD

import os
os.system("cls")
class Autos:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas

    def insertar(self):
        try:
           cursor.execute(
               "insert into autos values(null,%s,%s,%s,%s,%s,%s)",
               (self._marca,self._color,self._modelo,self._velocidad,self._caballaje,self._plazas)
               )
           conexion.commit()
           return True
        except:  
           return False   
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas):
        try:
            cursor.execute(
            "update autos set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s where id=%s",(marca,
            color,modelo,velocidad,caballaje,plazas,id))
            conexion.commit()
            return True
        except:
            return False
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from autos where id=%s",(id,))
            conexion.commit()
            return True
        except:
            return False
    @staticmethod
    def consultar():
        try:
            cursor.execute("select from autos",())
            return cursor.fetchall()
        except:
            []
class camionetas:
    @staticmethod
    def insertar(self,marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        try:
            cursor.execute("insert into camionetas values(null,%s,%s,%s,%s,%s,%s,%s,%s)"),
            (marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
            auto=cochesBD.camionetas(auto.marca,auto.color,auto.modelo,auto.velocidad,auto.caballaje,auto.plazas)
            respuesta=auto.insertar()
        
            conexion.commit()
            return True
        except:
            return False
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id):
        try:
            cursor.execute(
            "update autos set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s,eje=%s,capacidadCarga=%s where id=%s",(marca,
            color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id))
            conexion.commit()
            return True
        except:
            return False
    def eliminar(id):
        try:
            cursor.execute("delete from autos where id=%s",(id,))
            conexion.commit()
            return True
        except:
            return False

class camiones:
    @staticmethod
    def insertar(self,marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
        try:
            cursor.execute("insert into camiones values(null,%s,%s,%s,%s,%s,%s,%s,%s)"),
            (marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
            coche=coches.Camiones(marca,color,modelo,velocidad,plazas,eje,capacidadCarga)
            conexion.commit()
            imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
            respuesta=cochesBD.Camiones.insertar(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
            return True
        except:
            return False
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id):
        try:
            cursor.execute(
            "update autos set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s,eje=%s,capacidadCarga=%s where id=%s",(marca,
            color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id))
            conexion.commit()
            return True
        except:
            return False
    def eliminar(id):
        try:
            cursor.execute("delete from autos where id=%s",(id,))
            conexion.commit()
            return True
        except:
            return False
