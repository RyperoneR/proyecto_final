import random as rand
from baraja import baraja

def reparto_mano(jugadores): #FUNCIÓN QUE REPARTE A UN JUGADOR ESPECÍFICO 2 CARTAS DE LA BARAJA
    for jugador in jugadores:
        carta_1=rand.choice(baraja)
        baraja.remove(carta_1)
        carta_2=rand.choice(baraja)
        baraja.remove(carta_2)
        mano = carta_1,carta_2
        jugador['car']+= mano

def reparto_mesa(mesa): #FUNCIÓN QUE SELECCIONA 3 CARTAS DE LA BARAJA Y LAS PONE EN LA MESA
    carta_1=rand.choice(baraja)
    baraja.remove(carta_1)
    carta_2=rand.choice(baraja)
    baraja.remove(carta_2)
    carta_3=rand.choice(baraja)
    baraja.remove(carta_3)
    reveladas=carta_1,carta_2,carta_3
    mesa['cartas']+=reveladas

def carta_ronda(mesa):
    nueva_carta = rand.choice(baraja)
    baraja.remove(nueva_carta)
    carta_revelada = nueva_carta
    mesa['cartas'].append(nueva_carta)

def decisiones_maquina(jugadores,mesa): #FUNCIÓN QUE HACE ELEGIR A LOS JUGADORES DE LA MESA QUE NO SEAN EL USUARIO SU MOVIMIENTO
    for jugador in jugadores:
            if mesa['c'] == 0:
                posibilidades = ["pasar","apostar","irse"]
                decision = rand.choice(posibilidades)
                if decision == "pasar":
                    print(jugador['nombre'],"ha pasado.")
                elif decision== "apostar":
                    cuanto = rand.randint(0,jugador['fichas'])
                    jugador['f']-=cuanto
                    jugador['a']+=cuanto
                    mesa['f']+=cuanto
                    mesa['c']+=cuanto
                    print(jugador['nombre'],"ha apostado",cuanto,"fichas")
                else:
                    print(jugador['nombre'],"se ha ido en esta mano") 
                    jugador['m']=False
            else:
                posibilidades2 = ["apostar","irse"]
                decision2 = rand.choice(posibilidades2)
                if decision2 == "apostar":
                    posibilidades3 = ["i","s"]
                    decision3 = rand.choice(posibilidades3)
                    if decision3 == "i":
                        cantidad = mesa['c']
                        jugador['f']-=cantidad
                        jugador['a']= cantidad
                        mesa['f']+= cantidad
                        print(jugador['nombre'],"ha igualado la apuesta")
                    else:
                        cuant = rand.randint(0,jugador['fichas'])
                        cuantitos = cuant -mesa['c']
                        jugador['f']-=cuant
                        jugador['a']= cuant
                        mesa['f']+= cuant
                        mesa['c'] += cuantitos
                        print(jugador['nombre'],"ha subido la apuesta",cuant,"fichas.")
                else:
                    print(jugador['nombre'],"se retira de esta mano.")
                    jugador['m']=False

def detectar_escalera(lista, n):#FUNCIÓN QUE DETECTA SI UN JUGADOR TIENE UNA ESCALERA EN SU MANO
    # Verificar si la lista tiene al menos n elementos
    if len(lista) < n:
        return None
    
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
    return max_consecutivos

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


def comprobacion(jugador): #FUNCIÓN QUE ANALIZA LA MANO DE CADA JUGADOR
    cartas_totales = jugador['cartas']+mesa["cartas"]
    for carta in cartas_totales:
        for simbolo in carta:
            numeros = simbolo(0,2,4,6,8,10,12)
            palos = simbolo(1,3,5,7,9,11,13)

            pareja = detectar_parejas(numeros)
            if len(pareja) == 1:
                for elemento, ocurrencias in pareja.items():
                    print(jugador,"tiene pareja de",elemento)

            if len(pareja) == 2:
                for elemento,ocurrencias in pareja.items():
                    print(jugador,"tiene doble pareja de",elemento(0), "y",elemento(1))
            
            trio = detectar_trios(numeros)
            if len(trio)== 1:
                for elemento,ocurrencias in trio.items():
                    print(jugador,"tiene trío de",elemento,".")

            poker = detectar_poker(numeros)
            if len(poker) == 1:
                for elemento,ocurrencias in poker.items():
                    print(jugador,"tiene poker de",elemento,".")

            color = comprobar_color(palos)
            if len(color)==1:
                for elemento,ocurrencias in color.items():
                    print(jugador,"tiene color de",elemento,".")

            escalera = detectar_escalera(numeros,5)
            if escalera:
                print(jugador,"tiene escalera de",escalera,".")

            escalera_de_color,colour = detectar_escalera_de_color(cartas_totales)
            if escalera_de_color:
                print(jugador,"tiene una escalera de color de",escalera_de_color)

