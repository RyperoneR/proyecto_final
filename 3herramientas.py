def obtener_n_consecutivos_mas_altos(lista, n):
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

# Ejemplo de uso con una lista que va del 2 al 13 y busca 5 números consecutivos más altos:
mi_lista = [13,2,3,12,11,10,9]
n = 5
resultado = obtener_n_consecutivos_mas_altos(mi_lista, n)

if resultado:
    print(f"Los {n} números consecutivos más altos son: {resultado}")
else:
    print(f"No hay {n} números consecutivos en la lista.")

