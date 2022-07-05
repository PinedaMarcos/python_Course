#clase
class FabricaTelefonos():
    marca = "Samsung"

# Metodo de instancia
    def elaboradorHuawei(self):
#self engloba un atributo a toda una clase
        marca = "Huawei"

telefono = FabricaTelefonos()
telefono.elaboradorHuawei()
print(telefono.marca)

# Init sera el constructor de una clase
class FabricaTelefonos():
    def _init_(self, marca, color):
        self.marca = marca
        self.color = color

telefono = FabricaTelefonos("Negro")
print(telefono.marca)