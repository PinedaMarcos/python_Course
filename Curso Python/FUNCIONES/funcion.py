"""un funcion es una secuencia de setencias que
realizan una operacion y que recibe un nombre.
cuando se define una funcion, se especifica
el nimbre y la secuencia de sentencias, para
mas adelante mandar a llamar a la funcion"""

"""Los parametros son variables que se definen al
declarar funciones, las cuales van a ser
utilizadas para enviar valores al hacer un
llamado a la funcion"""

"""un argumento son los valores que van a tomar
cada uno de los parametros que se han definido
en las funciones"""

#funciones en python
# type sirve para saber clase es:
num = "70"
print(type(num))

#para saber el dato maximo y el minimo en una lista

lista = [2,4,5,67,80,987]
print(max(lista))
print(min(lista))

#crear funciones

def saludo():
    print("Hola prros")
saludo()

def tabla7():
    for i in range(11):
        print("7 x {} = {}". format(i, i *7))
tabla7()