"""Crear un programa, que tenga una variable 
con la cadena “Te quiero solo como amigo”,
 y muestre la siguiente información:

• Imprima los dos primeros caracteres."""

cadena = "Te quiero solo como amigo"
print(cadena[0 : 2])

"""• Imprima los tres últimos caracteres"""
print(cadena[-3 :])


"""• Imprima dicha cadena cada dos caracteres.
 Ej.: Si la cadena fuera “recta” debería 
 imprimir rca"""
print(cadena[: : 2])

"""• Dicha cadena en sentido inverso.
 Ej.: Si la cadena fuera hola mundo! 
 debe imprimir !odnum aloh"""
print(cadena[: : -1]) 

"""• Imprima la cadena en un sentido y en sentido
 inverso. Ej: Si la cadena es “reflejo”
  imprime reflejoojelfer."""
print(cadena + cadena[: : -1])


"""Crear un programa que tenga una variable
   con la cadena “Separado” y un carácter de
    coma (,); e inserte el carácter entre cada
     letra de la cadena. Ej: separar y , 
     debería devolver s,e,p,a,r,a,r"""
cadena = "Separado"
print(cadena)

reemplazar = cadena.replace("", ",")
print(reemplazar)