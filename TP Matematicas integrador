# 1 - Ingreso de los DNIs (reales o ficticios).
#se guarda en la variable correspondiente de la A a la F
A = input("Victor ingrese su dni: ")
B = input("Milagros ingrese su dni: ")
C = input("Santiago ingrese su dni: ")
D = input("Alan ingrese su dni: ")
E = input("Julieta ingrese su dni: ")

# 2 - A partir de los DNIs, se deben formar tantos conjuntos de dígitos únicos como integrantes tenga el grupo.

dnis = [A, B, C, D, E] #creo un conjunto con todos los números

#Generación automática de los conjuntos de dígitos únicos.
conjuntos = [set(dni) for dni in dnis] #crear un conjunto (set) a partir de una colección de datos como una lista

# Mostrar los conjuntos generados a partir de los DNIs
nombres = ["Victor", "Milagros", "Santiago", "Alan", "Julieta"]

print("\nConjuntos de dígitos únicos por integrante:")
for i in range(len(dnis)):
    print(f"{nombres[i]} ({dnis[i]}): {conjuntos[i]}")

# 3 - Realizar entre esos conjuntos las siguientes operaciones: unión, intersección, diferencia (entre pares) y diferencia simétrica.

#Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.

#Calcula la union de los conjuntos
union_abc = conjuntos[0] | conjuntos [1] | conjuntos [2]
union_de = conjuntos[3] | conjuntos [4]

#Calcula la interseccion de los conjuntos
intersecion_abc = conjuntos[0] & conjuntos[1] & conjuntos [2]
intersecion_cd = conjuntos[3] & conjuntos[4]

#Calcula la diferencia de los conjuntos
diferencia_ab = conjuntos[0] - conjuntos[1]
diferencia_ba = conjuntos[1] - conjuntos[0]
diferencia_cd = conjuntos[2] - conjuntos[3]
diferencia_dc = conjuntos[3] - conjuntos[2]
diferencia_de = conjuntos[4] - conjuntos[3]
diferencia_ed = conjuntos[3] - conjuntos[4]

#Calcula la diferencia simetrica de los conjuntos
diferencia_simetrica_abc = (conjuntos[0] ^ conjuntos[1]) ^ conjuntos[2]
diferencia_simetrica_de= conjuntos[3] ^ conjuntos[4]

#Se muestra todos los resultados
print("\nUnión A y B y C:", union_abc)
print("Unión D y E:", union_de)
print("\nIntersección A y B y C:", intersecion_abc)
print("Intersección D y E:", intersecion_cd)
print("\nDiferencia A - B:", diferencia_ab)
print("Diferencia B - A:", diferencia_ba)
print("Diferencia C - D:", diferencia_cd)
print("Diferencia D - C:", diferencia_dc)
print("Diferencia E - D:", diferencia_de)
print("Diferencia D - E:", diferencia_ed)
print("\nDiferencia simétrica A y B y C:", diferencia_simetrica_abc)
print("Diferencia simétrica D y E:", diferencia_simetrica_de)

# Conteo de frecuencia de dígitos (0-9) en cada DNI
print("\nConteo de frecuencia de cada dígito en cada DNI:")
#Ciclo for para conteo de digitos en todos los DNIs en lista
for i in range(len(dnis)):
    dni = dnis[i]
    nombre = ["Victor", "Milagros", "Santiago", "Alan", "Julieta"][i]
    frecuencias = {}  # Diccionario vacío

    for digito in dni:
        if digito in frecuencias:
            frecuencias[digito] += 1
        else:
            frecuencias[digito] = 1

    print(f"\n--- DNI de {nombre}: {dni}----")
    for digito in sorted(frecuencias.keys()):
        print(f"  Dígito {digito}: {frecuencias[digito]} veces")

#Suma total de los dígitos de cada DNI.
for dni in dnis:
    suma = sum(int(d) for d in dni) #convertir los caracteres a enteros y sumarlos
    print(f"\n DNI: {dni} → Suma de dígitos: {suma}")


# 5 - Redactar al menos dos expresiones lógicas en lenguaje natural, que puedan luego implementarse en Python y escribir en la documentación que van a presentar cuál sería el resultado con los conjuntos que tienen.

# Expresión 1: "Si todos los conjuntos tienen al menos 5 elementos, hay diversidad adecuada."
P = all(len(conj) >= 5 for conj in conjuntos)  # True si TODOS los conjuntos tienen al menos 5 elementos
Q = "hay diversidad adecuada"  # Esto es simbólico (podría ser un booleano o string)

print("\n--- Expresión Lógica 1 ---")
print(f"¿Todos los conjuntos tienen al menos 5 elementos? {P}")
print(f"Condicional P → Q: 'Si P es verdadero, entonces {Q}.'")
print(f"P es {P}, porque no todos los conjuntos tienen 5 elementos. En la lógica proposicional, cuando el condicional P → Q tiene un antecedente falso (P), el condicional es {'verdadero' if not P else 'falso'} por defecto (esto se llama condicional material).")

# Expresión 2: "Si algún dígito aparece en todos los conjuntos, se marca como dígito común."
P2 = all('3' in conj for conj in conjuntos)  # True si '3' está en TODOS los conjuntos
Q2 = "'3' se considera dígito común"

print("\n--- Expresión Lógica 2 ---")
print(f"¿El dígito '3' está en todos los conjuntos? {P2}")
print(f"Condicional P2 → Q2: 'Si P2 es verdadero, entonces {Q2}.'")
print(f"Como P2 es {P2}, el condicional P2 → Q2 es {'verdadero' if P2 else 'falso'}, y el dígito '3' {'es común' if P2 else 'no es común'} en todos los conjuntos.")



#SE define funcion para evaluar si un año es bisiesto
def anio_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
#Se inicalizan las variables de los años pares e impares
contador_anios_pares=0
contador_anios_impares=0
contador_anios=0
anios = []
edades = []

#Año actual, para no usar datetime
anio_actual = 2025
#Se progrma aun ciclo while para que evalue cada año ingresado y lo agregue al contador de años impares o pares y tambien evalue si es bisiesto"
while contador_anios < 5:
    anio = int(input("\nIngrese el año de nacimiento: "))
    anios.append(anio)
    edad = anio_actual - anio
    edades.append(edad)

    if anio % 2 == 0:
        contador_anios_pares += 1
    else:
        contador_anios_impares += 1

    if anio_bisiesto(anio):
        print("Tenemos un año especial")

    contador_anios += 1

# Mostrar totales
print(f"La cantidad de años impares es: {contador_anios_impares}")
print(f"La cantidad de años pares es: {contador_anios_pares}")
# Grupo Z
if all(anio >= 2000 for anio in anios):
    print("Grupo Z")

# Producto cartesiano entre años y edades actuales
print("Producto cartesiano entre años y edades:")
for anio in anios:
    for edad in edades:
        print((anio, edad))