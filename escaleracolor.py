def comprobar_color(lista): #FUNCIÓN QUE DETECTA SI UN JUGADOR TIENE COLOR EN SU MANO
    colores = {'♠': 0, '♥': 0, '♦': 0, '♣': 0}

    for carta in lista:
        palo = carta[-1]
        colores[palo] += 1

    for palo, ocurrencias in colores.items():
        if ocurrencias >= 5:
            return palo

    return False

def detectar_escalera(lista, n):  
    # Verificar si la lista tiene al menos n elementos
    if len(lista) < n:
        return False
    
    # Obtener solo los valores numéricos de las cartas
    valores_numericos = [int(carta[:-1]) for carta in lista if carta[:-1].isdigit()]
    
    # Convertir la lista a un conjunto para eliminar duplicados
    conjunto_valores = set(valores_numericos)
    
    # Inicializar variables para almacenar los n números consecutivos más altos
    max_consecutivos = None
    max_suma = float('-inf')
    
    # Verificar si hay n números consecutivos en la lista
    for i in range(min(valores_numericos), max(valores_numericos) - n + 2):
        consecutivos = [str(i + j) + obtener_palo(lista, i + j) for j in range(n)]
        if all(carta in lista for carta in consecutivos):
            suma_actual = sum([int(carta[:-1]) for carta in consecutivos])
            if suma_actual > max_suma:
                max_suma = suma_actual
                max_consecutivos = consecutivos
    
    # Devolver las n cartas consecutivas más altas
    return max_consecutivos if max_consecutivos is not None else False

def obtener_palo(lista, valor):
    for carta in lista:
        if carta[:-1].isdigit() and int(carta[:-1]) == valor:
            return carta[-1]
    return ''



def detectar_escalera_de_color(lista):
    escalera = detectar_escalera(lista,5)
    if escalera:
        escalera_color=comprobar_color(escalera)
        if escalera_color:
            return escalera_color
        else:
            return False
    else:
        return False















