# listas homogeneaas -> son del mismo dato
# listas heterogeneas -> son de distintos datos

lista = ['hello', 45 , 'prros', 512]
print(lista)

#para llamar un elemento de la lista
print(lista[3])

#para modificar un dato solo es necesario hacer
lista[1] = "PAPUS"
print(lista)

#debanado de listas
print(lista[0:4])

#para agregar elementos a una lista
lista.append(8)
print(lista)

#para agregar elementos a una lista en un lugar especifico
lista.insert(2 , "UAM")
print(lista)

#para saber cuantos elementos hay en una lista

lista1 = [1,2,3,5,6,6,11,8]
print(lista1.count(6))

#para ver en que posicion se encuntra un elemento
print(lista1.index(2))

#para ordenar una lista forma descendente
lista1.sort()
print(lista1)

#para ordenar una lista de forma ascendente
lista1.reverse()
print(lista1)

#elimiar datos de una lista
lista1.pop() #pop solo elimina el ultimo valor de la lista
print(lista1)

#eliminar datos de una lista, en la posicion que nosotros ocupemos
lista1.remove(11)
print(lista1)