"""Crear los metodos setters y getters estos metodos son importatnes y necesarios en todas las clases para que el programador interactue con los valores
de los atributos a traves de estos metodos. Digamos que es la manera mas adecuada y recomendada para solicitar un valor o para ingresar o cambiar un
valor o un atributo en particular de la clase a traves de un objeto.
En teoria se deberia de crear un metodo getters y setters por cada atributo que contenga la clase
Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return, por otro lado el metodo set siempre recibe prarametros
para cambiar o modificar el valor del atributo o propiuedad en cuestion 

Metodos o acciones o fubnciopnes hacia el objeto


"""
import os

os.system("cls")
class coches():
    __color=""
    __marca=""
    __modelo=""
    __velocidad=""
    __caballaje=""
    __plazas=""      
#Metodo Constructor 
    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):



        self.__color=color
        self.__marca=marca
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas      



  
    def acelerar(self,incremento):
        pass
    
    def frenar(self,decremento):
        pass
    def getMarca(self):
        return self.__marca
    def setMarca(self,marca):
        self.__marca=marca
    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color=color
    def getModelo(self):
        return self.__modelo
    def setModelo(self,modelo):
        self.__modelo=modelo
    def getVelocidad(self):
        return self.__velocidad
    def setVelocidad(self,velocidad):
        self.__velocidad=velocidad
    def getCaballaje(self):
        return self.__caballaje
    def setCaballaje(self,caballaje):
        self.__caballaje=caballaje
    def getPlazas(self):
        return self.__plazas
    def setPlazas(self,plazas):
        self.__plazas=plazas
#Multiples objetos
coche1=coches("vw","blanco","2022",220,150,5)
coche2=coches()
coche3=coches()



print(f"Los valores del objeto 1 son: {coche1.getMarca()},{coche1.getColor()},{coche1.getCaballaje()},{coche1.getModelo()},{coche1.getPlazas()},{coche1.getVelocidad()}")