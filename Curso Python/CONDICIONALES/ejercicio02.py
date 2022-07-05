"""Ejercicio 2

Escribir un programa que, dado un número
entero, muestre su valor absoluto. Nota: para
los números positivos su valor absoluto es  
igual al número (el valor absoluto de 52 es 
52), mientras que, para los negativos, su 
valor absoluto es el número multiplicado por
-1 (el valor absoluto de -52 es 52)."""
print("Bienveido a su programa, que le ayudara a saber el valor absoluto de un numero")

numero_absoluto = int(input("ingrese un numero:"))

if numero_absoluto > 0:
    print("El valor absoluto es {} es: {}".format(numero_absoluto, numero_absoluto))
else: 
    print("El valor absoluto es {} es: {}".format(numero_absoluto, abs(numero_absoluto)))