import os
os.system("cls")

class coches:
    def __init__(self, marca, color, modelo, velocidad, potencia, plazas):
        self.__marca = marca
        self.__color = color
        self.__modelo = modelo
        self.__velocidad = velocidad
        self.__potencia = potencia
        self.__plazas = plazas

    def acelerar(self):
        return f"Estoy acelerando km/h"

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def velocidad(self):
        return self.__velocidad
    @velocidad.setter
    def velocidad(self, velocidad):
        self.__velocidad = velocidad

    @property
    def potencia(self):
        return self.__potencia
    @potencia.setter
    def potencia(self, potencia):
        self.__potencia = potencia

    @property
    def plazas(self):
        return self.__plazas
    @plazas.setter
    def plazas(self, plazas):
        self.__plazas = plazas


class Camion(coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, plazas, ejes, capacidad_carga):
        super().__init__(marca, color, modelo, velocidad, potencia, plazas)
        self.__ejes = ejes
        self.__capacidad_carga = capacidad_carga

    @property
    def capacidad_carga(self):
        return self.__capacidad_carga
    @capacidad_carga.setter
    def capacidad_carga(self, capacidad_carga):
        self.__capacidad_carga = capacidad_carga


class Camioneta(coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada):
        super().__init__(marca, color, modelo, velocidad, potencia, plazas)
        self.__traccion = traccion
        self.__cerrada = cerrada

    @property
    def traccion(self):
        return self.__traccion
    @traccion.setter
    def traccion(self, traccion):
        self.__traccion = traccion

    @property
    def cerrada(self):
        return self.__cerrada
    @cerrada.setter
    def cerrada(self, cerrada):
        self.__cerrada = cerrada
    def transportar(self):
        return "Se ha transportado"
    def acelerar(self):
        return "Ha acelerado la camioneta"
    def frenar(self):
        return "Ha frenado la camioneta"