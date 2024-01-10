def obtener_5_consecutivos_mas_altos_mismo_simbolo(lista):
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

# Ejemplo de uso con una lista de 7 elementos (número y símbolo):
mi_lista = [(1, 'A'), (2, 'A'), (3, 'A'), (4, 'A'), (5, 'A'), (6, 'A'), (7, 'A')]
resultado, simbolo = obtener_5_consecutivos_mas_altos_mismo_simbolo(mi_lista)

if resultado:
    print(f"Los 5 números consecutivos más altos con el mismo símbolo son: {resultado}")
    print(f"El símbolo relacionado es: {simbolo}")
else:
    print("No hay 5 números consecutivos con el mismo símbolo en la lista.")
