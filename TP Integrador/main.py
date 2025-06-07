import time
# Lista de productos
productos = [
    {"nombre": "Mouse Inalambrico", "precio": 3500, "stock": 25},
    {"nombre": "Teclado Mecanico", "precio": 12500, "stock": 10},
    {"nombre": "Monitor", "precio": 48000, "stock": 8},
    {"nombre": "Notebook", "precio": 250000, "stock": 5},
    {"nombre": "Cable HDMI", "precio": 2000, "stock": 50},
    {"nombre": "Webcam Full HD", "precio": 8900, "stock": 15}
]

# Mostrar productos
def mostrar_productos(lista):
    print("\n--- Lista de Productos ---")
    for producto in lista:
        print(f"{producto['nombre']:<20} | ${producto['precio']:<7} | Stock: {producto['stock']}")
    print()

# Busqueda lineal (parcial)
def busqueda_lineal(productos, texto_buscado):
    resultados = []
    texto_buscado = texto_buscado.lower()
    for producto in productos:
        if texto_buscado in producto["nombre"].lower():
            resultados.append(producto)
    return resultados

# Busqueda binaria (exacta)
def busqueda_binaria(productos_ordenados, nombre_buscado):
    inicio = 0
    fin = len(productos_ordenados) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        nombre_actual = productos_ordenados[medio]["nombre"].lower()
        if nombre_actual == nombre_buscado.lower():
            return productos_ordenados[medio]
        elif nombre_actual < nombre_buscado.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    return None

# Ordenamiento por nombre (burbuja)
def ordenar_por_nombre(productos):
    lista = productos.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["nombre"].lower() > lista[j + 1]["nombre"].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ordenamiento por precio (inserción)
def ordenar_por_precio(productos):
    lista = productos.copy()
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["precio"] > actual["precio"]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

# Ordenamiento por stock (burbuja)
def ordenar_por_stock(productos):
    lista = productos.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["stock"] > lista[j + 1]["stock"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def comparar_tiempos_busqueda(productos, texto_buscado):
    print(f"\nComparando tiempos de búsqueda para: '{texto_buscado}'")

    # Busqueda lineal
    inicio = time.time()
    resultado_lineal = busqueda_lineal(productos, texto_buscado)
    tiempo_lineal = time.time() - inicio

    # Busqueda binaria
    productos_ordenados = ordenar_por_nombre(productos)
    inicio = time.time()
    resultado_binaria = busqueda_binaria(productos_ordenados, texto_buscado)
    tiempo_binaria = time.time() - inicio

    # Resultados
    print("\nResultado búsqueda LINEAL:")
    if resultado_lineal:
        mostrar_productos(resultado_lineal)
    else:
        print("No se encontraron coincidencias.")

    print("\nResultado búsqueda BINARIA:")
    if resultado_binaria:
        mostrar_productos([resultado_binaria])
    else:
        print("Producto no encontrado (solo búsqueda exacta).")

    # Tiempos
    print("\nTiempos de búsqueda:")
    print(f"Lineal:  {tiempo_lineal:.6f} segundos")
    print(f"Binaria: {tiempo_binaria:.6f} segundos")


# Menú principal
def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Buscar producto (Lineal)")
        print("2. Buscar producto (Binaria - requiere orden)")
        print("3. Ordenar productos por nombre")
        print("4. Ordenar productos por precio")
        print("5. Ordenar productos por stock")
        print("6. Salir")
        print("7. Comparar tiempos de búsqueda (Lineal vs Binaria)")

        
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            texto = input("Ingresá texto para buscar (parcial): ")
            resultado = busqueda_lineal(productos, texto)
            if resultado:
                print("\nResultados encontrados:")
                mostrar_productos(resultado)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "2":
            texto = input("Ingresá el nombre exacto del producto: ")
            productos_ordenados = ordenar_por_nombre(productos)
            resultado = busqueda_binaria(productos_ordenados, texto)
            if resultado:
                print("\nProducto encontrado:")
                mostrar_productos([resultado])
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            ordenados = ordenar_por_nombre(productos)
            print("\nProductos ordenados por NOMBRE:")
            mostrar_productos(ordenados)

        elif opcion == "4":
            ordenados = ordenar_por_precio(productos)
            print("\nProductos ordenados por PRECIO:")
            mostrar_productos(ordenados)

        elif opcion == "5":
            ordenados = ordenar_por_stock(productos)
            print("\nProductos ordenados por STOCK:")
            mostrar_productos(ordenados)

        elif opcion == "6":
            print("Hasta la proxima!")

        elif opcion == "7":
            texto = input("Ingresá el nombre del producto para comparar búsquedas: ")
            comparar_tiempos_busqueda(productos, texto)
            break

        else:
            print("Opción no válida. Intentá de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
