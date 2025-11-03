from tkinter import *
ventana=Tk()
ventana.title("Mi segunda app de tk")
ventana.geometry("1000x600")
ventana.resizable(FALSE,FALSE)
marco1=Frame(ventana,width=800,height=400,background="gray",relief=GROOVE,border=6)
marco1.pack_propagate(False)
marco1.pack(pady=100)#Es importante para que se muestre el objeto en la ventana
marco2=Frame(marco1, width=400,height=200,background="pink",relief=RIDGE,border=5).pack(pady=100)
ventana.mainloop()

