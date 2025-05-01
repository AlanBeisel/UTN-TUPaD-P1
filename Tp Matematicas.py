print("Conversor de números - UTN TUPaD - Comisión 10")

while True: #lo usamos para poder repetir que el usuario ingrese un número. El while True lo que hace es que es un bucle infinito mientras lo que ingrese no sea válido. Si el número es válido, el codigo sigue y el break hace que el bucle se detenga y el programa continúe.
    print("Elija una opción (1, 2 o 3):")
    print("1. Pasar de decimal a binario")
    print("2. Pasar de binario a decimal")
    print("3. Salir del programa")

    eleccion = input() #elije la opcion correspondiente

    if eleccion == '1':
        while True: #lo usamos para poder repetir que el usuario ingrese un número
            numero_decimal = input("Ingresá un número decimal positivo: ")

            if numero_decimal != "": #esto es para evitar que no quede vacío el input
                for num in numero_decimal: #recorre el numero ingresado uno por uno para buscar si hay algun error
                    if num not in '0123456789':
                        print("Número decimal inválido! Coloque números del 0 al 9.")
                        break
                else:
                    decimal = int(numero_decimal) #covertimos el texto a número
                    binario = bin(decimal)[2:] #bin() convierte numero decimal a binario pero con un "0b" al principio, se hace un "slicing" con [2:] (borra los dos primeros caracteres del string)
                    print("El número", decimal, "en binario es:", binario)
                    print()  #línea en blanco para separar
                    break

    elif eleccion == '2':
        while True: #lo usamos para poder repetir que el usuario ingrese un número
            numero_binario = input("Ingresá un número binario (0 y 1): ")

            if numero_binario != "": #esto es para evitar que no quede vacío el input
                for num in numero_binario: #recorre el numero ingresado uno por uno para buscar si hay algun error
                    if num != '0' and num != '1':
                        print("Número binario inválido! Coloque solo 0 y 1.")
                        break
                else:
                    decimal = int(numero_binario, 2) #covertimos el texto a número, y el "2" lo utilizamos para pasar de decimal a binario ya que es en base 2
                    print("El número binario", numero_binario, "en decimal es:", decimal)
                    print()  #línea en blanco para separar
                    break

    elif eleccion == '3':
        print("Saludos!")
        break

    else:
        print("Opción no válida! Elegí 1, 2 o 3.")
        print()  #línea en blanco para separar