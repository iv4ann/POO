#Instanciar los objetos

from cocheslol import coches




marca=input("Ingresa la marca").lower()
color=input("Ingresa el color")
modelo=input("Ingresa el modelo del vehiculo")
velocidad=int(input("Ingresa la velocidad del vehiculo"))
potencia=int(input("Ingresa la potencia del vehiculo"))
plazas=int(input("Ingresa las plazas del vehiculo"))
coche1=coches(marca,color,modelo,velocidad,potencia,plazas)

print(f"Los datos del vehiculo son {coche1.marca} ")
