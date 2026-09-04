nota = int(input("cual es tu nota?"))
while(nota > 10 or nota < 1):
    print("nota no valida")
    nota = int(input("cual es tu nota?"))

if(nota >= 7 and nota <= 10):
    print("aprobado")
elif(nota >= 1 and nota < 7):
    print("desaprobado")