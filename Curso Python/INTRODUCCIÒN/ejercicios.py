"""realize un programa que realice 
la siguiente operacion aritmetica"""

x = 3
y = 2
c = 2
z = 5

operacion = ((x+y)/(c*z))**y
print(operacion)

"""Una juguetería tiene mucho éxito en dos
 de sus productos: payasos y muñecas. Suele 
 hacer venta por correo y la empresa de
  logística les cobra por peso de cada
   paquete, así que deben calcular el peso
    de los payasos y muñecas que saldrán en
     cada paquete a demanda. Cada payaso 
     pesa 112 g y cada muñeca 75 g. 
     Un cliente frecuente pide la cantidad 
     de 23 payasos y 54 muñecas, realiza un
      programa que muestre el peso total de
       toda la venta."""
PESOPAYASO = 112
PESOMUÑECA = 75

payasos_pedidos = 23
muñecas_pedidas = 54

peso_total = PESOPAYASO*payasos_pedidos + PESOMUÑECA*muñecas_pedidas

print("el peso total de su pedido es:",peso_total,"grs")
