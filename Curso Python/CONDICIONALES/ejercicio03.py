"""Ejercicio 1

Escribe un programa que pida dos palabras
y diga si riman o no. Si coinciden las tres 
últimas letras tiene que decir que riman. Si 
coinciden sólo las dos últimas tiene que 
decir que riman un poco y si no, que no riman."""

# extraño <--> tamaño
# solo <--> amigo
# riman <--> cuerpo
print("Que onda, te ayudare para que tus rimas, queden chingonas y puedas pedir tu pollito KFC rimando")
palabra1 = input("ingresa la primer palabra: ")
palabra2 = input("ingrese la segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print("No riman, chale")
elif palabra1[-3 : ] == palabra2[-3 : ]:
    print("Eres un master rimando papi")
elif palabra1[-2 : ] == palabra2[-2 : ]:
    print("Vas bien, pero puedes mejorar crack")
else:
    print("No carnal, ¿la neta quieres ser rapero?")
