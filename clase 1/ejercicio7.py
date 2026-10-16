numero = 1
numeroaux = numero - 1
divisores = 2
while(numero > 1):
    resto = numero % numeroaux
    if(resto == 0):
        divisores + 1

    numeroaux = numeroaux - 1

if(divisores > 2):
    print(numeroaux)
