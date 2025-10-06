""" Practica # 1 Implementar paradigma estructurado
Crear un programa que obtenga el area de un rectangulo """""

import os 
#1 Estructurado

largo=5
ancho=6
def areaRectangulo(largo,ancho):
    area=largo*ancho
    os.system("cls")
    return area

print(f"El area del rectangulo es {areaRectangulo(largo,ancho)}")


#2 00
class areaRectangulo1:
    def _init_(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho

    def areaRectangulo2(self):
        area=self.largo*self.ancho
        return area

rectangulo=areaRectangulo1(4,7)# instanciar un objeto de la clase

print(f"El area del rectangulo es {rectangulo.areaRectangulo2()}")