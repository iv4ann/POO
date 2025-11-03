from tkinter import *
def clickar():
    lblTitulo.config(text="Boton pulsado",fg="#C01D1D",background="#000000",cursor="SPIDER")
def regresar():
    lblTitulo.config(background="#C01D1D",
    text="Bienvenidos a TKinter",
    font=("Comic Sans MS",24),
    fg="#000000"
    )


ventana=Tk()
ventana.title("Bienvenido a tkinter")
ventana.geometry("500x500")

lblTitulo=Label(
    ventana,
    width=50,
    height=4,
    background="#C01D1D",
    text="Bienvenidos a TKinter",
    font=("Comic Sans MS",24),
    fg="#000000"
    )
lblTitulo.pack(pady=25)

btnClickar=Button(ventana,text="Clickar",font=("Comic Sans MS",24),command=clickar)
btnClickar.config(
    font=("Comic Sans MS",24),
    background="#C4D31E",
    fg="#000000",
    activeforeground="#C4D31E",
    activebackground="#000000"
    )
btnClickar.pack()


btnRegresar=Button(ventana,text="Regresar",command=regresar)
btnRegresar.config(
    font=("Comic Sans MS",24),
    background="#C4D31E",
    fg="#000000",
    activeforeground="#C4D31E",
    activebackground="#000000"
    )
btnRegresar.pack(pady=20)

ventana.mainloop()
