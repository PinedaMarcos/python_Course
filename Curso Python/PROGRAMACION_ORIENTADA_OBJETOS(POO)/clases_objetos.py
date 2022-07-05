"""La clase es una entidad que define una serie de elementos
que determiann un estado (datos) y un comportamiento
(operacines sobre los datos que modifican su estado)"""

"""Los objetos son un nivel elemental, un objeto es
simplemente un trozo de codigo mas estructuras de
datos, mas pequeños que un programa completo"""

#Sintaxis para craer una clase

"""class <Nombre de la clase>():
    pass"""

#se recomienda que la primera letra de nuestra clase se ponga en mayuscula
class FabricaTelefonos():
    pass
print(type(FabricaTelefonos)) 

#Apartir de una clase, se crean los objetos

celular = FabricaTelefonos()
celular2 = FabricaTelefonos()
print(type(celular))
print(type(celular2))