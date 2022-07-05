"""Ejercicio 2
Realizar un programa en el cual se declaren 
dos valores enteros por teclado utilizando 
el método __init__. Calcular después la suma, 
resta, multiplicación y división. Utilizar 
un método para cada una e imprimir los 
resultados obtenidos. Llamar a la clase 
Calculadora."""

#clase
class Calculadora():
    def __init__(self):
        self.num1 = int(input("Ingrese el primer valor: "))
        self.num2 = int(input("Ingrese el segundo valor: "))

    def suma(self):
        self.suma = self.num1 + self.num2
        print("La suma es: " , self.suma)

    def resta(self):
        self.resta = self.num1 - self.num2
        print("La resta es: ", self.resta)

    def multiplicacion(self):
        self.multiplicacion = self.num1 * self.num2
        print("La multiplicacion es: ", self.multiplicacion)
 
    def division(self):
        self.resta = self.num1 / self.num2
        print("Su division es: ", self.division)

calcular = Calculadora()
calcular.suma()
calcular.resta()
calcular.multiplicacion()
calcular.division()

