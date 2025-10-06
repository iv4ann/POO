#Clase coches
import os

os.system("cls")

class coches():
 
    def __init__(self,color,marca,velocidad):#metodo que inicializa los valores cuando se instancia un objeto de la clase
        self.color=color#atributos del objeto
        self.marca=marca
        self._velocidad=velocidad

    def acelerar(self,incremento):#metodos del objeto
        self._velocidad=self._velocidad+incremento
        return self._velocidad
    
    def frenar(self,decremento):
        self._velocidad=self._velocidad-decremento
        return self._velocidad
    def tocar_claxon(self):
        print("LOL")
    
 
coche1=coches("blanco","toyota",220)
coche2=coches("amarillo","jeep",400)

print(coche1.acelerar(50))
print(coche2.frenar(100))
print(coche1.tocar_claxon())



"""print(f"Los valores del objeto 1 son: {coche1.marca},{coche1.color},{coche1._velocidad}")


print(f"El coche 1 acelero de {coche1._velocidad} a {coche1.acelerar(50)}")
print(f"Los valores del objeto 2 son: {coche2.marca},{coche2.color},{coche2._velocidad}")
print(f"El coche 1 acelero de {coche2._velocidad} a {coche2.frenar(50)}")"""

