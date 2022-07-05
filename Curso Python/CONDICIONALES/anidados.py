nombre = input("Bienveido a la estacion de la NASA, ¿Cual es su nombre?: ")
cargo = input("¿Que actividad realizas?: ")

if nombre == nombre.lower():
    if cargo == cargo.lower():
        print("Hola, bienvenido compañero")
    else: 
        print("ALERTA, UN INTRUSO")
else:
    print("Acuerdate que es con mayuscula")
