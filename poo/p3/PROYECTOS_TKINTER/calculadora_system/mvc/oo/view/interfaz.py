from tkinter import *
from controller import funciones

class Vistas():
    def __init__(self,ventana):
        ventana.geometry("600x400")
        ventana.title("Calculadora")
        ventana.resizable(False,False)
        self.interfaz(ventana)
        
    
    def interfaz(self,ventana):
        num1=IntVar()
        txtNum1=Entry(ventana,textvariable=num1,justify=CENTER,width=10)
        txtNum1.pack()
        num2=IntVar()
        txtNum2=Entry(ventana,textvariable=num2,justify=CENTER,width=10)
        txtNum2.pack(pady=20)

        btnSuma=Button(ventana,command=lambda: funciones.Controladores.operacion(num1.get(),num2.get(),"suma","+"),text="+ SUMA",border=4,relief=RIDGE)
        btnSuma.pack()

        btnResta=Button(ventana,command=lambda: funciones.Controladores.operacion(num1.get(),num2.get(),"resta","-"),text="- RESTA",border=4,relief=RIDGE)
        btnResta.pack()

        btnMulti=Button(ventana,command=lambda: funciones.Controladores.operacion(num1.get(),num2.get(),"multiplicacion","X"),text="* MULTIPLICACION",border=4,relief=RIDGE)
        btnMulti.pack()

        btnDivision=Button(ventana,command=lambda: funciones.Controladores.operacion(num1.get(),num2.get(),"division","/"),text="/ DIVISION",border=4,relief=RIDGE)
        btnDivision.pack()

        btnSalir=Button(ventana,command=ventana.quit,text="Salir",border=4,relief=RIDGE,background="#FF0000",activebackground="#810404")
        btnSalir.pack(pady=30)

def menu_principal(self, ventana):
    barra_menu = Menu(ventana)
    ventana.config(menu=barra_menu)

    operaciones_menu = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Operaciones", menu=operaciones_menu)

    operaciones_menu.add_command(label="Agregar", command=lambda: print("Agregar"))
    operaciones_menu.add_command(label="Consultar", command=lambda: print("Consultar"))
    operaciones_menu.add_command(label="Cambiar", command=lambda: print("Cambiar"))
    operaciones_menu.add_command(label="Borrar", command=lambda: print("Borrar"))
    operaciones_menu.add_separator()
    operaciones_menu.add_command(label="Salir", command=ventana.quit)

    resultado = Label(ventana, text="")
    resultado.pack()

