print("Escriba la palabra secreta:")
palabraSecreta = str(input())  # Se guarda la palabra secreta que el jugador debe adivinar

intento = list()  # Se crea una lista vacía para mostrar el progreso del jugador

# Se rellena la lista con guiones ("-"), uno por cada letra de la palabra secreta
for letra in palabraSecreta:
    intento.append("-")

print(intento)  # Muestra los guiones al jugador como pistas ocultas
aciertos = 0    # Contador para llevar la cuenta de cuántas letras se han adivinado

# Bucle principal del juego: se repite hasta que se adivinen todas las letras
while aciertos < len(palabraSecreta):
    print("Letra:")
    letra = str(input())  # El jugador introduce una letra
    letra = letra[0]      # Se toma solo el primer carácter por si el usuario escribe más de una letra

    i = 0  # Se inicia un índice para recorrer la palabra letra por letra

    # Este bucle recorre la palabra secreta
    while i < len(palabraSecreta):
        # Si la letra introducida coincide con la letra en la posición i
        # y todavía no se había adivinado esa letra (intento[i] == "-"):
        if palabraSecreta[i] == letra and intento[i] == '-':
            intento[i] = letra  # Se revela la letra en esa posición
            aciertos += 1       # Se incrementa el número de aciertos

        i += 1  # Se pasa a la siguiente letra

    print(intento)  # Muestra el progreso actual (letras adivinadas y guiones restantes)
