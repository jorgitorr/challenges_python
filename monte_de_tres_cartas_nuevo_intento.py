import random, time
from random import shuffle

#constantes
CORAZONES = chr(9829)
DIAMANTES = chr(9830)
PICAS = chr(9824)
TREBOL = chr(9827)
NUMERO_CAMBIOS = 5 
DELAY = 0.2 


def get_carta_azar():
    cartas = []
    carta1 = ("Q",CORAZONES)
    carta2 = random.choice(list("123456789JK")+ ['10']),random.choice([CORAZONES,DIAMANTES,PICAS,TREBOL])
    carta3 = random.choice(list("123456789JK")+ ['10']),random.choice([CORAZONES,DIAMANTES,PICAS,TREBOL])
    if carta2 in cartas:
        carta2 = random.choice(list("123456789JK")+ ['10']),random.choice([CORAZONES,DIAMANTES,PICAS,TREBOL])
    if carta3 in cartas:
        carta3 = random.choice(list("123456789JK")+ ['10']),random.choice([CORAZONES,DIAMANTES,PICAS,TREBOL])
    cartas = [(carta1),(carta2),(carta3)]
    return cartas


def imprime(cartas):
    print(" _____ " + " " + " _____ " + " " + " _____ \n"\
          "|" + f'{cartas[0][0]:>2}' + "   |" + " " + "|" + f'{cartas[1][0]:>2}' + "   |" + " " + "|" + f'{cartas[2][0]:>2}' + "   |\n"\
          "|  " + cartas[0][1] + "  |" + " " + "|  " + cartas[1][1] + "  |" + " " + "|  " + cartas[2][1] + "  |\n"\
          "|___" + f'{cartas[0][0]:>2}' + "|" + " " + "|___" + f'{cartas[1][0]:>2}' + "|" + " " + "|___" + f'{cartas[2][0]:>2}' + "|")

def get_pos_carta(pos_usuario, cartas):# le tengo que pasar las cartas por parámetros para que no coja la variable global
    if pos_usuario=="LEFT":
        if cartas[0] == ("Q",CORAZONES):
            return True
        else:
            return False    
    elif pos_usuario=="MIDDLE":
        if cartas[1] == ("Q",CORAZONES):
            return True
        else:
            return False 
    elif pos_usuario=="RIGHT":
        if cartas[2] == ("Q",CORAZONES):
            return True
        else:
            return False     


if __name__=="__main__":
    #variables
    movimientos = ["L-R","L-M","M-L","M-R","R-L","R-M"]# todas las posibles jugadas
    cartas = get_carta_azar()

    shuffle(cartas) # desordena las barajas antes de imprimir por primera vez

    print("Three-Card Monte\n\nFind the red lady (the Queen of Hearts)! Keep an eye on how\n"\
        "the cards move.\n\nHere are the cards:")
    imprime(cartas)
    input("Press Enter when you are ready to begin...")
    

    for i in range(NUMERO_CAMBIOS):
        jugada_cupier = random.choice(movimientos)
        if jugada_cupier == 'L-R':
            print("swapping left and right")
            cartas[0],cartas[2] = cartas[2],cartas[0]
        elif jugada_cupier == "L-M":
            print("swapping left and middle")
            cartas[0],cartas[1] = cartas[1],cartas[0] 
        elif jugada_cupier == "M-L":
            print("swapping middle and left")
            cartas[1],cartas[0] = cartas[0],cartas[1]
        elif jugada_cupier == "M-R":
            print("swapping middle and right")
            cartas[1],cartas[2] = cartas[2],cartas[1]
        elif jugada_cupier == "R-L":
            print("swapping right and left")
            cartas[2],cartas[0] = cartas[0],cartas[2]
        elif jugada_cupier == "R-M":
            print("swapping right and middle")    
            cartas[2],cartas[1] = cartas[1],cartas[2]
        time.sleep(DELAY)
    
    print("--snip--")
    pos = input("Wich card has the Queen of Hearts? (LEFT MIDDLE RIGHT)\n> ").upper()
    imprime(cartas)

    if get_pos_carta(pos, cartas) == True:
        print("You win!\nYou are the king!")
    else:
        print("You lost!\nThanks for playing, sucker!")


