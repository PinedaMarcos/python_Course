from calendar import prcal


conjunto = {1, 2, 2, 3, 3, 4, 5, 6}

print(conjunto)
#en una lista si se muestran los valores repedidos, en un conjunto no

#para añadir
conjunto.add(34)
print(conjunto)

#para eliminar
conjunto.remove(3)
print(conjunto)
 
#para eliminar numero al azar
conjunto.pop()
print(conjunto)

#para añadir elementos
conjunto.update([45 ,2103])
print(conjunto)