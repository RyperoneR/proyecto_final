

import sys
import random as rand
import json
from baraja import baraja
import escaleracolor as esca
import funcionescorrectas as fun

with open("datos.json","r") as archivo:
    fichas = json.load(archivo)

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
    mesa['car']+=reveladas

def carta_ronda(mesa):
    nueva_carta = rand.choice(baraja)
    baraja.remove(nueva_carta)
    carta_revelada = nueva_carta
    mesa['car'].append(nueva_carta)

def decision(usuario,mesa):
    if usuario['m']==True:
            if usuario['f']==0:
                pass
            else:
                if usuario['a']==mesa['c'] and mesa['c']==0:
                    if usuario['f']>0:
                        decision = input("Apostar(a)/Pasar(p)/Irse(i)")
                        if decision == 'a':
                            cantidad = int(input("¿Cuántas fichas quieres apostar?:"))
                            if cantidad > usuario['f']:
                                print("No tienes esa cantidad. Dispones de",usuario['f'],"fichas.")
                            elif usuario['f']>=cantidad>=0:
                                usuario['f']-=cantidad
                                usuario['a']+=cantidad
                                mesa['f']+=cantidad
                                mesa['c']+=cantidad
                                print("La puja está en",usuario['a'],"fichas.")
                            else:
                                print("Ha ocurrido un error")
                        elif decision == 'p':
                            pass
                        elif decision == 'i':
                            print("Te retiras de esta mano. Prueba suerte en la siguiente")
                            usuario['m']=False
                    elif usuario['f']==0:
                        opciones = input("No te quedan fichas. Pasar(p)/Irse(i):")
                        if opciones == 'p':
                            pass
                        elif opciones =='i':
                            print("Te retiras de esta mano. Prueba suerte en la siguiente")
                            usuario['m']=False
                elif usuario['a']==mesa['c'] and mesa['c']!=0:
                    pass
                else:
                    if usuario['f']>0:
                        decision = input("Apostar(a)/Irse(i)")
                        if decision == 'a':
                            cuanto = input("Igualar(i)/Subir Apuesta(s):")
                            if cuanto =='s':
                                subida = int(input("¿Cuántas fichas más quieres apostar?:")) #FICHAS QUE SUBES A LA APUESTA ANTERIOR A LA TUYA
                                subido = subida + mesa['c'] #TOTAL DE FICHAS QUE HAS APOSTADO
                                if subido > usuario['f']:
                                    print("No tienes esa cantidad. Dispones de",usuario['f'],"fichas.")
                                elif usuario['f']>=subido>=0:
                                    usuario['f']-=subido
                                    usuario['a']+=subida
                                    mesa['f']+=subido
                                    mesa['c']+= subida
                                    print("La puja está en",mesa['c'],"fichas.")
                            elif cuanto == 'i':
                                igualada = mesa['c']-usuario['a']
                                usuario['f']-= igualada
                                usuario['a']+=igualada
                                mesa['f']+=igualada
                            else:
                                print("Ha ocurrido un error")
                        elif decision == 'i':
                            print("Te retiras de esta mano. Prueba suerte en la siguiente")
                            usuario['m']=False
                    elif usuario['f']==0:
                        opciones = input("No te quedan fichas. Pasar(p)/Irse(i):")
                        if opciones == 'p':
                            pass
                        elif opciones =='i':
                            print("Te retiras de esta mano. Prueba suerte en la siguiente")
                            usuario['m']=False

    else:
        pass


def decisiones_maquina(jugadores,mesa): #FUNCIÓN QUE HACE ELEGIR A LOS JUGADORES DE LA MESA QUE NO SEAN EL USUARIO SU MOVIMIENTO:
    global jugadores_máquina
    jugadores_máquina_actual = [jugador for jugador in jugadores if jugador['m']]

    for jugador in jugadores_máquina_actual:
            print("   ")
            if mesa['c'] == 0:
                posibilidades = ["pasar","apostar","irse"]
                decision = rand.choice(posibilidades)
                if decision == "pasar":
                    print(jugador['nombre'],"ha pasado.")
                elif decision== "apostar":
                    cuanto = rand.randint(0,(jugador['f']))
                    jugador['f']-=cuanto
                    jugador['a']+=cuanto
                    mesa['f']+=cuanto
                    mesa['c']+=cuanto
                    print(jugador['nombre'],"ha apostado",cuanto,"fichas")
                    print("La puja está en",mesa['c'],"fichas")
                else:
                    print(jugador['nombre'],"se ha ido en esta mano") 
                    jugador['m']=False
                    jugadores_máquina.remove(jugador)
            elif mesa['c']!=0 and mesa['c']==jugador['a']:
                pass
            else:
                posibilidades2 = ["apostar","irse"]
                decision2 = rand.choice(posibilidades2)
                if decision2 == "apostar":

                    decision3 = rand.randint(0,100)
                    if decision3 <=95:
                        cantidad = mesa['c']
                        jugador['f']-=cantidad
                        jugador['a']+= cantidad
                        mesa['f']+= cantidad
                        print(jugador['nombre'],"ha igualado la apuesta")
                    else:
                        if jugador['f']>0:
                            cuant = rand.randint(0,(jugador['f']))
                            cuantitos = cuant -mesa['c']
                            jugador['f']-=cuant
                            jugador['a']= cuant
                            mesa['f']+= cuant
                            mesa['c'] += cuantitos
                            print(jugador['nombre'],"ha subido la apuesta",cuant,"fichas.")
                            print("La puja está en",mesa['c'],"fichas")

                        else:
                            print(jugador['nombre'], "ha pasado.")
                else:
                    print(jugador['nombre'],"se retira de esta mano.")
                    jugador['m']=False
                    jugadores_máquina.remove(jugador)
    jugadores_máquina = jugadores_máquina_actual





