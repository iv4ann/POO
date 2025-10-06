import os 
os.system("cls")

class Clase:
    def __init__(self, color, tamano):
        self._atributo_publico = "Soy un atributo público"
        self._atributo_protegido = "Soy un atributo protegido"
        self.__atributo_privado = "Soy un atributo privado"
        self.__color = color
        self.__tamano = tamano

    # Encapsulamiento de color
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color

    # Encapsulamiento de tamaño
    @property
    def tamano(self):
        return self.__tamano
    @tamano.setter
    def tamano(self, tamano):
        self.__tamano = tamano    

    # Getter para el atributo privado
    def getAtributoPrivado(self):
        return self.__atributo_privado

    # Público
    @property
    def atributo_publico(self):
        return self._atributo_publico
    @atributo_publico.setter
    def atributo_publico(self, valor):
        self._atributo_publico = valor

    # Protegido
    @property
    def atributo_protegido(self):
        return self._atributo_protegido
    @atributo_protegido.setter
    def atributo_protegido(self, valor):
        self._atributo_protegido = valor

    # Privado
    @property
    def atributo_privado(self):
        return self.__atributo_privado
    @atributo_privado.setter
    def atributo_privado(self, valor):
        self.__atributo_privado = valor
objeto = Clase("Rojo","Grande")

print(objeto.atributo_privado)     # Privado (via property)
print(objeto.atributo_protegido)   # Protegido (convención, no recomendado)
print(objeto.atributo_publico)     # Público
print(objeto.color, objeto.tamano)

objeto.color = "Amarillo"
print(objeto.color)