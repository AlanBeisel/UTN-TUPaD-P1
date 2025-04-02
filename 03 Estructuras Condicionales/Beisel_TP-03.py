##Actividades:

#   1) Es mayor de edad

print("Hola!")

edad= int(input("Por favor, Ingrese su edad:"))
if edad >= 18:
 print("Eres mayor de edad, podes ir en cana")
else: print("Eres menor de edad");

# 2) Nota de aprobado

print("Hola")
nota= int(input("Por favor ingrese su nota obtenida:"))
if nota >= 6:
 print("Felicidades, usted fue aprobado")
else: print("Usted lamentablemente ha desaprobado, suerte para la proxima")

# 3) Numeros par o impar
numero= int(input("por favor ingrese un numero"))
if numero % 2 == 0 : print(f"{numero} es un numero par")
else: print (f"{numero} es un numero impar")

#   4) Categoria segun edad
edad= int(input("Ingrese su edad, por favor:"))

if edad < 12:
 print("Niño")
elif edad >=12 and edad < 18:
 print("Adolecente")
elif edad >= 18 and edad < 30:
 print("Joven/ Adulto")
else: print("Adulto")

# 5) Ecribir contraseña

contraseña= input("ingrese una contraseña de entre 6 y 14 caracteres:")
if len(contraseña) >= 6 and len(contraseña) <= 14:
 print("ha ingresado una contraseña correcta")
else: print("por favor, ingrese una contraseña de entre 6 y 14 caracteres")

# 6)  Definiendo sesgo

import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
media_lista = mean(numeros_aleatorios)
mediana_lista= median(numeros_aleatorios)
moda_lista= mode(numeros_aleatorios)

print(f"Media: {media_lista}")
print(f"Mediana: {mediana_lista}")
print(f"Moda: {moda_lista}")

if media_lista > mediana_lista > moda_lista:
    print("Sesgo positivo (a la derecha)")
elif media_lista < mediana_lista < moda_lista:
    print("Sesgo negativo (a la izquierda)")
else:
    print("Sin sesgo")

# 7) Termina con vocal

frase = input("Ingrese una frase o palabra:")
ultima_letra = frase[-1]
vocales= "aeiou"

if ultima_letra.lower() in vocales:
  print(f"la ultima letra es:{ultima_letra} la cual es vocal")
else: print("la ultima letra no es vocal") 


# 8) Ingrese su nombre y opcion

nombre= input("Ingrese su nombre por favor: ")
print(f"Hola {nombre.capitalize()}")
opcion_seleccionada= int(input( "Precione 1. Si quiere su nombre en mayúsculas. \n" 
                                "Precione 2. Si quiere su nombre en minúsculas. \n"
                                "Precione 3. Si quiere su nombre con la primera letra mayúscula. \n"
                                "Ingrese una opcion: "))

if opcion_seleccionada == 1:
  print(nombre.upper())
elif opcion_seleccionada == 2:
  print(nombre.lower())
elif opcion_seleccionada == 3:
  print(nombre.capitalize())
else:
  print("Ingrese una opcion correcta")

# 9) Ingrese la magnitud del terremoto

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#10) Estacion del año

hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes del año (1-12): "))
dia = int(input("Ingrese el día del mes: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Verano")
    else:
        print("Otoño")
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Invierno")
    else:
        print("Primavera")
else:
    print("Hemisferio inválido")