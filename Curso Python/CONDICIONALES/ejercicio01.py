"""Ejercicio 1

Crear un programa que pida al usuario una 
letra, y si es vocal, muestre el mensaje 
"Es vocal". Sino, decirle al usuario que no 
es vocal"""
print("Hola bienveido a su programa, que le ayudara a saber si una letra es vocal o no")

letra = input("Ingrese una letra: ")

if letra.lower() == "a":
    print("Es una vocal")
elif letra.lower() == "e":
    print("Es una vocal")
elif letra.lower() == "i":
    print("Es una vocal")
elif letra.lower() == "o":
    print("Es una vocal")
elif letra.lower() == "u":
    print("Es una vocal")
else:
    print("No es una vocal ")
