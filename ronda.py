import funciones as fun
import subfuncion as sub

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
            fun.decisiones_maquina(jugador2,mesa)
            if mesa['cantidad apostada por cada jugador']!=0:
                sub.subfuncion2_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa)
            else:
                fun.decisiones_maquina(jugador3,mesa)
                if mesa['cantidad apostada por cada jugador']!=0:
                    sub.subfuncion3_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa)
                else:
                    fun.decisiones_maquina(jugador4,mesa)
                    if mesa['cantidad apostada por cada jugador']!=0:
                        sub.subfuncion4_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa)
                    else:
                        fun.decisiones_maquina(jugador5,mesa)
                        if mesa['cantidad apostada por cada jugador']!=0:
                            sub.subfuncion5_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa)
                        else:
                            fun.decisiones_maquina(jugador6,mesa)
                            if mesa['cantidad apostada por cada jugador']!=0:
                                sub.subfuncion6_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa)

        else:
            print("Ha ocurrido un error. Por favor intentalo de nuevo.")

                        


            



    

    


    



