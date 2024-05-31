def historia():
    print("¡Bienvenido a tu aventura!")
    print("Estás en un bosque misterioso. ¿Qué camino eliges?")
    print("1. Camino de la izquierda")
    print("2. Camino de la derecha")

    eleccion = input("Elige 1 o 2: ")

    if eleccion == "1":
        print("Has encontrado un tesoro escondido. ¡Felicidades!")
    elif eleccion == "2":
        print("Te has perdido en el bosque. ¡Intenta de nuevo!")
    else:
        print("Esa no es una opción válida. ¡Intenta de nuevo!")


def juego():
    historia()
    # Aquí puedes agregar más funciones o lógica para continuar la historia

juego()
