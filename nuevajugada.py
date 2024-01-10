
import random as rand
import json
from baraja import baraja

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

def decision(usuario,mesa):
    if usuario['m']==True:
            if usuario['a']==mesa['c']:
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
                            usuario['a']=igualada
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


def decisiones_maquina(jugadores,mesa): #FUNCIÓN QUE HACE ELEGIR A LOS JUGADORES DE LA MESA QUE NO SEAN EL USUARIO SU MOVIMIENTO
    for jugador in jugadores:
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
                        if jugador['f']>0:
                            cuant = rand.randint(0,(jugador['f']))
                            cuantitos = cuant -mesa['c']
                            jugador['f']-=cuant
                            jugador['a']= cuant
                            mesa['f']+= cuant
                            mesa['c'] += cuantitos
                            print(jugador['nombre'],"ha subido la apuesta",cuant,"fichas.")
                        else:
                            print(jugador['nombre'], "ha pasado.")
                else:
                    print(jugador['nombre'],"se retira de esta mano.")
                    jugador['m']=False




def ronda(usuario,jugadores,mesa):
    usuario['a']=0
    for jugador in jugadores:
        jugador['a']=0

    decision(usuario,mesa)
    print("klk")
    decisiones_maquina(jugadores,mesa)


    if usuario['a']==jugadores[0]['a']and jugadores[0]['a']==jugadores[1]['a']and jugadores[1]['a'] == jugadores[2]['a'] and jugadores[2]['a'] == jugadores[3]['a'] and jugadores[3]['a'] == jugadores[4]['a'] and jugadores[4]['a'] == usuario['a']:
        pass
    elif usuario['m']:
        ronda(user,jugadores_máquina,table)

    
            
    
    

user ={
    'nombre':input("¿Cuál es tu nombre:"), #NOMBRE DEL JUGADOR
    'f': fichas['jugador 1'], #FICHAS DEL JUGADOR
    'car': [],                #CARTAS DEL JUGADOR
    'a':0,                    #FICHAS APOSTADAS POR EL JUGADOR
    'm':True                  #INDICADOR DE SI EL JUGADOR SIGUE EN LA MESA
}

jugador_2 ={
    'nombre':'Jugador 2', #NOMBRE DEL JUGADOR
    'f': fichas['jugador 2'], #FICHAS DEL JUGADOR
    'car': [],                #CARTAS DEL JUGADOR
    'a':0,                    #FICHAS APOSTADAS POR EL JUGADOR
    'm':True                  #INDICADOR DE SI EL JUGADOR SIGUE EN LA MESA
}

jugador_3 ={
    'nombre':'Jugador 3', #NOMBRE DEL JUGADOR
    'f': fichas['jugador 3'], #FICHAS DEL JUGADOR
    'car': [],                #CARTAS DEL JUGADOR
    'a':0,                    #FICHAS APOSTADAS POR EL JUGADOR
    'm':True                  #INDICADOR DE SI EL JUGADOR SIGUE EN LA MESA
}

jugador_4 ={
    'nombre':'Jugador 4', #NOMBRE DEL JUGADOR
    'f': fichas['jugador 4'], #FICHAS DEL JUGADOR
    'car': [],                #CARTAS DEL JUGADOR
    'a':0,                    #FICHAS APOSTADAS POR EL JUGADOR
    'm':True                  #INDICADOR DE SI EL JUGADOR SIGUE EN LA MESA
}

jugador_5 ={
    'nombre':'Jugador 5', #NOMBRE DEL JUGADOR
    'f': fichas['jugador 5'], #FICHAS DEL JUGADOR
    'car': [],                #CARTAS DEL JUGADOR
    'a':0,                    #FICHAS APOSTADAS POR EL JUGADOR
    'm':True                  #INDICADOR DE SI EL JUGADOR SIGUE EN LA MESA
}

jugador_6 ={
    'nombre':'Jugador 6', #NOMBRE DEL JUGADOR
    'f': fichas['jugador 6'], #FICHAS DEL JUGADOR
    'car': [],                #CARTAS DEL JUGADOR
    'a':0,                    #FICHAS APOSTADAS POR EL JUGADOR
    'm':True                  #INDICADOR DE SI EL JUGADOR SIGUE EN LA MESA
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
print("Tu mano es:",user['car'])

ronda(user,jugadores_máquina,table)





