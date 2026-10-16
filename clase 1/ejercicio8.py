for palabra in "Johann":
    print(palabra)

print("===================")

for numero in range(1,11):
    print(numero)

print("===================")

for cuenta in range(200,300,2):
    print(cuenta)

print("===================")

for regresiva in range(10,0,-1):
    print(regresiva)
print("DESPEGUE")

print("===================")

numero1 = int(input("elige un numero\n"))
for multiplicacion in range(1,11):
    resultado = numero1 * multiplicacion
    print(numero1, "*", multiplicacion ,"=" ,resultado)

print("===================")

notas = [10, 5, 4, 8, 3, 5, 7, 8, 9, 10, 1]
sumatoria = 0
for nota in notas:
    sumatoria += nota
cantNotas = len(notas)
promedio = sumatoria / cantNotas
print("el promedio es ", promedio)