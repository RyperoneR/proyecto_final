import random as rand
import subfuncion as sub
import ronda
import funciones as fun
from baraja import baraja
import json

with open("datos.json","r") as archivo:
    fichas = json.load(archivo)

def ronda_1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa): #FUNCIÓN QUE PONE EN MARCHA LA PRIMERA RONDA
    if jugador1['jugando']==True:
        jugador1['cantidad apostada'] -=jugador1['cantidad apostada']
        jugador2['cantidad apostada'] -= jugador2['cantidad apostada']
        jugador3['cantidad apostada'] -= jugador3['cantidad apostada']
        jugador4['cantidad apostada'] -= jugador4['cantidad apostada']
        jugador5['cantidad apostada'] -= jugador5['cantidad apostada']
        jugador6['cantidad apostada'] -= jugador6['cantidad apostada']
        mesa['cantidad apostada por cada jugador']-=mesa['cantidad apostada por cada jugador']

        decision = input("pasar(p)/apostar(a)/irse(i):")
        if decision == "a":
            cantidad = int(input("¿Cuánto quieres apostar?:"))
            jugador1['fichas']-=cantidad
            jugador1['cantidad apostada'] += cantidad
            mesa['fichas']+=cantidad
            mesa['cantidad apostada por cada jugador'] += cantidad
            sub.subfuncion_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa)
        elif decision == "i":
            print("Te retiras de la jugada. Prueba suerte en la siguiente mano")
            jugador1['jugando']= False

        elif decision == "p":
            apuesta_jugador2 = fun.decisiones_maquina(jugador2,mesa)
            jugador2['fichas']-=apuesta_jugador2
            jugador2['cantidad apostada']+=apuesta_jugador2
            mesa['fichas']+=apuesta_jugador2
            mesa['cantidad apostada por cada jugador']+=apuesta_jugador2
            if mesa['cantidad apostada por cada jugador']!=0:
                sub.subfuncion2_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa)
            else:
                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                jugador3['fichas']-=apuesta_jugador3
                jugador3['cantidad apostada']+=apuesta_jugador3
                mesa['fichas']+=apuesta_jugador3
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3
                if mesa['cantidad apostada por cada jugador']!=0:
                    sub.subfuncion3_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa)
                else:
                    apuesta_jugador4=fun.decisiones_maquina(jugador4,mesa)
                    jugador4['fichas']-=apuesta_jugador4
                    jugador4['cantidad apostada']+=apuesta_jugador4
                    mesa['fichas']+=apuesta_jugador4
                    mesa['cantidad apostada por cada jugador']+=apuesta_jugador4
                    if mesa['cantidad apostada por cada jugador']!=0:
                        sub.subfuncion4_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa)
                    else:
                        apuesta_jugador5=fun.decisiones_maquina(jugador5,mesa)
                        jugador5['fichas']-=apuesta_jugador5
                        jugador5['cantidad apostada']+=apuesta_jugador5
                        mesa['fichas']+=apuesta_jugador5
                        mesa['cantidad apostada por cada jugador']+=apuesta_jugador5
                        if mesa['cantidad apostada por cada jugador']!=0:
                            sub.subfuncion5_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa)
                        else:
                            apuesta_jugador6=fun.decisiones_maquina(jugador6,mesa)
                            jugador6['fichas']-=apuesta_jugador6
                            jugador6['cantidad apostada']+=apuesta_jugador6
                            mesa['fichas']+=apuesta_jugador6
                            mesa['cantidad apostada por cada jugador']+=apuesta_jugador6
                            
                            if mesa['cantidad apostada por cada jugador']!=0:
                                sub.subfuncion6_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa)

        else:
            print("Ha ocurrido un error. Por favor intentalo de nuevo.")
            jugador1['jugando'] = False
   
user = {
    'nombre': input("¿Cuál es tu nombre?: "),
    'fichas': fichas['jugador 1'],
    'cartas':[],
    'cantidad apostada': 0,
    'jugando':True
    }

jugador_1 ={
    'nombre': 'Jugador 1',
    'fichas': fichas['jugador 2'],
    'cartas':[],
    'cantidad apostada': 0,
    'jugando': True
}

jugador_2 ={
    'nombre': 'Jugador 2',
    'fichas': fichas['jugador 3'],
    'cartas':[],
    'cantidad apostada': 0,
    'jugando': True
}

jugador_3 ={
    'nombre': 'Jugador 3',
    'fichas':fichas['jugador 4'],
    'cartas':[],
    'cantidad apostada': 0,
    'jugando': True
}

jugador_4={
    'nombre': 'Jugador 4',
    'fichas':fichas['jugador 5'],
    'cartas':[],
    'cantidad apostada': 0,
    'jugando': True
}

jugador_5={
    'nombre': 'Jugador 5',
    'fichas':fichas['jugador 6'],
    'cartas':[],
    'cantidad apostada': 0,
    'jugando': True
}

mesa ={
    'fichas':0,
    'cartas': [],
    'cantidad apostada por cada jugador': 0
}


#SE REPARTEN CARTAS A CADA JUGADOR

fun.reparto_mano(user)
print("Tus cartas son:",user['cartas'])
fun.reparto_mano(jugador_1)
fun.reparto_mano(jugador_2)
fun.reparto_mano(jugador_3)
fun.reparto_mano(jugador_4)
fun.reparto_mano(jugador_5)

#PRIMERA RONDA

print("!Primera ronda!")
ronda_1(user,jugador_1,jugador_2,jugador_3,jugador_4,jugador_5,mesa)

#SEGUNDA RONDA

print("¡Segunda ronda!")
print("Tus cartas son:",user['cartas'])
print("En el bote hay",mesa['fichas'],"fichas.")
fun.reparto_mesa(mesa)
print("Las cartas que hay en la mesa son:",mesa['cartas'])
ronda_1(user,jugador_1,jugador_2,jugador_3,jugador_4,jugador_5,mesa)

#TERCERA RONDA
print("¡Tercera ronda!")
print("Tus cartas son:",user['cartas'])
print("En el bote hay",mesa['fichas'],"fichas.")
fun.carta_ronda(mesa)
print("Las cartas que hay en la mesa son:",mesa['cartas'])

ronda_1(user,jugador_1,jugador_2,jugador_3,jugador_4,jugador_5,mesa)

#ULTIMA RONDA
print("¡Última ronda!")
print("Tus cartas son:",user['cartas'])
print("En el bote hay",mesa['fichas'],"fichas.")
fun.carta_ronda(mesa)
print("Las cartas que hay en la mesa son:",mesa['cartas'])

ronda_1(user,jugador_1,jugador_2,jugador_3,jugador_4,jugador_5,mesa)

#COMPROBAR QUIÉN GANA

