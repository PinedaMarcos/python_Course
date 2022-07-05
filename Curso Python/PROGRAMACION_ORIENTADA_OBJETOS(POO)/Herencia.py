"""la herencia son 2 o mas clases, y que
se hereden (padre e hijas)"""
#clase
class Animales():
# metodo
   def habla(self):
    print("Yo soy un animal")

   def descripcion():
        print("Yo soy un {}".format(self.animal))
#clase heredando los metodos de animales
class Perro(Animales):
    pass #no vamos a colocar nada 
#clase
class Abeja(Animales):
    def __init__(self, animal):
        self.animal = animal
#objeto
animal = Animales()
animal.habla()
#perro ha heredado de animales
perro = Perro()
perro.habla()

abeja = Abeja("Abeja")
abeja.descripcion()