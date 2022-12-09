from random import randint

def printTablero(tablero):
    print(tablero[1],'|',tablero[2],'|',tablero[3])
    print('--+---+--')
    print(tablero[4],'|',tablero[5],'|',tablero[6])
    print('--+---+--')
    print(tablero[7],'|',tablero[8],'|',tablero[9])

def set_posicion():
    print("es el turno de",turno,"introduce posición")
    return int(input("> "))
      
def jugada_tablero(turno,tablero):
    '''añade posición al tablero segun la jugada del jugador'''
    pos = set_posicion()
    if pos>0 and pos<10:
        if tablero[pos]==' ':
            tablero[pos] = turno
        else:
            print("Posición ocupada")
            jugada_tablero(turno,tablero) 
    else:
        print("Posición inexistente")  
        jugada_tablero(turno,tablero)

def reglas(tablero):
    if tablero[1]==tablero[2]==tablero[3]==turno or tablero[4]==tablero[5]==tablero[6]==turno or \
    tablero[7] == tablero[8] == tablero[9]==turno or tablero[1] == tablero[4] == tablero[7]==turno or \
    tablero[2] == tablero[5] == tablero[8] == turno or tablero[3] == tablero[6] == tablero[9] == turno or \
    tablero[1] == tablero[5] == tablero[9] == turno or tablero[3] == tablero[5] == tablero[7] == turno:
        return True 
    return False     

def dice_ganador(ganador):
    if ganador:
        print("El ganador es",turno)

#programa principal

tablero = {1:' ',2:' ',3:' ',
           4:' ',5:' ',6:' ',
           7:' ',8:' ',9:' '}

turno = 'X' if randint(0,1)==0 else '0'

printTablero(tablero)
ganador = False
jugadas = 0
while ganador == False:
    jugadas += 1
    if jugadas == 10:# si las jugadas llegan a 10 termina el juego sin ganador
        print("No hay ganador")
        break
    jugada_tablero(turno,tablero)# añade la posición al tablero del jugador
    printTablero(tablero)
    ganador = reglas(tablero)
    dice_ganador(ganador)# dice el ganador en el caso de que halla
    turno = '0' if turno == 'X' else 'X'# cambia de turno al jugador

    
    

