#modificar los valores
class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

#metodos get
    @property
    def cuenta(self):
        return self._cuenta
#metodo set
    @cuenta.setter
    def cuenta(self, cuenta):
        self._cuenta

#metodo get
    @property
    def contador(self):
        return self._contador

#metodo get
    @contador.setter
    def contador(self, contador):
        self._contador = contador

a = A()
print(a.cuenta)
a._cuenta = 20
print(a.cuenta)
a.contador = 100
print(a.contador)

