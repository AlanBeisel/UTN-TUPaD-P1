# 1. Imprimir hola mundo
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# 2. saludo personalizado
def saludar_usuario(nombre):
    return f"¡Hola {nombre}!"

nombre_usuario = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

# 3. Información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4. area y perímetro del círculo
import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio_circulo = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio_circulo)
perimetro = calcular_perimetro_circulo(radio_circulo)
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# 5. Segundos a horas
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

cantidad_segundos = int(input("Ingrese la cantidad de segundos: "))
horas_equivalentes = segundos_a_horas(cantidad_segundos)
print(f"{cantidad_segundos} segundos equivalen a {horas_equivalentes:.2f} horas.")

# 6. tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero_tabla = int(input("Ingrese el número para la tabla de multiplicar: "))
tabla_multiplicar(numero_tabla)

# 7. operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(num1, num2)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]:.2f}")

# 8. Calcular IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso_usuario = float(input("Ingrese su peso en kilogramos: "))
altura_usuario = float(input("Ingrese su altura en metros: "))
imc_calculado = calcular_imc(peso_usuario, altura_usuario)
print(f"Su Índice de Masa Corporal (IMC) es: {imc_calculado:.2f}")

# 9. Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C equivalen a {temperatura_fahrenheit:.2f}°F.")

# 10. Calcular promedio
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num_a = float(input("Ingrese el primer número: "))
num_b = float(input("Ingrese el segundo número: "))
num_c = float(input("Ingrese el tercer número: "))
promedio_calculado = calcular_promedio(num_a, num_b, num_c)
print(f"El promedio de los tres números es: {promedio_calculado:.2f}")