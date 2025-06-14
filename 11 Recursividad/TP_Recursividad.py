##Ejercicio 1

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# Mostrar los factoriales
def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")

# Ejemplo
mostrar_factoriales(5)


##Ejercicio 2


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def imprimir_serie_fibonacci(hasta):
    for i in range(hasta + 1):
        print(f"fibonacci({i}) = {fibonacci(i)}")

# Ejemplo
imprimir_serie_fibonacci(6)


##Ejercicio 3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# Ejemplo
print(potencia(2, 4))  # 16



##Ejercicio 4

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

# caso n = 0 para que no devuelva cadena vacía:
def convertir_a_binario(n):
    if n == 0:
        return "0"
    return decimal_a_binario(n)

# Ejemplo
print(convertir_a_binario(10))  # "1010"


##Ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Ejemplos
print(es_palindromo("reconocer"))  # True
print(es_palindromo("python"))     # False


##Ejercicio 6


def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# Ejemplos
print(suma_digitos(1234))  # 10
print(suma_digitos(9))     # 9
print(suma_digitos(305))   # 8


#ejercicio 7

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# Ejemplos
print(contar_bloques(1))  # 1
print(contar_bloques(2))  # 3 (2+1)
print(contar_bloques(4))  # 10 (4+3+2+1)


##Ejercicio 8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

# Ejemplos
print(contar_digito(12233421, 2))  # 3
print(contar_digito(5555, 5))      # 4
print(contar_digito(123456, 7))    # 0

