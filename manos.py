def detectar_parejas(lista): 
    numeros = [carta[:-1] for carta in lista]
    parejas = []

    for numero in numeros:
        ocurrencias = numeros.count(numero)
        if ocurrencias == 2 and numero not in parejas:
            parejas.append(numero)

    return parejas if len(parejas) > 0 else False

# Llamada a la función y selección de la pareja más alta
cartas_totales = ['12♦', '11♦', '10♥', '13♦', '9♦','7♦','8♦']
parejas = detectar_parejas(cartas_totales)

if parejas:
    if len(parejas)==1:
        print("Tienes pareja de",parejas)
    elif len(parejas)>1:
        parejas_ordenadas = sorted(parejas, key=lambda x: int(x), reverse=True)
        primera_pareja=parejas_ordenadas[0]
        segunda_pareja_mas_alta = parejas_ordenadas[1]
        print("Tienes doble pareja de",primera_pareja, segunda_pareja_mas_alta)


