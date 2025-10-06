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
    
coche1=coches()
coche2=coches()
coche3=coches()
#2DA FORMA
@property
def marca(self):
    return self.__marca
@marca.setter
def marca(self,marca):
    self.__marca=marca

coche1.setMarca("VW")
coche1.setColor("Blano")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)
"""
coche1.__color="blanco"
coche1.__marca="VW"
coche1.__modelo="2022"
coche1.__velocidad=220
coche1.__caballaje=150
coche1.__plazas=5



coche2.__color="azul"
coche2.__marca="Nissan"
coche2.__modelo="2020"
coche2.__velocidad=180
coche2.__caballaje=150
coche2.__plazas=6"""

print(f"Los valores del objeto 1 son: {coche1.getMarca()},{coche1.getColor()},{coche1.getCaballaje()},{coche1.getModelo()},{coche1.getPlazas()},{coche1.getVelocidad()}")