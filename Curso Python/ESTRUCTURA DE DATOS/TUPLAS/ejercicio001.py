"""Ejercicio 1

Escribir una tupla con los meses del año, 
luego, pide al usuario un numero, el que haya 
ingresado, es el mes que debe mostrar en la 
tupla"""

print("Hola, Bienvenido a su calendario digital")
tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
opcionMes = int(input("Ingrese un numero para que sepas que mes es: "))

print("El mes es:", tupla[opcionMes -1])