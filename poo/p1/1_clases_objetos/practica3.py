import os
os.system("cls")
class Alumnos:
    def __init__(self,nombre,edad,matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        self.__edad = edad
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    def inscribirse():
        pass
    def estudiar():
        pass

alumno1= Alumnos("Pedro Paramo",25,222)
print(alumno1.nombre)
print(alumno1.edad)
print(alumno1.matricula)
alumno2=Alumnos("Juan Escutia",90,777)
print(alumno2.nombre)
print(alumno2.edad)
print(alumno2.matricula)

class Cursos:
    def __init__(self,nombre,codigo,creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo=codigo
    @property
    def creditos(self):
        return self.__creditos
    @creditos.setter
    def creditos(self, creditos):
        self.__creditos=creditos
    def asignar():
        pass

curso1=Cursos("Ciencias Sociales",123,100)
print(curso1.nombre)
print(curso1.codigo)
print(curso1.creditos)
curso2=Cursos("Termodinamica",243,70)
print(curso2.nombre)
print(curso2.codigo)
print(curso2.creditos)

class profesores:
    def __init__(self,nombre,experiencia,numprofesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__numprofesor=numprofesor
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre
    @property
    def experiencia(self):
        return self.__experiencia
    @experiencia.setter
    def experiencia(self, experiencia):
        self.__experiencia=experiencia
    @property
    def numprofesor(self):
        return self.__numprofesor
    @nombre.setter
    def nombre(self, numprofesor):
        self.__numprofesor=numprofesor
    def impartir():
        pass
    def evaluar():
        pass

profesor1=profesores("Lolito Paco",15,22222)
print(profesor1.nombre)
print(profesor1.experiencia)
print(profesor1.numprofesor)
    
    

