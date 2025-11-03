#Instanciar los objetos para posterior implementarlos 
from model import coches,cochesBD
import os

def borrarPantalla():
   os.system("cls") 

def esperaTecla():
    input("\n\t... Oprima una tecla para continuar ...")   

def datos_autos(tipo):
    borrarPantalla()
    print(f"\n\t ...Ingresar los datos del Vehiculo de tipo: {tipo}")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    potencia=int(input("Potencia: "))
    plazas=int(input("No. de plazas: "))
    return marca,color,modelo,velocidad,potencia,plazas

def imprimir_datos_vehiculo(marca,color,modelo,velocidad,potencia,plazas):
    print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n color: {color} \n Modelo: {modelo} \n velocidad: {velocidad} \n caballaje: {potencia} \n plazas: {plazas}")

def resultados_sql():
    
def resultas_insertar(respuesta,tipo):
    if respuesta:
        print("Registro insertado correctamente")
    else: 
        print("No fue posible insertar el registro, intenta lo nuevamente ...")
def autos():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Auto")
    coche=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    #Agregar en la BD
    auto=cochesBD.Autos(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    respuesta=auto.insertar()
    resultas_insertar(respuesta)
    return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas
            
def camionetas():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camioneta")
    traccion=input("Traccion: ").upper()
    cerrada=input("¿Cerrada (Si/No)?: ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False    
    coche=coches.Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"traccion: {coche.traccion}\n cerrada: {coche.cerrada}")

def camiones():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camiones")
    eje=int(input("No. de ejes: "))
    capacidadCarga=int(input("Capacidad de carga: "))
    coche=coches.Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"#Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")
def menu_opciones(tipo):
    print(f"\n\t\t .::Menu de {tipo}::. \n\t\t Insertar \n\t\t Consultar \n\t\t Actualizar \n\t\t Eliminar \n\t\t Regresar")
    opcion=input("\n\t\t Elige una opcion ").upper().strip()
    return opcion
def menu_autos():
    while True:
        borrarPantalla()
        menu_opciones()
        opcion=menu_opciones("Autos")
        if opcion=="1" or opcion=="INSERTAR":
            marca,color,modelo,velocidad,caballaje,plazas=autos()
            auto=cochesBD.Autos(marca,color,modelo,velocidad,caballaje,plazas)
            respuesta=auto.insertar()
            resultas_insertar(respuesta)
            esperaTecla()
        elif opcion=="2" or opcion=="CONSULTAR":
            borrarPantalla()
            registro=cochesBD.Autos.consultar()
            if len(registro)>0:
                num_autos=1
                for fila in registro:
                    print(f"\nAuto {num_autos} con ID: {fila(0)}\nMarca: {fila(1)}\nColor: {fila(2)}\nModelo {fila(3)}\nVelocidad{fila(4)}\n Potencia {fila(4)}")
                    num_autos=+1
                    esperaTecla() 
            else: 
                print("No existe datos para mostrar por el momento")
            print("consultar")
        elif opcion=="3" or opcion=="ACTUALIZAR":
            borrarPantalla()
            id=int(input("\n Ingresar el ID del auto a Actualizar "))
            marca,color,modelo,velocidad,caballaje,plazas=autos()
            respuesta=cochesBD.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas)
            
            esperaTecla()
            print("ACTUALIZAR")
        elif opcion=="4" or opcion=="ELIMINAR":
            print("ELIMINAR")
        elif opcion=="5" or opcion=="REGRESAR":
            break
        else:
            print("Opcion no valida intente de nuevo")

def main():
   opcion=True
   while opcion:
    os.system("cls")
    opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.- Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige un opción: ").lower().strip()
    match opcion:
        case "1":
            autos()
            esperaTecla()
        case "2":
            camionetas()
            esperaTecla()  
        case "3":
            camiones()
            esperaTecla()
        case "4":
            borrarPantalla()
            input("\n\t\tSalir del Sistema")
            opcion=False   
        case _:
            input("\n\tOpcion invalidad ... vuelva a intertarlo ... ")      

if __name__=="__main__":
    main()

