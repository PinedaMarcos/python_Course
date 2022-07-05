"""Ejercicio 1
Escribir un programa que solicite al usuario
un vocal en minuscula, y luego una letra en 
mayúsculas. El programa debe convertir la 
letra en minúscula y la vocal en mayúscula, 
y al final, deben ser concatenadas ambas"""

vocal = input("Hola, por favor ingrese una vocal EN MINUSCULA: ")
consonante = input("Hola, ingresa una consonante EN MAYUSCULA: ")

vocal = vocal.upper()
consonante = consonante.lower()

print("La consonante es: {} \nLa vocal es: {}".format(consonante, vocal))

