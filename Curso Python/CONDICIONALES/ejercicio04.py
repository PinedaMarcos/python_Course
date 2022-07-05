"""Ejercicio 2

Crear un programa que permita al usuario 
elegir un candidato por el cual votar. Las 
posibilidades son: candidato A por el partido
rojo, candidato B por el partido verde, 
candidato C por el partido azul. Según el 
candidato elegido (A, B ó C) se le debe 
imprimir el mensaje “Usted ha votado por el 
partido [color que corresponda al candidato
elegido]”. Si el usuario ingresa una opción 
que no corresponde a ninguno de los candidatos
disponibles, indicar “Opción errónea”."""

voto = input("¿Por quien vas a votar crack?: ")

if voto.upper() == "A":
    print("Usted a votado por el candidado rojo")
elif voto.upper() == "B":
    print("Usted voto por el candidato color verde")
elif voto.upper() == "C":
    print("Usted voto por el candidato color azul")

else:
    print("No has votado por nadie, ¿Acaso no te importa el futuro de tu pais?")