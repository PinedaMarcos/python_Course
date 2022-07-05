"""Ejercicio 5

Crear un programa que tenga dos funciones, 
una que contenga el area de un cuadrado con 
argumentos de base y altura; y la otra el 
area de un circulo con argumento de radio"""

#definicion de la funcion
def areaCuadrado(base , altura):
    area = base * altura #formula del arae del cuadrado
    print(area)
#se manda a llamar la funcion
areaCuadrado(10, 10)

def areaCirculo(radio):
    return pow(radio, 2) * 3.14
print(areaCirculo(10))