from tkinter import *
def cambiar_texto():
    lblEmail.config(text="Carlos Manuel Rodriguez Sanchez")
    lblPass.config(text="1234")
def regresar_texto():
    lblEmail.config(text="Correo electronico",font=("VERDANA",24))
    lblPass.config(text="Contraseña",font=("VERDANA",24))

ventana=Tk()
ventana.title("Inicio de sesion")
ventana.geometry("800x600")
fmTitulo=Frame(ventana,width=800,height=100,background="#C793E1")
fmTitulo.pack_propagate(False)
fmTitulo.pack()
lblTitulo=Label(fmTitulo,text="Inicio de sesion",font=("VERDANA",36),background="#C793E1").pack(pady=20)
lblEmail=Label(ventana,text="Correo electronico",font=("VERDANA",24))
lblEmail.pack(anchor="w")
lblPass=Label(ventana,text="Contraseña",font=("VERDANA",24))
lblPass.pack(anchor="w",pady=100)
btnIngresar=Button(ventana,text="Iniciar sesion",font=("Verdana",24),command=cambiar_texto).pack()
btnRegresar=Button(ventana,text="Regresar",font=("Verdana",24),command=regresar_texto).pack(pady=10)



ventana.mainloop()