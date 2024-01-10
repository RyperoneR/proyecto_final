import funciones as fun
def subfuncion6_ronda1(jugador1, jugador2, jugador3, jugador4, jugador5, jugador6, mesa):
    while (jugador1['jugando'] and jugador2['jugando'] and jugador3['jugando'] and jugador4['jugando'] and
           jugador5['jugando'] and jugador6['jugando'] and
           (jugador1['jugando'] and jugador2['jugando'] and jugador3['jugando'] and jugador4['jugando'] and
            jugador5['jugando'] and jugador6['jugando']) and
           (jugador1['cantidad apostada'] != jugador2['cantidad apostada'] or
            jugador2['cantidad apostada'] != jugador3['cantidad apostada'] or
            jugador3['cantidad apostada'] != jugador4['cantidad apostada'] or
            jugador4['cantidad apostada'] != jugador5['cantidad apostada'] or
            jugador5['cantidad apostada'] != jugador6['cantidad apostada'] or
            jugador6['cantidad apostada'] != mesa['cantidad apostada por cada jugador'])):

        for jugador in [jugador2, jugador3, jugador4, jugador5, jugador6]:
            if jugador['jugando']==True:
                apuesta_jugador = fun.decisiones_maquina(jugador,mesa)
                jugador['fichas'] -= apuesta_jugador
                jugador['cantidad apostada'] += apuesta_jugador
                mesa['fichas'] += apuesta_jugador
                mesa['cantidad apostada por cada jugador'] += apuesta_jugador
            else:
                next
        if jugador1['cantidad apostada'] != mesa['cantidad apostada por cada jugador']:
            decision = input("Igualar(i)/Subir Apuesta(s)/Irse(i):")
            if decision == "i":
                subida = mesa['cantidad apostada por cada jugador'] - jugador1['cantidad apostada']
                jugador1['cantidad apostada']+=subida
                jugador1['fichas']-=subida
                mesa['fichas']+=subida
            elif decision == "s":
                subir = int(input("¿Cuanto quieres subir?:"))
                apuesta = mesa['cantidad apostada por cada jugador'] - jugador1['cantidad apostada'] + subir
                jugador1['cantidad apostada']+=apuesta
                jugador1['fichas']-=apuesta
                mesa['fichas']+=apuesta
                mesa['cantidad apostada por cada jugador']+=subir
                subfuncion6_ronda1(jugador1, jugador2, jugador3, jugador4, jugador5, jugador6, mesa)
            elif decision == "i":
                print("Te retiras de esta mano. Prueba suerte en la siguiente.")
                jugador1['jugando']=False
                break



        if jugador1['cantidad apostada'] == jugador2['cantidad apostada'] == jugador3['cantidad apostada'] == jugador4['cantidad apostada'] == jugador5['cantidad apostada'] == jugador6['cantidad apostada']:
            break
