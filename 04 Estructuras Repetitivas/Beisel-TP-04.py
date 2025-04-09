#1) Números del 0 al 100:
for numero in range(101):
    print(numero)


#2) Cantidad de dígitos de un número:

numero = int(input("Ingresa un número entero: "))
cantidad_digitos = 0
numero_abs = abs(numero)
while numero_abs > 0:
    numero_abs //= 10
    cantidad_digitos += 1

if numero == 0:
  cantidad_digitos = 1
print("El número tiene", cantidad_digitos, "dígitos.")

#3) Suma de números entre dos valores:

valor1 = int(input("Ingresa el primer valor: "))
valor2 = int(input("Ingresa el segundo valor: "))

if valor1 > valor2:
    valor1, valor2 = valor2, valor1

suma = 0
for numero in range(valor1 + 1, valor2):
    suma += numero

print("La suma es:", suma)

#4) Suma de números hasta que se ingresa 0:

suma = 0
numero = int(input("Ingresa un número (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingresa otro número (0 para terminar): "))

print("La suma total es:", suma)

#5) Juego de adivinanza:

import random

numero_aleatorio = random.randint(0, 9)
intentos = 0

while True:
    intento_usuario = int(input("Adivina el número (0-9): "))
    intentos += 1

    if intento_usuario == numero_aleatorio:
        print("¡Correcto! Adivinaste en", intentos, "intentos.")
        break
    elif intento_usuario < numero_aleatorio:
        print("El número es mayor.")
    else:
        print("El número es menor.")

#6) Números pares del 100 al 0:

for numero in range(100, -1, -2):
    print(numero)

#7) Suma de números hasta un valor dado:

valor_limite = int(input("Ingresa un número entero positivo: "))

suma = 0
for numero in range(valor_limite + 1):
    suma += numero

print("La suma es:", suma)

#8) Conteo de números pares, impares, positivos y negativos:

cantidad_pares = 0
cantidad_impares = 0
cantidad_positivos = 0
cantidad_negativos = 0

for _ in range(100):
    numero = int(input("Ingresa un número entero: "))

    if numero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1

    if numero > 0:
        cantidad_positivos += 1
    elif numero < 0:
        cantidad_negativos += 1

print("Pares:", cantidad_pares)
print("Impares:", cantidad_impares)
print("Positivos:", cantidad_positivos)
print("Negativos:", cantidad_negativos)

#9) Media de 100 números:

suma = 0

for _ in range(100):
    numero = int(input("Ingresa un número entero: "))
    suma += numero

media = suma / 100
print("La media es:", media)

#10) numero = int(input("Ingresa un número entero: "))
numero_invertido = 0

while numero > 0:
    ultimo_digito = numero % 10
    numero_invertido = numero_invertido * 10 + ultimo_digito
    numero //= 10

print("El número invertido es:", numero_invertido)