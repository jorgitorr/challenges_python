import random, time
from random import shuffle


def get_baraja_al_azar(numero,palo):
    return random.choice(str(numero)),random.choice(palo)


def imprime(baraja):
    return(" _____ " + " " + " _____ " + " " + " _____ \n"\
          "|" + baraja[0][0] + "    |" + " " + "|" + baraja[1][0] + "    |" + " " + "|" + baraja[2][0] + "    |\n"\
          "|  " + baraja[0][1] + "  |" + " " + "|  " + baraja[1][1] + "  |" + " " + "|  " + baraja[2][1] + "  |\n"\
          "|____" + baraja[0][0] + "|" + " " + "|____" + baraja[1][0] + "|" + " " + "|____" + baraja[2][0] + "|")

def get_jugada_cupier(jugadas):
    return random.choice(jugadas)

def intercambio_cartas(baraja):
    '''intercambia la posición entre cartas'''
    jugada_cupier = get_jugada_cupier(jugadas)

    if jugada_cupier == 'L-R':
        print("swapping left and right")
        baraja[0],baraja[2] = baraja[2],baraja[0]
    elif jugada_cupier == "L-M":
        print("swapping left and middle")
        baraja[0],baraja[1] = baraja[1],baraja[0] 
    elif jugada_cupier == "M-L":
        print("swapping middle and left")
        baraja[1],baraja[0] = baraja[0],baraja[1]
    elif jugada_cupier == "M-R":
        print("swapping middle and right")
        baraja[1],baraja[2] = baraja[2],baraja[1]
    elif jugada_cupier == "R-L":
        print("swapping right and left")
        baraja[2],baraja[0] = baraja[0],baraja[2]
    elif jugada_cupier == "R-M":
        print("swapping right and middle")    
        baraja[2],baraja[1] = baraja[1],baraja[2]

def get_pos_usuario():
    print("--snip--")
    return input("Wich card has the Queen of Hearts? (LEFT MIDDLE RIGHT)\n> ").upper()

def get_pos_carta(baraja):
    pos_usuario = get_pos_usuario()
    '''devuelve la posicion de la carta'''
    if pos_usuario=="LEFT":
        return 0
    elif pos_usuario=="MIDDLE":
        return 1
    elif pos_usuario=="RIGHT":
        return 2  

def es_posicion(pos):
    if baraja[pos] == ("Q",CORAZONES):
        return True
    else:
        return False    


if __name__=="__main__":
    '''variables'''
    CORAZONES = chr(9829)
    DIAMANTES = chr(9830)
    PICAS = chr(9824)
    TREBOL = chr(9827)
    jugadas = ["L-R","L-M","M-L","M-R","R-L","R-M"]# todas las posibles jugadas
    palo = [CORAZONES,DIAMANTES,PICAS,TREBOL] 
    numero = "123456789JK" 
    baraja = [("Q",palo[0]),(get_baraja_al_azar(numero,palo)),(get_baraja_al_azar(numero,palo))]
    NUMERO_CAMBIOS = 5 # numero de cambios que realiza el cupier
    DELAY = 0.2 # velocidad con la que cambia las cartas(modificable)
    '''fin de variables'''

    get_baraja_al_azar(numero,palo)
    shuffle(baraja) # desordena las barajas antes de imprimir por primera vez

    print("Three-Card Monte\n\nFind the red lady (the Queen of Hearts)! Keep an eye on how\n"\
        "the cards move.\n\nHere are the cards:")
    print(imprime(baraja))
    input("Press Enter when you are ready to begin...")
    
    while NUMERO_CAMBIOS>0:
        '''proceso en el que el cupier intercambia las cartas'''
        intercambio_cartas(baraja)
        time.sleep(DELAY)
        NUMERO_CAMBIOS -= 1
    
    pos = get_pos_carta(baraja)#posicion de la carta introducida por el usuario
    print(imprime(baraja))

    '''comprobacion'''
    if es_posicion(pos) == True:
        print("You win!\nYou are the king!")
    else:
        print("You lost!\nThanks for playing, sucker!")
