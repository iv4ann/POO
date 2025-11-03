from model import usuario,nota
import datetime
import getpass
from funciones import *

def user():
    nombre=input("\t ¿Cual es tu nombre?: ")
    apellidos=input("\t ¿Cuales son tus apellidos?: ")
    email=input("\t Ingresa tu email: ")
    password=getpass.getpass("\t Ingresa tu contraseña: ")
    fecha=datetime.datetime.now()
    usuar=usuario.Usuarios(nombre,apellidos,email,password,fecha)
    return usuar.nombre,usuar.apellidos,usuar.email,usuar.password,usuar.fecha

def notas(usuario_id):
    user_id=usuario_id
    titulo=input("\tTitulo: ")
    descripcion=input("\tDescripción: ")
    fecha=datetime.datetime.now()
    note=nota.Notas(user_id,titulo,descripcion,fecha)
    return note.id_user,note.titulo,note.descripcion,note.fecha

def confirmaciones(resultado):
    if resultado:
        print(f"\n \t \t.::Accion Realizada Correctamente ::.")
    else:
        print(f"\n \t \t** No fue posible realizar la accion **...")  

def menu_principal():
    while True:    
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registro
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1' or opcion=="REGISTRO":
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre,apellidos,email,password,fecha=user()
            resultado=usuario.Usuarios.registrar(nombre,apellidos,email,password,fecha)
            confirmaciones(resultado)
            esperarTecla()      
        elif opcion == '2' or opcion=="LOGIN":
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ")
            password=getpass.getpass("\t Ingresa tu Contraseña: ")
            #Agregar codigo 
            registro=usuario.Usuarios.iniciar_sesion(email,password)
            if registro:
                menu_notas(registro[0],registro[1],registro[2])
            else:
                print(f"\n\t Email y/o contraseña incorrectas... vuelva a intentarlo ...")
                esperarTecla()    
        elif opcion == '3' or opcion=="SALIR":
            print("\n\t.. ¡Gracias Bye! ...")
            #opc=False
            break
            #exit()
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        print("""
                  \n \t 
                      .::  Menu Notas ::. 
                  1.- Crear 
                  2.- Mostrar
                  3.- Cambiar
                  4.- Eliminar
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ").upper()

        if opcion == '1' or opcion=="CREAR":
            borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            usuario_id,titulo,descripcion,fecha=notas(usuario_id)
            #Agregar codigo
            resultado=nota.Notas.crear(usuario_id,titulo,descripcion,fecha)
            confirmaciones(resultado)
            esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            borrarPantalla()
            #Agregar codigo  
            registros=nota.Notas.mostrar(usuario_id)
            if len(registros)>0:
                print(f"\n\t {nombre} {apellidos}, tus notas son: ")
                num_notas=1
                for fila in registros:
                   print(f"\nNota: {num_notas} \nID: {fila[0]}.- Titulo: {fila[2]} Fecha de Creación: {fila[4]} \nDescripción: {fila[3]}") 
                   num_notas+=1    
            else:
                print(f"\n \t \t** No existen notas para el usuario ... vuelva a intentarlo **...")
            esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            id = input("\t \t ID de la nota a actualizar: ")
            ning,titulo,descripcion,fecha=notas(id)
            #Agregar codigo
            resultado=nota.Notas.actualizar(titulo,descripcion,fecha,id)
            confirmaciones(resultado)
            esperarTecla()      
        elif opcion == '4' or opcion=="ELIMINAR":
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            id = input("\t \t ID de la nota a eliminar: ")
            #Agregar codigo
            resultado=nota.Notas.eliminar(id)
            confirmaciones(resultado)
            esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
  menu_principal()

