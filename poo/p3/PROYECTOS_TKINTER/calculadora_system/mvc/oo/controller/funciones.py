from tkinter import messagebox
from model import operaciones
class Controladores():
    @staticmethod
    def operacion(a,b,op,caracter):
        match op:
            case "suma":
                opera=a+b
                
            case "resta":
                opera=a-b
            case "multiplicacion":
                opera=a*b
            case "division":
                opera=a/b
        messagebox.showinfo(message=f"El resultado de {a} {caracter} {b} es: {opera}",title=op)
        respuesta=messagebox.askquestion(message=f"Quieres insertarlo en la base de datos").lower()
        if respuesta=="yes":
            operaciones.Operaciones.crear(a,b,caracter,opera)
        else:
            pass