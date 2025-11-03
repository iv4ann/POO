'''
from tkinter import *
def clickarSaludar():
    lblSaludo.config(text=f"Hola,bienvenido {nombre.get()}")

ventana=Tk()
ventana.title("Uso del entry")
ventana.geometry("400x600")

lblTitulo=Label(ventana,text="Ingrese su nombre:")
lblTitulo.pack()

nombre=StringVar()

txtNomb=Entry(ventana,width=30,textvariable=nombre)
txtNomb.pack()

btnSaludar=Button(ventana,text="Saludar",command=clickarSaludar)
btnSaludar.pack()

lblSaludo=Label(ventana,text="")
lblSaludo.pack()


ventana.mainloop()
'''
from tkinter import *
def ingresar():
    usuario=txtNomb.get()
    password=txtPass.get()
    if len(password)>0:
        lblMens.config(text=f"Bienvenido {usuario}")
        txtNomb.config(state="readonly")
        txtPass.config(state="readonly")
    else:
        lblMens.config(text="Debe de ingresar una contraseña")
def borrar():
    txtNomb.delete(0,END)
    txtPass.delete(0,END)
    color_defecto = ventana.cget("bg")
    lblMens.config(text="",
                font=("Comic Sans MS",12),
                width=20,
                background=color_defecto
                )
    txtNomb.config(state="normal")
    txtPass.config(state="normal")

ventana=Tk()
ventana.title("Uso del entry")
ventana.geometry("400x600")
ventana.config(background="lightgray")

lblTitulo=Label(ventana,
                text="Ingreso al sistema",
                font=("Comic Sans MS",18),
                background="#FFA3F6",
                width=400
                )
lblTitulo.pack()

lblUser=Label(ventana,
                text="Introduzca su usario",
                font=("Comic Sans MS",12),
                background="#FFA3F6",
                width=20
                )
lblUser.pack(pady=20)

txtNomb=Entry(ventana,width=30)
txtNomb.pack()

lblPass=Label(ventana,
                text="Introduzca su contraseña",
                font=("Comic Sans MS",12),
                background="#FFA3F6",
                width=20
                )
lblPass.pack(pady=20)

txtPass=Entry(ventana,width=30,show="*")
txtPass.pack()

btnIng=Button(ventana,text="Ingresar",font=("Comic Sans MS",12),command=ingresar)
btnIng.pack(pady=20)
btnBorrar=Button(ventana,text="Borrar",font=("Comic Sans MS",12),command=borrar)
btnBorrar.pack(pady=10)

lblMens=Label(ventana,
                text="",
                font=("Comic Sans MS",10),
                width=30,
                background="lightgray"
                )
lblMens.pack(pady=20)

ventana.mainloop()


