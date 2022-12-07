from random import randint

def printTablero(tablero):
    print(tablero[1],'|',tablero[2],'|',tablero[3])
    print('--+---+--')
    print(tablero[4],'|',tablero[5],'|',tablero[6])
    print('--+---+--')
    print(tablero[7],'|',tablero[8],'|',tablero[9])

tablero = {1:' ',2:' ',3:' ',
           4:' ',5:' ',6:' ',
           7:' ',8:' ',9:' '}

turno = 'x' if randint(0,1)==0 else '0'

def devuelve_tablero(ganador):
    printTablero(tablero)
    if not ganador:
        print("Empate")
    else:
        print("Ha ganado el jugador",turno)

#programa principal



print("Tres en raya")
c = 0 #contador para las 9 jugadas
ganador = False

#bucle controlado por contador y por bandera
#termina cuando hay un ganador en 9 jugadas o menos
#de lo contrario termina cuando se superan las 9 jugadas
#y eso indica empate

while c < 9 and not ganador:
    printTablero(tablero)

    print("Turno para",turno,"¿a qué espacio mueves? ")
    pos = int(input())

    if pos<1 or pos>9:
        print("Posición inexistente")
    elif tablero[pos] != ' ':
        print("Posición ocupada")
    else:
        tablero[pos] = turno

        #¿hay ganador?
        if tablero[1] == tablero[5] == tablero[9] and tablero[1] != ' ' or \
           tablero[3] == tablero[5] == tablero[7] and tablero[3] != ' ' or \
           tablero[1] == tablero[4] == tablero[7] and tablero[1] != ' ' or \
           tablero[2] == tablero[5] == tablero[8] and tablero[2] != ' ' or \
           tablero[3] == tablero[6] == tablero[9] and tablero[3] != ' ' or \
           tablero[1] == tablero[2] == tablero[3] and tablero[1] != ' ' or \
           tablero[4] == tablero[5] == tablero[6] and tablero[4] != ' ' or \
           tablero[7] == tablero[8] == tablero[9] and tablero[7] != ' ':
                ganador = True
                devuelve_tablero(ganador)

        #Si no hay ganador le doy el turno al otro
        if not ganador:
            turno = '0' if turno == 'x' else 'x'
            c += 1
