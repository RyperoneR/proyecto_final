def tiene_5_consecutivos(lista):
    # Verificar si la lista tiene al menos 5 elementos
    if len(lista) < 5:
        return False
    
    # Convertir la lista a un conjunto para eliminar duplicados
    conjunto_lista = set(lista)
    
    # Verificar si hay 5 números consecutivos en el rango del 2 al 13
    for i in range(2, 9):  # Rango del 2 al 8 (inclusive)
        if all((i + j) in conjunto_lista for j in range(5)):
            return True
    
    # Si no se encontraron 5 números consecutivos
    return False

# Ejemplo de uso con una lista que va del 2 al 13:
mi_lista = [2,5,7,10,3,9,8]
resultado = tiene_5_consecutivos(mi_lista)

if resultado:
    print("Hay 5 números consecutivos en la lista.")
else:
    print("No hay 5 números consecutivos en la lista.")


