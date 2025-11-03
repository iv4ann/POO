from tkinter import *
ventana=Tk()
ventana.title("Uso de labels")
ventana.geometry("600x400")
marco1=Frame(ventana,width=600,height=100,background="#00FFCC")
marco1.pack_propagate(False)
marco1.pack()

marco2=Frame(ventana,width=600,height=100,background="#00D5FF")
marco2.pack_propagate(False)
marco2.pack()

marco3=Frame(ventana,width=600,height=100,background="#0055FF")
marco3.pack_propagate(False)
marco3.pack()

marco4=Frame(ventana,width=600,height=100,background="#000ED1")
marco4.pack_propagate(False)
marco4.pack()

etiqueta1=Label(marco1,text="Carlos Manuel Rodriguez Sanchez",background="#00FFCC").pack(pady=40)
etiqueta2=Label(marco2,text="Universidad tecnologica de Durango",background="#00D5FF").pack(pady=40)
etiqueta3=Label(marco3,text="Tecnologias de la Informacion",background="#0055FF").pack(pady=40)
etiqueta4=Label(marco4,text="Desarrollo de Software multiplataforma",background="#000ED1",).pack(pady=40)

ventana.mainloop()