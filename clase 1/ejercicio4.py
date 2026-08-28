nota = int(input("cual es la nota que te sacaste?\n"))
if(nota >= 9 and nota <= 10):
    print("promocionado")
elif(nota >= 7 and nota <= 8):
    print("aprobado")
elif(nota >= 1 and nota <= 6):
    print("desaprobado")
else:
    print("mentiroso")
