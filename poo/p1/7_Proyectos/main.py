import os
os.system("cls")
from coches import *

def imprimir_datos_vehiculos(marca,color,modelo,velocidad,potencia,plazas):
    print(f"✅ Los datos del vehiculo son: {marca}, {modelo}, {color,velocidad,potencia,plazas}")
def datos_autos(tipo):
    print("\n📌 Ingresar los datos del vehiculo de tipo:{tipo}")
    marca = input("Ingresa la marca: ").lower()
    color = input("Ingresa el color: ")
    modelo = input("Ingresa el modelo de la camioneta: ")
    velocidad = int(input("Ingresa la velocidad: "))
    potencia = int(input("Ingresa la potencia: "))
    plazas = int(input("Ingresa las plazas: "))
    return marca,color,modelo,velocidad,potencia,plazas
def autos(): 
    print("\n📌 Datos del vehículo")
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("auto")
    coche1 = coches(marca, color, modelo, velocidad, potencia, plazas)
    imprimir_datos_vehiculos(coche1.marca,coche1.color,coche1.modelo,coche1.velocidad,coche1.potencia,coche1.plazas)
    
    print(f"coche1.marca,coche1.color,coche1.modelo,coche1.velocidad,coche1.potencia,coche1.plazas")
def camionetas(): 
    print("\n📌 Datos de la camioneta")
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("camioneta")
    traccion = input("Ingresa el tipo de tracción (4x2, 4x4): ")
    cerrada = input("¿Es cerrada? (si/no): ").lower() == "si"
    camioneta1 = Camioneta(marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada)
    print(f"✅ Camioneta {camioneta1.marca}, {camioneta1.traccion}, cerrada={camioneta1.cerrada}")

def camiones(): 
    print("\n📌 Datos del camión")
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("camion")
    ejes = int(input("Número de ejes: "))
    capacidad = int(input("Capacidad de carga (kg): "))
    camion1 = Camion(marca, color, modelo, velocidad, potencia, plazas, ejes, capacidad)
    print(f"✅ Camión {camion1.marca}, {camion1.modelo}, capacidad {camion1.capacidad_carga} kg")

# Menú con lista y for
opciones = ["Autos", "Camionetas", "Camiones", "Salir"]

while True:
    print("\n📌 Menú Principal")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

    eleccion = input("Seleccione una opción: ")

    match eleccion:
        case "1":
            autos()
            input("Presione Enter para continuar...")
        case "2":
            camionetas()
            input("Presione Enter para continuar...")
        case "3":
            camiones()
            input("Presione Enter para continuar...")
        case "4":
            print("👋 Saliendo del programa...")
            break
        case _:
            print("❌ Opción inválida, intente de nuevo.")
