"""Ejercicio 2

Escribir un programa que pregunte al usuario 
su edad y muestre por pantalla todos los años 
que ha cumplido (desde 1 hasta su edad)."""

edad = int(input("Digita tu edad, para que te muestre tus años: 1"))
i = 1

while i != edad:
    print("Has cumplido", i, "años")
    i += 1
