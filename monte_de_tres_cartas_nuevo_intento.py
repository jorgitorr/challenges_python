import random, time
from random import shuffle

'''constantes'''
CORAZONES = chr(9829)
DIAMANTES = chr(9830)
PICAS = chr(9824)
TREBOL = chr(9827)

NUMERO_CAMBIOS = 5 # numero de cambios que realiza el cupier (modificable)
DELAY = 0.2 # velocidad con la que cambia las cartas(modificable)
''''''

def get_carta_azar():
    '''tengo que comprobar que las cartas son diferentes''' 
    return random.choice(list("123456789JK")+ ['10']),random.choice([CORAZONES,DIAMANTES,PICAS,TREBOL])


def imprime(baraja):
    print(" _____ " + " " + " _____ " + " " + " _____ \n"\
          "|" + baraja[0][0] + "    |" + " " + "|" + baraja[1][0] + "    |" + " " + "|" + baraja[2][0] + "    |\n"\
          "|  " + baraja[0][1] + "  |" + " " + "|  " + baraja[1][1] + "  |" + " " + "|  " + baraja[2][1] + "  |\n"\
          "|____" + baraja[0][0] + "|" + " " + "|____" + baraja[1][0] + "|" + " " + "|____" + baraja[2][0] + "|")


def get_pos_carta(pos_usuario):
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
    jugadas = ["L-R","L-M","M-L","M-R","R-L","R-M"]# todas las posibles jugadas
    baraja = [("Q",CORAZONES),(get_carta_azar()),(get_carta_azar())]
    '''fin de variables'''

    get_carta_azar()
    shuffle(baraja) # desordena las barajas antes de imprimir por primera vez

    print("Three-Card Monte\n\nFind the red lady (the Queen of Hearts)! Keep an eye on how\n"\
        "the cards move.\n\nHere are the cards:")
    imprime(baraja)
    input("Press Enter when you are ready to begin...")
    

    for i in range(NUMERO_CAMBIOS):#principio de responsabilidad única (que una función haga una única cosa)
        jugada_cupier = random.choice(jugadas)
        '''proceso en el que el cupier intercambia las cartas'''
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
        time.sleep(DELAY)
    
    print("--snip--")
    pos = input("Wich card has the Queen of Hearts? (LEFT MIDDLE RIGHT)\n> ").upper()
    pos_en_num = get_pos_carta(pos)
    imprime(baraja)

    '''comprobacion'''
    if es_posicion(pos_en_num) == True:
        print("You win!\nYou are the king!")
    else:
        print("You lost!\nThanks for playing, sucker!")


