import json

# Guardar datos en un archivo JSON
datos_python = {
    "jugador 1": 100000,
    "jugador 2": 100000,
    "jugador 3": 100000,
    "jugador 4": 100000,
    "jugador 5": 100000,
    "jugador 6": 100000
}

with open('datos.json', 'w') as archivo:
    json.dump(datos_python, archivo)

# Cargar datos desde un archivo JSON
with open('datos.json', 'r') as archivo:
    datos_cargados = json.load(archivo)

# Acceder a los datos cargados
print("fichas del jugador 1:", datos_cargados["jugador 1"])
print("fichas del jugador 2:", datos_cargados["jugador 2"])
print("fichas del jugador 3:", datos_cargados["jugador 3"])
print("fichas del jugador 4:", datos_cargados["jugador 4"])
print("fichas del jugador 5:", datos_cargados["jugador 5"])
print("fichas del jugador 6:", datos_cargados["jugador 6"])
