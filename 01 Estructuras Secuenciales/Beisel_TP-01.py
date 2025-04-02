# Trabajo Practico N°1 Secuenciales, alumno Alan Beisel


# 1) Imprimir "Hola Mundo!"
print("Hola Mundo!")

# 2) Saludar al usuario por su nombre
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Pedir datos personales e imprimirlos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4) Calcular área y perímetro de un círculo

radio = float(input("Ingrese el radio del círculo: "))
pi = 3.14159
area = pi * radio * radio
perimetro = 2 * pi * radio
print(f"El área del círculo es {area:.2f} y el perímetro es {perimetro:.2f}")

# 5) Convertir segundos a horas
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

# 6) Imprimir la tabla de multiplicar de un número
numero = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7) Operaciones con dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2:.2f}")

# 8) Calcular el Índice de Masa Corporal (IMC)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su Índice de Masa Corporal es: {imc:.2f}")

# 9) Convertir temperatura de Celsius a Fahrenheit
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"La temperatura en Fahrenheit es {fahrenheit:.2f}°F")

# 10) Calcular el promedio de tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio:.2f}")
