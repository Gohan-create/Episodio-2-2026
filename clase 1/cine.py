#datos
asientoslim = 100
preciomenor = 300
preciomayor = 600
numero = 1
print("Buenos dias bienvenido al cine del Mendoza, que desea hacer hoy?")
while(numero != 3):
    print("precione 1 para comprar entradas")
    print("precione 2 para ver los datos")
    print("precione 3 para salir")
    numero = int(input("ingrese el numero:\n "))

    if(numero == 1):
        print("===========================================")
        cantEntradas = int(input("cuantas entradas desea comprar?"))
        if(cantEntradas <= asientoslim ):
            asientoslim = asientoslim - cantEntradas
            adultos = int(input("cuantos asientos son para adultos?\n"))
            while(adultos > cantEntradas):
                adultos = int(input("Cantidad no valida. Ingrese nuevamente:\n"))
            menores = cantEntradas - adultos
            costoAdulto = adultos*preciomayor
            costoMenor = menores*preciomenor
            costoTotal = costoAdulto + costoMenor
            print("===========================================")
            print("Entrada Asignada")
            print(f"Precio por Adultos: ${costoAdulto}")
            print(f"Precio por Menor: ${costoMenor}")
            print(f"Precio Total: ${costoTotal}")
            print("===========================================")
        elif(cantEntradas > asientoslim ):
            print("Cantidad de asientos no disponible")
        print("===========================================")

     elif(numero == 2):
        print("===========================================")
        print("precio de menores a 12: ", preciomenor)
        print("precio de mayores a 12: ", preciomayor)
        print("asientos disponibles: ", asientoslim)     
        print("===========================================")
    else:
        print("===========================================")
        print("numero invalido, vuelva a intentar")
        print("===========================================")

print("programa finalizado")