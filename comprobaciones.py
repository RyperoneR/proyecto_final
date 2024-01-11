def detectar_escalera(lista, n):  # FUNCIÓN QUE DETECTA SI UN JUGADOR TIENE UNA ESCALERA EN SU MANO
    # Verificar si la lista tiene al menos n elementos
    if len(lista) < n:
        return False
    
    # Convertir la lista a un conjunto para eliminar duplicados
    conjunto_lista = set(lista)
    
    # Inicializar variables para almacenar los 5 números consecutivos más altos
    max_consecutivos = None
    max_suma = float('-inf')
    
    # Verificar si hay n números consecutivos en la lista
    for i in range(min(lista), max(lista) - n + 2):
        consecutivos = [i + j for j in range(n)]
        if all(num in conjunto_lista for num in consecutivos):
            suma_actual = sum(consecutivos)
            if suma_actual > max_suma:
                max_suma = suma_actual
                max_consecutivos = consecutivos
    
    # Devolver los 5 números consecutivos más altos
    return max_consecutivos if max_consecutivos is not None else False

# ... (otras funciones)

def carta_alta(jugador):
    # Obtener los números de las dos cartas en la mano del jugador
    numeros = [int(carta[:-1]) for carta in jugador['car']]

    # Encontrar la carta más alta
    carta_alta_numero = max(numeros)

    # Obtener el palo de la carta más alta
    palo_carta_alta = [carta[-1] for carta in jugador['car'] if int(carta[:-1]) == carta_alta_numero][0]

    # Devolver la carta alta como una cadena en notación de poker
    return carta_alta_numero, palo_carta_alta


def detectar_escalera_de_color(lista):#FUNCIÓN QUE DETECTA SI UN JUGADOR TIENE UNA ESCALERA DE COLOR EN SU MANO
    # Verificar si la lista tiene al menos 5 elementos
    if len(lista) < 5:
        return None

    # Inicializar variables para almacenar los 5 números consecutivos más altos y el símbolo
    max_consecutivos = None
    max_suma = float('-inf')
    simbolo_relacionado = None

    # Verificar si hay 5 números consecutivos con el mismo símbolo
    for i in range(len(lista) - 4):
        consecutivos = lista[i:i+5]
        simbolo_actual = consecutivos[0][1]

        if all(elemento[1] == simbolo_actual for elemento in consecutivos):
            suma_actual = sum([elemento[0] for elemento in consecutivos])

            if suma_actual > max_suma:
                max_suma = suma_actual
                max_consecutivos = consecutivos
                simbolo_relacionado = simbolo_actual

    # Devolver los 5 números consecutivos más altos y el símbolo
    return max_consecutivos, simbolo_relacionado
def comprobar_color(lista):#FUNCIÓN QUE DETECTA SI UN JUGADOR TIENE COLOR EN SU MANO
    color = {}

    for elemento in lista:
        ocurrencias = lista.count(elemento)
        if ocurrencias == 5:
            color[elemento]=ocurrencias
    return color
def detectar_parejas(lista):#FUNCIÓN QUE DETECTA SI UN JUGADOR TIENE PAREJA EN SU MANO
    parejas = {}

    for elemento in lista:
        ocurrencias = lista.count(elemento)
        if ocurrencias == 2:
            parejas[elemento] = ocurrencias
    return parejas 
def detectar_trios(lista):#FUNCIÓN QUE DETECTA SI UN JUGADOR TIENE TRÍO EN SI MANO
    trios = {}

    for elemento in lista:
        ocurrencias = lista.count(elemento)
        if ocurrencias == 3:
            trios[elemento] = ocurrencias
    return trios
def detectar_poker(lista):#FUNCIÓN QUE DETECTA SI UN JUGADOR TIENE POKER EN SU MANO
    poker = {}

    for elemento in lista:
        ocurrencias = lista.count(elemento)
        if ocurrencias == 4:
            poker[elemento] = ocurrencias
    return poker

def comprobacion(jugador, mesa):  # FUNCIÓN QUE ANALIZA LA MANO DE CADA JUGADOR
    cartas_totales = jugador['car'] + mesa["car"]
    for carta in cartas_totales:
        for simbolo in carta:
            numeros = simbolo[0:13:2]
            palos = simbolo[1:13:2]

    pareja = detectar_parejas(numeros)
    if len(pareja) == 1:
        for elemento, ocurrencias in pareja.items():
            print(jugador, "tiene pareja de", elemento)

    if len(pareja) == 2:
        for elemento, ocurrencias in pareja.items():
            print(jugador, "tiene doble pareja de", elemento[0], "y", elemento[1])
            
    trio = detectar_trios(numeros)
    if len(trio) == 1:
        for elemento, ocurrencias in trio.items():
            print(jugador, "tiene trío de", elemento, ".")

    poker = detectar_poker(numeros)
    if len(poker) == 1:
        for elemento, ocurrencias in poker.items():
            print(jugador, "tiene poker de", elemento, ".")

    color = comprobar_color(palos)
    if len(color) == 1:
        for elemento, ocurrencias in color.items():
            print(jugador, "tiene color de", elemento, ".")

    escalera = detectar_escalera(numeros, 5)
    if escalera is not False:
        print(jugador, "tiene escalera de", escalera, ".")

    escalera_de_color, colour = detectar_escalera_de_color(cartas_totales)
    if escalera_de_color:
        print(jugador, "tiene una escalera de color de", escalera_de_color)
            
    if not (pareja or trio or poker or color or escalera or escalera_de_color):
        numero,palo=carta_alta(jugador)
        print("La carta mas alta de", jugador['nombre'], "es",numero,"de",palo)

mesa = {
    'car': ['9♦','2♥', '7♣', '12♥', '5♥']
}
jugador = {
    'nombre':'Rodrigo',
    'car': ['12♣', '8♠']
}

comprobacion(jugador, mesa)




