"""Realizar un programa que haga el proceso 
de formula general para la resolución de
ecuaciones, sabiendo que la formula general es
la que está en la imagen, el usuario debe
ingresar los valores de “a”, “b” y “c”, y el 
programa debe hacer el proceso para que al 
final muestre el mensaje: “La solución es:
 <solucion>”"""

from math import sqrt 

print("Hola, bienvenido a su programa, solucionador de la formula general")
Valor_A = float(input("ingrese el valor a "))
print("usted ha puesto:", Valor_A)

Valor_B = float(input("ingrese el valor b "))
print("usted ha puesto:", Valor_B)

Valor_C = float(input("ingrese el valor c "))
print("usted ha puesto:", Valor_C)

x1 = 0
x2 = 0

if((Valor_B ** 2)-( 4 * Valor_B  * Valor_C)) < 0:
 print("Estos datos ingresados no tienen valores reales")
else:
    x1 = (-Valor_B + sqrt((Valor_B**2)- (4*Valor_A*Valor_C)))/(2*Valor_A)
    x2 = (-Valor_B - sqrt((Valor_B**2)- (4*Valor_A*Valor_C)))/(2*Valor_A)
    print("La solucion es: \nx1= ", x1, "\nx2 = ", x2)
   
"""Se desea tener un algoritmo que permita
determinar y mostrar el promedio que ha 
obtenido un alumno en un determinado curso,
conociendo las notas de: tres prácticas, el
examen parcial y el examen final.
Considere:
PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
Donde: P1, P2, P3 : Practicas
PP: promedio de práctica
PROM: promedio
EP: examen parcial
EF: examen final"""
print("Bienvenid@ a tu programa, que te ayudara a evaluar a tus alumnos")
practica_1 = float(input("Hola, ingresa la calificacion obtenida en la practica 1: "))
practica_2 = float(input("Hola, ingresa la calificacion obtenida en la practica 2: "))
practica_3 = float(input("Hola, ingresa la calificacion obtenida en la practica 3: "))

examen_parcial = float(input("ingrese la califiacion obtenida en el examen parcial: "))
examen_final = float(input("ingrese la calificacion obtenida en el examen final: "))

promedio_practicas = (practica_1 + practica_2 + practica_3) / 3

calificacion_final = (promedio_practicas + 2 * examen_parcial + 3 * examen_final) / 6
print("Su calificacion obtenida es:",calificacion_final)