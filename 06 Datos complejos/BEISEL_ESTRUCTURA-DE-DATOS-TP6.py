
# Actividad 1: Agregar frutas nuevas al diccionario
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Actividad 2: Actualizar precios de algunas frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

# Actividad 3: Crear lista con solo los nombres de las frutas
frutas = list(precios_frutas.keys())
print("Frutas:", frutas)

# Actividad 4: Agenda telefonica de 5 contactos
agenda = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el numero de telefono: ")
    agenda[nombre] = numero

buscado = input("Ingrese el nombre a buscar en la agenda: ")
if buscado in agenda:
    print("Numero:", agenda[buscado])
else:
    print("Contacto no encontrado.")

# Actividad 5: Contar palabras unicas y su frecuencia
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras unicas:", palabras_unicas)

frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
print("Frecuencia de palabras:", frecuencia)

# Actividad 6: Ingresar notas de 3 alumnos y calcular promedios
alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"Promedio de {nombre}: {promedio:.2f}")

# Actividad 7: Operaciones con sets de estudiantes
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# Actividad 8: Diccionario de productos y stock
stock = {}
producto = input("Ingrese producto a consultar: ")
if producto in stock:
    print("Stock actual:", stock[producto])
    agregar = int(input("Cuantas unidades agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto no existe. Ingrese stock inicial: "))
    stock[producto] = nuevo_stock

# Actividad 9: Agenda con tuplas como clave
agenda_eventos = {
    ('Lunes', '10:00'): 'Reunion',
    ('Martes', '14:00'): 'Clase de programacion'
}
dia = input("Ingrese el dia: ")
hora = input("Ingrese la hora: ")
clave = (dia, hora)
if clave in agenda_eventos:
    print("Evento:", agenda_eventos[clave])
else:
    print("No hay eventos para ese dia y hora.")

# Actividad 10: Invertir diccionario de paises y capitales
paises = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago'
}
capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido:", capitales)
