#ver los valores
class A():

    def __init__(self):
        self._cuenta = 0 
        self._contador = 0
#metodo get
    @property    
    def cuenta(self):
        return self._cuenta

    @property
    def contador(self):
        return self._contador

a = A()
#print(a.contador)
print(a.cuenta)
print(a.contador)