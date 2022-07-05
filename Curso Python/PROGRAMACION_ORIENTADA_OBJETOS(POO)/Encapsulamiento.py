class A():
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador
    
a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
