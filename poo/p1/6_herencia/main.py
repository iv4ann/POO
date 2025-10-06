#Instanciar los objetos
import os
os.system("cls")
from coches import coches,Camioneta,Camion


coche1=coches("w","BLANCO","2020",3,3,3)
camioneta1=Camioneta("Nissan","Amarillo","2025",220,3,32,2,2)
camion=Camion("Nissan","Amarillo","2025",220,3,32,2,2)
"""
marca=input("Ingresa la marca").lower()
color=input("Ingresa el color")
modelo=input("Ingresa el modelo del vehiculo")
velocidad=int(input("Ingresa la velocidad del vehiculo"))
potencia=int(input("Ingresa la potencia del vehiculo"))
plazas=int(input("Ingresa las plazas del vehiculo"))
coche1=coches(marca,color,modelo,velocidad,potencia,plazas)

print(f"Los datos del vehiculo son {coche1.marca} ")
"""
print(coche1.marca, coche1.acelerar())
print(camioneta1.marca, camioneta1.acelerar())
print(camion.marca, camion.acelerar())