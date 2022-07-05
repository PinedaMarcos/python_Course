"""Los metodos son funciones, pero en POO pasan a llamarse metodos,
los cuales hacen los objetos. Ejemplo: si una clase crea un objeto 
persona, el metodo puede ser hablar."""
#Los metodos van enfocados a las clases

"""Los atributos son caracteristicas, cualidades o descripciones que´
los objetos tienen. Es decir son datos que tienen los objetos, ejemplo:
un carro, tiene llantas, un color, una marca"""
#Los atributos van enfocados a los objetos

#clase
class FabricaTelefonos():
#Atributos
   marca = "Huawei"
   color = "Negro"
   memoriaRam = 32
   almacenamiento = 128
#Metodos
#Los metodos que se crean se llaman metodos de instancia
   def llamar(self, mensaje):
    return mensaje

    def escucharMusica(self):
        print("Estas escuchando Mùsica")

#creacion del objeto
telefono = FabricaTelefonos()
#agregamos los atributos
telefono.marca
telefono.color
telefono.memoriaRam
telefono.almacenamiento

telefono.escucharMusica
print(telefono.llamar("Hola, ¿Quien habla?"))
print(telefono.marca)