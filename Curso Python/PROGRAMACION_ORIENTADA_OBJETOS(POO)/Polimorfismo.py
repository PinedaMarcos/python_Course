"""modificacion de metodos, cuando se heredan
de las clases."""

class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)
    
class Perro(Animales):
        def hablar(self):
            print("Yo no hablo, soy un prro wex")
    
class Pez(Animales):
    def hablar(self):
        print("Yo no hablo, soy un pez Wex")

perro = Perro("Guau")
perro.hablar()