def ronda(usuario,jugadores,mesa):
    if usuario['m']==True:

        decision(usuario,mesa)
        if usuario['m']==False:
            print("Adiós.")
        else:
            decisiones_maquina(jugadores,mesa)

            if jugadores_máquina ==[]:
                print("Has ganado la mano.")
                sys.exit()
            
            if all(jugador['a']==usuario['a'] for jugador in jugadores):
                pass
            else:
                ronda(user,jugadores_máquina,table)
    else:
        pass

    
            
    
    

user ={
    'nombre':input("¿Cuál es tu nombre?:"), #NOMBRE DEL JUGADOR
    'f': fichas['jugador 1'], #FICHAS DEL JUGADOR
    'car': [],                #CARTAS DEL JUGADOR
    'a':0,                    #FICHAS APOSTADAS POR EL JUGADOR
    'm':True ,                 #INDICADOR DE SI EL JUGADOR SIGUE EN LA MESA
    'mano': 0,
    'carta alta': 0
}

jugador_2 ={
    'nombre':'Jugador 2', #NOMBRE DEL JUGADOR
    'f': fichas['jugador 2'], #FICHAS DEL JUGADOR
    'car': [],                #CARTAS DEL JUGADOR
    'a':0,                    #FICHAS APOSTADAS POR EL JUGADOR
    'm':True,                  #INDICADOR DE SI EL JUGADOR SIGUE EN LA MESA
    'mano': 0
}

jugador_3 ={
    'nombre':'Jugador 3', #NOMBRE DEL JUGADOR
    'f': fichas['jugador 3'], #FICHAS DEL JUGADOR
    'car': [],                #CARTAS DEL JUGADOR
    'a':0,                    #FICHAS APOSTADAS POR EL JUGADOR
    'm':True,                  #INDICADOR DE SI EL JUGADOR SIGUE EN LA MESA
    'mano': 0
}

jugador_4 ={
    'nombre':'Jugador 4', #NOMBRE DEL JUGADOR
    'f': fichas['jugador 4'], #FICHAS DEL JUGADOR
    'car': [],                #CARTAS DEL JUGADOR
    'a':0,                    #FICHAS APOSTADAS POR EL JUGADOR
    'm':True,                  #INDICADOR DE SI EL JUGADOR SIGUE EN LA MESA
    'mano': 0
}

jugador_5 ={
    'nombre':'Jugador 5', #NOMBRE DEL JUGADOR
    'f': fichas['jugador 5'], #FICHAS DEL JUGADOR
    'car': [],                #CARTAS DEL JUGADOR
    'a':0,                    #FICHAS APOSTADAS POR EL JUGADOR
    'm':True,                  #INDICADOR DE SI EL JUGADOR SIGUE EN LA MESA
    'mano': 0
}

jugador_6 ={
    'nombre':'Jugador 6', #NOMBRE DEL JUGADOR
    'f': fichas['jugador 6'], #FICHAS DEL JUGADOR
    'car': [],                #CARTAS DEL JUGADOR
    'a':0,                    #FICHAS APOSTADAS POR EL JUGADOR
    'm':True,                  #INDICADOR DE SI EL JUGADOR SIGUE EN LA MESA
    'mano': 0
}

table ={
    'f':0,
    'car':[],
    'c':0
}

jugadores_total =[user,jugador_2,jugador_3,jugador_4,jugador_5,jugador_6]
jugadores_mesa = [jugador for jugador in jugadores_total if jugador['m']]
jugadores_máquina = jugadores_mesa[1:]

#REPARTO DE CARTAS

reparto_mano(jugadores_mesa)
print("   ")
print("Tu mano es:",user['car'])

#RONDA 1
print("   ")
print("PRIMERA RONDA")
print("   ")

ronda(user,jugadores_máquina,table)

#RONDA 2
print("   ")
print("SEGUNDA RONDA")
print("   ")

reparto_mesa(table)

