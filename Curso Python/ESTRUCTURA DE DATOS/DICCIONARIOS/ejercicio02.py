"""Ejercicio 2

Con el siguiente diccionario, debes crear un 
programa que pregunte al usuario por un 
número; el programa debe imprimir el jugador 
al que hace referencia ese número
{
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}"""

diccionario = {
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}

jugador = int(input("Ingrese el numero de su jugador: "))

if jugador in diccionario : 
    print("su jugador es:",diccionario[jugador])
else: 
    print("Este jugador aun no lo eh fichado")