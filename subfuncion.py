
import funciones as fun

def subfuncion_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa):
    while (jugador1['jugando'] and jugador2['jugando'] and jugador3['jugando'] and jugador4['jugando'] and jugador5['jugando'] and jugador6['jugando'] and
       (jugador1['jugando'] and jugador2['jugando'] and jugador3['jugando'] and jugador4['jugando'] and jugador5['jugando'] and jugador6['jugando']) and
       (jugador1['cantidad apostada'] != jugador2['cantidad apostada'] or
        jugador2['cantidad apostada'] != jugador3['cantidad apostada'] or
        jugador3['cantidad apostada'] != jugador4['cantidad apostada'] or
        jugador4['cantidad apostada'] != jugador5['cantidad apostada'] or
        jugador5['cantidad apostada'] != jugador6['cantidad apostada'] or
        jugador6['cantidad apostada'] != mesa['cantidad apostada por cada jugador'])):


                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                jugador2['fichas']-=apuesta_jugador2
                jugador2['cantidad apostada']+=apuesta_jugador2
                mesa['fichas']+=apuesta_jugador2
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2
                
                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                jugador3['fichas']-=apuesta_jugador3
                jugador3['cantidad apostada']+=apuesta_jugador3
                mesa['fichas']+=apuesta_jugador3
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3
                
                apuesta_jugador4=fun.decisiones_maquina(jugador4,mesa)
                jugador4['fichas']-=apuesta_jugador4
                jugador4['cantidad apostada']+=apuesta_jugador4
                mesa['fichas']+=apuesta_jugador4
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador4

                apuesta_jugador5=fun.decisiones_maquina(jugador5,mesa)
                jugador5['fichas']-=apuesta_jugador5
                jugador5['cantidad apostada']+=apuesta_jugador5
                mesa['fichas']+=apuesta_jugador5
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador5

                apuesta_jugador6=fun.decisiones_maquina(jugador6,mesa)
                jugador6['fichas']-=apuesta_jugador6
                jugador6['cantidad apostada']+=apuesta_jugador6
                mesa['fichas']+=apuesta_jugador6
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador6

                if jugador1['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                    decision_segunda = input("apostar(a)/irse(i):")
                    if decision_segunda == "a":
                        decision_tercera = input("Igualar(i)/Subir apuesta(s)")
                        if decision_tercera == "i":
                            fichas_a_apostar = mesa['cantidad apostada por cada jugador']-jugador1['cantidad apostada']
                            jugador1['fichas']-=fichas_a_apostar
                            jugador1['cantidad apostada']+=fichas_a_apostar
                            mesa['fichas']+= fichas_a_apostar
                        elif decision_tercera == "s":
                            subida = int(input("¿Cuanto más quieres subir?"))
                            if jugador1['fichas']-subida>0:
                                jugador1['fichas']-=subida
                                jugador1['cantidad apostada']+=subida
                                mesa['fichas']+=subida
                                mesa['cantidad apostada por cada jugador']+=subida
                            else:
                                subir = jugador1['fichas']
                                jugador1['fichas']=0
                                jugador1['cantidad apostada']+=subir
                                mesa['fichas']+=subir
                                mesa['cantidad apostada por cada jugador']+=subir
                                print("¡All-in!")
                        else:
                             print("Ha ocurrido un error.")
                             jugador1['jugando']=False
                    elif decision_segunda == "i":
                         print("Te retiras en esta jugada. Prueba suerte en la próxima mano")
                         jugador1['jugando']= False
                         break
                else:
                     break
                
                if jugador1['cantidad apostada'] !=jugador2['cantidad apostada'] !=jugador3['cantidad apostada'] !=jugador4['cantidad apostada'] !=jugador5['cantidad apostada'] !=jugador6['cantidad apostada']:
                    break

def subfuncion2_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa):
    while (jugador1['jugando'] and jugador2['jugando'] and jugador3['jugando'] and jugador4['jugando'] and jugador5['jugando'] and jugador6['jugando'] and
       (jugador1['jugando'] and jugador2['jugando'] and jugador3['jugando'] and jugador4['jugando'] and jugador5['jugando'] and jugador6['jugando']) and
       (jugador1['cantidad apostada'] != jugador2['cantidad apostada'] or
        jugador2['cantidad apostada'] != jugador3['cantidad apostada'] or
        jugador3['cantidad apostada'] != jugador4['cantidad apostada'] or
        jugador4['cantidad apostada'] != jugador5['cantidad apostada'] or
        jugador5['cantidad apostada'] != jugador6['cantidad apostada'] or
        jugador6['cantidad apostada'] != mesa['cantidad apostada por cada jugador'])):


                
                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                jugador3['fichas']-=apuesta_jugador3
                jugador3['cantidad apostada']+=apuesta_jugador3
                mesa['fichas']+=apuesta_jugador3
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3
                
                apuesta_jugador4=fun.decisiones_maquina(jugador4,mesa)
                jugador4['fichas']-=apuesta_jugador4
                jugador4['cantidad apostada']+=apuesta_jugador4
                mesa['fichas']+=apuesta_jugador4
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador4

                apuesta_jugador5=fun.decisiones_maquina(jugador5,mesa)
                jugador5['fichas']-=apuesta_jugador5
                jugador5['cantidad apostada']+=apuesta_jugador5
                mesa['fichas']+=apuesta_jugador5
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador5

                apuesta_jugador6=fun.decisiones_maquina(jugador6,mesa)
                jugador6['fichas']-=apuesta_jugador6
                jugador6['cantidad apostada']+=apuesta_jugador6
                mesa['fichas']+=apuesta_jugador6
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador6
                
                if jugador1['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                    decision_segunda = input("apostar(a)/irse(i):")
                    if decision_segunda == "a":
                        decision_tercera = input("Igualar(i)/Subir apuesta(s)")
                        if decision_tercera == "i":
                            fichas_a_apostar = mesa['cantidad apostada por cada jugador']-jugador1['cantidad apostada']
                            jugador1['fichas']-=fichas_a_apostar
                            jugador1['cantidad apostada']+=fichas_a_apostar
                            mesa['fichas']+= fichas_a_apostar
                            if jugador2['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2
                        elif decision_tercera == "s":
                            subida = int(input("¿Cuanto más quieres subir?"))
                            if jugador1['fichas']-subida>0:
                                jugador1['fichas']-=subida
                                jugador1['cantidad apostada']+=subida
                                mesa['fichas']+=subida
                                mesa['cantidad apostada por cada jugador']+=subida

                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2
                            else:
                                subir = jugador1['fichas']
                                jugador1['fichas']=0
                                jugador1['cantidad apostada']+=subir
                                mesa['fichas']+=subir
                                mesa['cantidad apostada por cada jugador']+=subir
                                print("¡All-in!")

                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2
                        else:
                             print("Ha ocurrido un error.")
                             jugador1['jugando']=False
                    elif decision_segunda == "i":
                         print("Te retiras en esta jugada. Prueba suerte en la próxima mano")
                         jugador1['jugando']= False
                         break
                else:
                     break
                
                if jugador1['cantidad apostada'] !=jugador2['cantidad apostada'] !=jugador3['cantidad apostada'] !=jugador4['cantidad apostada'] !=jugador5['cantidad apostada'] !=jugador6['cantidad apostada']:
                    break

def subfuncion3_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa):
    while (jugador1['jugando'] and jugador2['jugando'] and jugador3['jugando'] and jugador4['jugando'] and jugador5['jugando'] and jugador6['jugando'] and
       (jugador1['jugando'] and jugador2['jugando'] and jugador3['jugando'] and jugador4['jugando'] and jugador5['jugando'] and jugador6['jugando']) and
       (jugador1['cantidad apostada'] != jugador2['cantidad apostada'] or
        jugador2['cantidad apostada'] != jugador3['cantidad apostada'] or
        jugador3['cantidad apostada'] != jugador4['cantidad apostada'] or
        jugador4['cantidad apostada'] != jugador5['cantidad apostada'] or
        jugador5['cantidad apostada'] != jugador6['cantidad apostada'] or
        jugador6['cantidad apostada'] != mesa['cantidad apostada por cada jugador'])):


                
                apuesta_jugador4=fun.decisiones_maquina(jugador4,mesa)
                jugador4['fichas']-=apuesta_jugador4
                jugador4['cantidad apostada']+=apuesta_jugador4
                mesa['fichas']+=apuesta_jugador4
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador4

                apuesta_jugador5=fun.decisiones_maquina(jugador5,mesa)
                jugador5['fichas']-=apuesta_jugador5
                jugador5['cantidad apostada']+=apuesta_jugador5
                mesa['fichas']+=apuesta_jugador5
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador5

                apuesta_jugador6=fun.decisiones_maquina(jugador6,mesa)
                jugador6['fichas']-=apuesta_jugador6
                jugador6['cantidad apostada']+=apuesta_jugador6
                mesa['fichas']+=apuesta_jugador6
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador6
                
                if jugador1['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                    decision_segunda = input("apostar(a)/irse(i):")
                    if decision_segunda == "a":
                        decision_tercera = input("Igualar(i)/Subir apuesta(s)")
                        if decision_tercera == "i":
                            fichas_a_apostar = mesa['cantidad apostada por cada jugador']-jugador1['cantidad apostada']
                            jugador1['fichas']-=fichas_a_apostar
                            jugador1['cantidad apostada']+=fichas_a_apostar
                            mesa['fichas']+= fichas_a_apostar
                            if jugador2['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2
                            if jugador3['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                                jugador3['fichas']-=apuesta_jugador3
                                jugador3['cantidad apostada']+=apuesta_jugador3
                                mesa['fichas']+=apuesta_jugador3
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3
                                 
                        elif decision_tercera == "s":
                            subida = int(input("¿Cuanto más quieres subir?"))
                            if jugador1['fichas']-subida>0:
                                jugador1['fichas']-=subida
                                jugador1['cantidad apostada']+=subida
                                mesa['fichas']+=subida
                                mesa['cantidad apostada por cada jugador']+=subida

                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2

                                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                                jugador3['fichas']-=apuesta_jugador3
                                jugador3['cantidad apostada']+=apuesta_jugador3
                                mesa['fichas']+=apuesta_jugador3
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3
                            else:
                                subir = jugador1['fichas']
                                jugador1['fichas']=0
                                jugador1['cantidad apostada']+=subir
                                mesa['fichas']+=subir
                                mesa['cantidad apostada por cada jugador']+=subir
                                print("¡All-in!")

                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2

                                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                                jugador3['fichas']-=apuesta_jugador3
                                jugador3['cantidad apostada']+=apuesta_jugador3
                                mesa['fichas']+=apuesta_jugador3
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3
                        else:
                             print("Ha ocurrido un error.")
                             jugador1['jugando']=False
                    elif decision_segunda == "i":
                         print("Te retiras en esta jugada. Prueba suerte en la próxima mano")
                         jugador1['jugando']= False
                         break
                else:
                     break
                
                if jugador1['cantidad apostada'] !=jugador2['cantidad apostada'] !=jugador3['cantidad apostada'] !=jugador4['cantidad apostada'] !=jugador5['cantidad apostada'] !=jugador6['cantidad apostada']:
                    break

def subfuncion4_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa):
    while (jugador1['jugando'] and jugador2['jugando'] and jugador3['jugando'] and jugador4['jugando'] and jugador5['jugando'] and jugador6['jugando'] and
       (jugador1['jugando'] and jugador2['jugando'] and jugador3['jugando'] and jugador4['jugando'] and jugador5['jugando'] and jugador6['jugando']) and
       (jugador1['cantidad apostada'] != jugador2['cantidad apostada'] or
        jugador2['cantidad apostada'] != jugador3['cantidad apostada'] or
        jugador3['cantidad apostada'] != jugador4['cantidad apostada'] or
        jugador4['cantidad apostada'] != jugador5['cantidad apostada'] or
        jugador5['cantidad apostada'] != jugador6['cantidad apostada'] or
        jugador6['cantidad apostada'] != mesa['cantidad apostada por cada jugador'])):



                apuesta_jugador5=fun.decisiones_maquina(jugador5,mesa)
                jugador5['fichas']-=apuesta_jugador5
                jugador5['cantidad apostada']+=apuesta_jugador5
                mesa['fichas']+=apuesta_jugador5
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador5

                apuesta_jugador6=fun.decisiones_maquina(jugador6,mesa)
                jugador6['fichas']-=apuesta_jugador6
                jugador6['cantidad apostada']+=apuesta_jugador6
                mesa['fichas']+=apuesta_jugador6
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador6
                
                if jugador1['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                    decision_segunda = input("apostar(a)/irse(i):")
                    if decision_segunda == "a":
                        decision_tercera = input("Igualar(i)/Subir apuesta(s)")
                        if decision_tercera == "i":
                            fichas_a_apostar = mesa['cantidad apostada por cada jugador']-jugador1['cantidad apostada']
                            jugador1['fichas']-=fichas_a_apostar
                            jugador1['cantidad apostada']+=fichas_a_apostar
                            mesa['fichas']+= fichas_a_apostar
                            if jugador2['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2
                            if jugador3['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                                jugador3['fichas']-=apuesta_jugador3
                                jugador3['cantidad apostada']+=apuesta_jugador3
                                mesa['fichas']+=apuesta_jugador3
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3
                            if jugador4['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                                apuesta_jugador4=fun.decisiones_maquina(jugador4,mesa)
                                jugador4['fichas']-=apuesta_jugador4
                                jugador4['cantidad apostada']+=apuesta_jugador4
                                mesa['fichas']+=apuesta_jugador4
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador4
                                 
                        elif decision_tercera == "s":
                            subida = int(input("¿Cuanto más quieres subir?"))
                            if jugador1['fichas']-subida>0:
                                jugador1['fichas']-=subida
                                jugador1['cantidad apostada']+=subida
                                mesa['fichas']+=subida
                                mesa['cantidad apostada por cada jugador']+=subida

                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2

                                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                                jugador3['fichas']-=apuesta_jugador3
                                jugador3['cantidad apostada']+=apuesta_jugador3
                                mesa['fichas']+=apuesta_jugador3
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3

                                apuesta_jugador4=fun.decisiones_maquina(jugador4,mesa)
                                jugador4['fichas']-=apuesta_jugador4
                                jugador4['cantidad apostada']+=apuesta_jugador4
                                mesa['fichas']+=apuesta_jugador4
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador4
                            else:
                                subir = jugador1['fichas']
                                jugador1['fichas']=0
                                jugador1['cantidad apostada']+=subir
                                mesa['fichas']+=subir
                                mesa['cantidad apostada por cada jugador']+=subir
                                print("¡All-in!")

                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2

                                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                                jugador3['fichas']-=apuesta_jugador3
                                jugador3['cantidad apostada']+=apuesta_jugador3
                                mesa['fichas']+=apuesta_jugador3
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3

                                apuesta_jugador4=fun.decisiones_maquina(jugador4,mesa)
                                jugador4['fichas']-=apuesta_jugador4
                                jugador4['cantidad apostada']+=apuesta_jugador4
                                mesa['fichas']+=apuesta_jugador4
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador4
                        else:
                             print("Ha ocurrido un error.")
                             jugador1['jugando']=False
                    elif decision_segunda == "i":
                         print("Te retiras en esta jugada. Prueba suerte en la próxima mano")
                         jugador1['jugando']= False
                         break
                else:
                     break
                
                if jugador1['cantidad apostada'] !=jugador2['cantidad apostada'] !=jugador3['cantidad apostada'] !=jugador4['cantidad apostada'] !=jugador5['cantidad apostada'] !=jugador6['cantidad apostada']:
                    break

def subfuncion5_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa):
    while (jugador1['jugando'] and jugador2['jugando'] and jugador3['jugando'] and jugador4['jugando'] and jugador5['jugando'] and jugador6['jugando'] and
       (jugador1['jugando'] and jugador2['jugando'] and jugador3['jugando'] and jugador4['jugando'] and jugador5['jugando'] and jugador6['jugando']) and
       (jugador1['cantidad apostada'] != jugador2['cantidad apostada'] or
        jugador2['cantidad apostada'] != jugador3['cantidad apostada'] or
        jugador3['cantidad apostada'] != jugador4['cantidad apostada'] or
        jugador4['cantidad apostada'] != jugador5['cantidad apostada'] or
        jugador5['cantidad apostada'] != jugador6['cantidad apostada'] or
        jugador6['cantidad apostada'] != mesa['cantidad apostada por cada jugador'])):


                apuesta_jugador6=fun.decisiones_maquina(jugador6,mesa)
                jugador6['fichas']-=apuesta_jugador6
                jugador6['cantidad apostada']+=apuesta_jugador6
                mesa['fichas']+=apuesta_jugador6
                mesa['cantidad apostada por cada jugador']+=apuesta_jugador6
                
                if jugador1['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                    decision_segunda = input("apostar(a)/irse(i):")
                    if decision_segunda == "a":
                        decision_tercera = input("Igualar(i)/Subir apuesta(s)")
                        if decision_tercera == "i":
                            fichas_a_apostar = mesa['cantidad apostada por cada jugador']-jugador1['cantidad apostada']
                            jugador1['fichas']-=fichas_a_apostar
                            jugador1['cantidad apostada']+=fichas_a_apostar
                            mesa['fichas']+= fichas_a_apostar
                            if jugador2['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2
                            if jugador3['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                                jugador3['fichas']-=apuesta_jugador3
                                jugador3['cantidad apostada']+=apuesta_jugador3
                                mesa['fichas']+=apuesta_jugador3
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3
                            if jugador4['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                                apuesta_jugador4=fun.decisiones_maquina(jugador4,mesa)
                                jugador4['fichas']-=apuesta_jugador4
                                jugador4['cantidad apostada']+=apuesta_jugador4
                                mesa['fichas']+=apuesta_jugador4
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador4
                            if jugador5['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                                apuesta_jugador5=fun.decisiones_maquina(jugador5,mesa)
                                jugador5['fichas']-=apuesta_jugador5
                                jugador5['cantidad apostada']+=apuesta_jugador5
                                mesa['fichas']+=apuesta_jugador5
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador5
                                 
                        elif decision_tercera == "s":
                            subida = int(input("¿Cuanto más quieres subir?"))
                            if jugador1['fichas']-subida>0:
                                jugador1['fichas']-=subida
                                jugador1['cantidad apostada']+=subida
                                mesa['fichas']+=subida
                                mesa['cantidad apostada por cada jugador']+=subida

                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2

                                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                                jugador3['fichas']-=apuesta_jugador3
                                jugador3['cantidad apostada']+=apuesta_jugador3
                                mesa['fichas']+=apuesta_jugador3
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3

                                apuesta_jugador4=fun.decisiones_maquina(jugador4,mesa)
                                jugador4['fichas']-=apuesta_jugador4
                                jugador4['cantidad apostada']+=apuesta_jugador4
                                mesa['fichas']+=apuesta_jugador4
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador4

                                apuesta_jugador5=fun.decisiones_maquina(jugador5,mesa)
                                jugador5['fichas']-=apuesta_jugador5
                                jugador5['cantidad apostada']+=apuesta_jugador5
                                mesa['fichas']+=apuesta_jugador5
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador5
                            else:
                                subir = jugador1['fichas']
                                jugador1['fichas']=0
                                jugador1['cantidad apostada']+=subir
                                mesa['fichas']+=subir
                                mesa['cantidad apostada por cada jugador']+=subir
                                print("¡All-in!")

                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2

                                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                                jugador3['fichas']-=apuesta_jugador3
                                jugador3['cantidad apostada']+=apuesta_jugador3
                                mesa['fichas']+=apuesta_jugador3
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3
                                
                                apuesta_jugador4=fun.decisiones_maquina(jugador4,mesa)
                                jugador4['fichas']-=apuesta_jugador4
                                jugador4['cantidad apostada']+=apuesta_jugador4
                                mesa['fichas']+=apuesta_jugador4
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador4

                                apuesta_jugador5=fun.decisiones_maquina(jugador5,mesa)
                                jugador5['fichas']-=apuesta_jugador5
                                jugador5['cantidad apostada']+=apuesta_jugador5
                                mesa['fichas']+=apuesta_jugador5
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador5
                        else:
                             print("Ha ocurrido un error.")
                             jugador1['jugando']=False
                    elif decision_segunda == "i":
                         print("Te retiras en esta jugada. Prueba suerte en la próxima mano")
                         jugador1['jugando']= False
                         break
                else:
                     break
                
                if jugador1['cantidad apostada'] !=jugador2['cantidad apostada'] !=jugador3['cantidad apostada'] !=jugador4['cantidad apostada'] !=jugador5['cantidad apostada'] !=jugador6['cantidad apostada']:
                    break

def subfuncion6_ronda1(jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,mesa):
    while (jugador1['jugando'] and jugador2['jugando'] and jugador3['jugando'] and jugador4['jugando'] and jugador5['jugando'] and jugador6['jugando'] and
       (jugador1['jugando'] and jugador2['jugando'] and jugador3['jugando'] and jugador4['jugando'] and jugador5['jugando'] and jugador6['jugando']) and
       (jugador1['cantidad apostada'] != jugador2['cantidad apostada'] or
        jugador2['cantidad apostada'] != jugador3['cantidad apostada'] or
        jugador3['cantidad apostada'] != jugador4['cantidad apostada'] or
        jugador4['cantidad apostada'] != jugador5['cantidad apostada'] or
        jugador5['cantidad apostada'] != jugador6['cantidad apostada'] or
        jugador6['cantidad apostada'] != mesa['cantidad apostada por cada jugador'])):

                
                if jugador1['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                    decision_segunda = input("apostar(a)/irse(i):")
                    if decision_segunda == "a":
                        decision_tercera = input("Igualar(i)/Subir apuesta(s)")
                        if decision_tercera == "i":
                            fichas_a_apostar = mesa['cantidad apostada por cada jugador']-jugador1['cantidad apostada']
                            jugador1['fichas']-=fichas_a_apostar
                            jugador1['cantidad apostada']+=fichas_a_apostar
                            mesa['fichas']+= fichas_a_apostar
                            if jugador2['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2
                            if jugador3['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                                jugador3['fichas']-=apuesta_jugador3
                                jugador3['cantidad apostada']+=apuesta_jugador3
                                mesa['fichas']+=apuesta_jugador3
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3
                            if jugador4['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                                apuesta_jugador4=fun.decisiones_maquina(jugador4,mesa)
                                jugador4['fichas']-=apuesta_jugador4
                                jugador4['cantidad apostada']+=apuesta_jugador4
                                mesa['fichas']+=apuesta_jugador4
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador4
                            if jugador5['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:
                                apuesta_jugador5=fun.decisiones_maquina(jugador5,mesa)
                                jugador5['fichas']-=apuesta_jugador5
                                jugador5['cantidad apostada']+=apuesta_jugador5
                                mesa['fichas']+=apuesta_jugador5
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador5
                            if jugador6['cantidad apostada']!=mesa['cantidad apostada por cada jugador']:                                 
                                apuesta_jugador6=fun.decisiones_maquina(jugador6,mesa)
                                jugador6['fichas']-=apuesta_jugador6
                                jugador6['cantidad apostada']+=apuesta_jugador6
                                mesa['fichas']+=apuesta_jugador6
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador6
                                 
                        elif decision_tercera == "s":
                            subida = int(input("¿Cuanto más quieres subir?"))
                            if jugador1['fichas']-subida>0:
                                jugador1['fichas']-=subida
                                jugador1['cantidad apostada']+=subida
                                mesa['fichas']+=subida
                                mesa['cantidad apostada por cada jugador']+=subida

                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2

                                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                                jugador3['fichas']-=apuesta_jugador3
                                jugador3['cantidad apostada']+=apuesta_jugador3
                                mesa['fichas']+=apuesta_jugador3
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3

                                apuesta_jugador4=fun.decisiones_maquina(jugador4,mesa)
                                jugador4['fichas']-=apuesta_jugador4
                                jugador4['cantidad apostada']+=apuesta_jugador4
                                mesa['fichas']+=apuesta_jugador4
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador4

                                apuesta_jugador5=fun.decisiones_maquina(jugador5,mesa)
                                jugador5['fichas']-=apuesta_jugador5
                                jugador5['cantidad apostada']+=apuesta_jugador5
                                mesa['fichas']+=apuesta_jugador5
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador5
                        
                                apuesta_jugador6=fun.decisiones_maquina(jugador6,mesa)
                                jugador6['fichas']-=apuesta_jugador6
                                jugador6['cantidad apostada']+=apuesta_jugador6
                                mesa['fichas']+=apuesta_jugador6
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador6
                            else:
                                subir = jugador1['fichas']
                                jugador1['fichas']=0
                                jugador1['cantidad apostada']+=subir
                                mesa['fichas']+=subir
                                mesa['cantidad apostada por cada jugador']+=subir
                                print("¡All-in!")

                                apuesta_jugador2 =fun.decisiones_maquina(jugador2,mesa)
                                jugador2['fichas']-=apuesta_jugador2
                                jugador2['cantidad apostada']+=apuesta_jugador2
                                mesa['fichas']+=apuesta_jugador2
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador2

                                apuesta_jugador3=fun.decisiones_maquina(jugador3,mesa)
                                jugador3['fichas']-=apuesta_jugador3
                                jugador3['cantidad apostada']+=apuesta_jugador3
                                mesa['fichas']+=apuesta_jugador3
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador3
                                
                                apuesta_jugador4=fun.decisiones_maquina(jugador4,mesa)
                                jugador4['fichas']-=apuesta_jugador4
                                jugador4['cantidad apostada']+=apuesta_jugador4
                                mesa['fichas']+=apuesta_jugador4
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador4

                                apuesta_jugador5=fun.decisiones_maquina(jugador5,mesa)
                                jugador5['fichas']-=apuesta_jugador5
                                jugador5['cantidad apostada']+=apuesta_jugador5
                                mesa['fichas']+=apuesta_jugador5
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador5

                                apuesta_jugador6=fun.decisiones_maquina(jugador6,mesa)
                                jugador6['fichas']-=apuesta_jugador6
                                jugador6['cantidad apostada']+=apuesta_jugador6
                                mesa['fichas']+=apuesta_jugador6
                                mesa['cantidad apostada por cada jugador']+=apuesta_jugador6
                        else:
                             print("Ha ocurrido un error.")
                             jugador1['jugando']=False
                    elif decision_segunda == "i":
                         print("Te retiras en esta jugada. Prueba suerte en la próxima mano")
                         jugador1['jugando']= False
                         break
                else:
                     break
                
                if jugador1['cantidad apostada'] !=jugador2['cantidad apostada'] !=jugador3['cantidad apostada'] !=jugador4['cantidad apostada'] !=jugador5['cantidad apostada'] !=jugador6['cantidad apostada']:
                    break