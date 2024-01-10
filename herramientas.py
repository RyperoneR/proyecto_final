def detectar_elementos_repetidos(lista):
    elementos_repetidos = {}

    for elemento in lista:
        ocurrencias = lista.count(elemento)

        # Verificar si hay más de una ocurrencia
        if ocurrencias > 1:
            # Almacenar el elemento y su cantidad de ocurrencias
            elementos_repetidos[elemento] = ocurrencias

    return elementos_repetidos

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 2, 5, 3, 3, 4, 4, 4]
resultados = detectar_elementos_repetidos(mi_lista)

# Mostrar los elementos repetidos y su cantidad de ocurrencias
for elemento, ocurrencias in resultados.items():
    print(f"El elemento {elemento} aparece {ocurrencias} veces en la lista.")

def encontrar_consecutivos(lista):
    for i in range(len(lista) - 4):
        if lista[i] + 1 == lista[i + 1] == lista[i + 2] == lista[i + 3] == lista[i + 4]:
            numeros_consecutivos = lista[i:i+5]
            return True, numeros_consecutivos
    return False, []

# Ejemplo de uso con valores del 2 al 13:
lista_ejemplo = [2, 4, 6, 8, 10, 11, 13]
resultado, consecutivos = encontrar_consecutivos(lista_ejemplo)

if resultado:
    print(f"Hay 5 números consecutivos en la lista: {consecutivos}.")
else:
    print("No hay 5 números consecutivos en la lista.")

