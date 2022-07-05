"""Escribir una función que calcule el total 
de una factura tras aplicarle el IVA. La 
función debe recibir la cantidad sin IVA y 
el porcentaje de IVA a aplicar, y devolver 
el total de la factura. Si se invoca la 
función sin pasarle el porcentaje de IVA, 
deberá aplicar un 21%."""

from re import M


def total():
    monto = float(input("Ingresa el precio del producto que estas comprando: "))
    iva = int(input("Ingrese el porcentaje que le roba el gobierno(IVA): "))

    if iva != 0:
        if iva > 0:
            totalPagar = ((monto * iva) / 100) + monto
            return totalPagar

        else:
            return "El monto de IVA es invalido, pague sus impuestos"

    

    else:    #0.21 es igual a 21%
        totalPagar = (monto * 0.21) + monto
        return totalPagar
        

print("Su compra es por:$ ",total()) 