print("Las cartas que hay sobre la mesa son:",table['car'])
print("Tus cartas son:",user['car'])

table['c']=0
user['a']=0
for jugon in jugadores_máquina:
    jugon['a']=0
ronda(user,jugadores_máquina,table)

#RONDA 3
print("   ")
print("TERCERA RONDA")
print("   ")

carta_ronda(table)

print("Las cartas que hay sobre la mesa son:",table['car'])
print("Tus cartas son:",user['car'])

table['c']=0
user['a']=0
for jugon in jugadores_máquina:
    jugon['a']=0
ronda(user,jugadores_máquina,table)

#RONDA FINAL
print("   ")
print("ÚLTIMA RONDA")
print("   ")

carta_ronda(table)

print("Las cartas que hay sobre la mesa son:",table['car'])
print("Tus cartas son:",user['car'])

table['c']=0
user['a']=0
for jugon in jugadores_máquina:
    jugon['a']=0
ronda(user,jugadores_máquina,table)

#EVALUACIÓN DE CADA MANO

if user['m']==True:
    cartas_totales=user['car']+table['car']
    parejas = fun.detectar_parejas(cartas_totales)
    if parejas:
        if len(parejas)==1:
            print("Tienes pareja de",parejas)
            user['mano'] = 1
        elif len(parejas)>1:
            parejas_ordenadas = sorted(parejas, key=lambda x: int(x), reverse=True)
            primera_pareja=parejas_ordenadas[0]
            segunda_pareja_mas_alta = parejas_ordenadas[1]
            print("Tienes doble pareja de",primera_pareja, segunda_pareja_mas_alta)
            user['mano']=2
    trio = fun.detectar_trios(cartas_totales)
    if trio:
        print("Tienes trio de",trio)
        user['mano']=3
    escalera = fun.detectar_escalera(cartas_totales,5)
    if escalera:
        print("Tienes escalera de",escalera)
        user['mano']=4
    color = fun.comprobar_color(cartas_totales)
    if color:
        print("Tienes color de",color)
        user['mano']
    if trio and parejas:
        pareja_ordenada = sorted(parejas, key=lambda x: int(x), reverse=True)
        print("Tienes full house de",trio,"y",pareja_ordenada[0])
        user['mano']=6
    poker = fun.detectar_poker(cartas_totales)
    if poker:
        print("Tienes poker de",poker)
        user['mano']=7
    escalera_de_color=esca.detectar_escalera_de_color(cartas_totales)
    if escalera_de_color:
        print("Tienes escalera de color de",escalera_de_color)

print("  ")

for jugadores in jugadores_mesa:
    cartas_jugador = jugadores['car']+table['car']
    parejas = fun.detectar_parejas(cartas_jugador)
    if parejas:
        if len(parejas)==1:
            print(jugadores['nombre'],"tiene pareja de",parejas)
            jugadores['mano'] = 1
        elif len(parejas)>1:
            parejas_ordenadas = sorted(parejas, key=lambda x: int(x), reverse=True)
            primera_pareja=parejas_ordenadas[0]
            segunda_pareja_mas_alta = parejas_ordenadas[1]
            print(jugadores['nombre'],"tiene doble pareja de",primera_pareja, segunda_pareja_mas_alta)
            jugadores['mano']=2
    trio = fun.detectar_trios(cartas_jugador)
    if trio:
        print(jugadores['nombre'],"Tienes trio de",trio)
        jugadores['mano']=3
    escalera = fun.detectar_escalera(cartas_jugador,5)
    if escalera:
        print(jugadores['nombre'],"tiene escalera de",escalera)
        jugadores['mano']=4
    color = fun.comprobar_color(cartas_jugador)
    if color:
        print(jugadores['nombre'],"tiene color de",color)
        jugadores['mano']
    if trio and parejas:
        pareja_ordenada = sorted(parejas, key=lambda x: int(x), reverse=True)
        print(jugadores['nombre'],"iene full house de",trio,"y",pareja_ordenada[0])
        jugadores['mano']=6
    poker = fun.detectar_poker(cartas_jugador)
    if poker:
        print(jugadores['nombre'],"tiene poker de",poker)
        jugadores['mano']=7
    escalera_de_color=esca.detectar_escalera_de_color(cartas_jugador)
    if escalera_de_color:
        print(jugadores['nombre'],"tiene escalera de color de",escalera_de_color)

    print("  ")

manos = [jugador['mano'] for jugador in jugadores_total]

ganador = max(manos)

ganadores = [diccionario for diccionario in jugadores_total if diccionario['mano'] == ganador]

if len(ganadores) == 1:
    print(ganadores[0]['nombre'], "ha ganado la mano.")
else:
    ganador_con_carta_mas_alta = max(ganadores, key=lambda x: max(x['car']))
    
    print(ganador_con_carta_mas_alta['nombre'], "ha ganado con la mano por carta alta.")









    











