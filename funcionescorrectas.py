def carta_alta(jugador):
    # Obtener los números de las dos cartas en la mano del jugador
    numeros = [int(carta[:-1]) for carta in jugador['car']]

    # Encontrar la carta más alta
    carta_alta_numero = max(numeros)

    # Obtener el palo de la carta más alta
    palo_carta_alta = [carta[-1] for carta in jugador['car'] if int(carta[:-1]) == carta_alta_numero][0]

    # Devolver la carta alta como una cadena en notación de poker
    return carta_alta_numero, palo_carta_alta
#ESTA FUNCIÓN SIEMPRE VA A FUNCIONAR

def detectar_escalera(lista, n):  # FUNCIÓN QUE DETECTA SI UN JUGADOR TIENE UNA ESCALERA EN SU MANO
    # Verificar si la lista tiene al menos n elementos
    if len(lista) < n:
        return False
    
    # Obtener solo los valores numéricos de las cartas
    valores_numericos = [int(carta[:-1]) for carta in lista if carta[:-1].isdigit()]
    
    # Convertir la lista a un conjunto para eliminar duplicados
    conjunto_lista = set(valores_numericos)
    
    # Inicializar variables para almacenar los n números consecutivos más altos
    max_consecutivos = None
    max_suma = float('-inf')
    
    # Verificar si hay n números consecutivos en la lista
    for i in range(min(valores_numericos), max(valores_numericos) - n + 2):
        consecutivos = [i + j for j in range(n)]
        if all(num in conjunto_lista for num in consecutivos):
            suma_actual = sum(consecutivos)
            if suma_actual > max_suma:
                max_suma = suma_actual
                max_consecutivos = consecutivos
    
    # Devolver los n números consecutivos más altos
    return max_consecutivos if max_consecutivos is not None else False

#ESTA FUNCIÓN DEVUELVE LA ESCALERA SI LA HAY, Y SI NO LA ESCALERA=FALSE

def comprobar_color(lista): #FUNCIÓN QUE DETECTA SI UN JUGADOR TIENE COLOR EN SU MANO
    colores = {'♠': 0, '♥': 0, '♦': 0, '♣': 0}

    for carta in lista:
        palo = carta[-1]
        colores[palo] += 1

    for palo, ocurrencias in colores.items():
        if ocurrencias >= 5:
            return palo

    return False

#ESTA FUNCIÓN DEVUELVE EL PALO DEL COLOR SI LO HAY Y EN CASO CONTRARIO COLOR=FALSE

def detectar_parejas(lista): #FUNCIÓN QUE DETECTA SI UN JUGADOR TIENE PAREJA EN SU MANO
    numeros = [carta[:-1] for carta in lista]
    parejas = []

    for numero in numeros:
        ocurrencias = numeros.count(numero)
        if ocurrencias == 2 and numero not in parejas:
            parejas.append(numero)

    return parejas if len(parejas) > 0 else False

#ESTA FUNCIÓN DEVUELVE UNA LISTA DE PAREJAS SI LAS HAY, EN CASO CONTRARIO DEVUELVE PAREJAS=FALSE (CUIDADO CON LAS DOBLES PAREJAS)

def detectar_trios(lista): #FUNCIÓN QUE DETECTA SI UN JUGADOR TIENE TRIO EN SU MANO
    numeros = [carta[:-1] for carta in lista]
    trios = []

    for numero in numeros:
        ocurrencias = numeros.count(numero)
        if ocurrencias == 3 and numero not in trios:
            trios.append(numero)

    return trios if len(trios) > 0 else False

#ESTA FUNCION DEVUELVE EL NUMERO DEL TRIO SI LO HAY. EN CASO CONTRARIO DEVUELVE FALSE.

def detectar_poker(lista): #FUNCIÓN QUE DETECTA SI UN JUGADOR TIENE POKER EN SU MANO
    numeros = [carta[:-1] for carta in lista]
    poker = []

    for numero in numeros:
        ocurrencias = numeros.count(numero)
        if ocurrencias == 4 and numero not in poker:
            poker.append(numero)

    return poker if len(poker) > 0 else False

#ESTA FUNCION DEVUELVE EL NÚMERO DEL POKER SI LO HAY. EN CASO CONTRARIO DEVUELVE FALSE


jugador1={
    'cartas':['2♥', '8♠']
}

jugador1={
    'cartas':['9♦', '12♣']
}

def obtener_carta_mas_alta(cartas):
    valores_cartas = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, '12': 12, '13': 13, '14': 14}
    return max(cartas, key=lambda x: valores_cartas[x[:-1]])