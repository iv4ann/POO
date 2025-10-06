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
    
coche1=coches()
coche1.__color="blanco"
coche1.__marca="VW"
coche1.__modelo="2022"
coche1.__velocidad=220
coche1.__caballaje=150
coche1.__plazas=5
print(f"Los valores del objeto 1 son: {coche1.__marca},{coche1.__color},{coche1.__velocidad},{coche1.__modelo},{coche1.__caballaje},{coche1.__plazas}")

coche2=coches()
coche2.__color="azul"
coche2.__marca="Nissan"
coche2.__modelo="2020"
coche2.__velocidad=180
coche2.__caballaje=150
coche2.__plazas=6
print(f"Los valores del objeto 1 son: {coche2.__marca},{coche2.__color},{coche2.__velocidad},{coche2.__modelo},{coche2.__caballaje},{coche2.__plazas}")