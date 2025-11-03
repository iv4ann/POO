from PIL import Image

class Imagenlol:
    def __init__(self,imagen):
        self.imagen= Image.open(ruta)

    def dimensiones_figura(self,ancho,alto):
        nueva_dimension=self.imagen.resize((ancho,alto))
        nueva_dimension.show()

ruta=r"C:\Users\marti\OneDrive\Escritorio\modelo_tenis\hogrider.jpg"
editar=Imagenlol(ruta)
editar.dimensiones_figura(777,777)