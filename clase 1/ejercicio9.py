import random 

num = random.randint(1,10)

intento = 0

while(intento < 3):
    respuesta = int(input("Intenta adivinar el numero\n"))

    if (respuesta == num):
        print("Felicidades, si era ", num)

    else:
        print("oooh que mal, era ", num)
        intento = intento + 1
        num = random.randint(1,10)

print("lo siento se acabaron los intentos")