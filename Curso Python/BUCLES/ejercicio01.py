"""Ejercicio 1

Escribir un programa que pida un numero al 
usuario y muestre las tablas de multiplicar 
de ese numero"""

numero = int(input("Ingrese el numero para que conozcas su tabla de multiplicar"))

i = 0
multiplicacion = 0

while i <= 10:
    multiplicacion = numero * i
    print("{} x {} = {}".format(numero, i, multiplicacion))
    i += 1
