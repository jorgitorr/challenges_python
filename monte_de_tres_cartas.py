from random import sample
import random
import time

def baraja(cartas):
    for i in range(2,10):
        cartas.append(str(i)+" DE CORAZONES")
        cartas.append(str(i)+" DE DIAMANTES")
        cartas.append(str(i)+" DE PICAS")
        cartas.append(str(i)+" DE TREBOL")
    cartas.append("K DE CORAZONES")
    cartas.append("J DE CORAZONES")
    cartas.append("K DE DIAMANTES")
    cartas.append("J DE DIAMANTES")
    cartas.append("K DE PICAS")
    cartas.append("J DE PICAS")
    cartas.append("K DE TREBOL")
    cartas.append("J DE TREBOL")
    return cartas

def saco_dos_cartas(cartas):
    '''metodo para quedarse con dos cartas al azar de todas la baraja'''
    cartas = sample(cartas,2)
    return cartas


def anadio_desordeno(cartas):
    '''añade carta conocido Q y desordena la lista'''
    cartas.append("Q")
    random.shuffle(cartas)
    return cartas

def carta_posicion(pos_cartas,cartas,posiciones):
    '''añado los nombres de la carta como key y su posicion como valor'''
    pos_cartas[cartas[0]] = posiciones[0]
    pos_cartas[cartas[1]] = posiciones[1]
    pos_cartas[cartas[2]] = posiciones[2]
    return pos_cartas

def cupier_modifica_pos(posiciones, pos_cartas):
    '''el cupier elige modifica dos posiciones'''
    posiciones = sample(posiciones,2)# el cupier coge 2 posiciones al azar

    print("Swapping",str(posiciones[0]).lower(),"and",str(posiciones[1]).lower(),"...")

    for key, value in pos_cartas.items():
        if value == posiciones[0]:
            pos_cartas[key] = posiciones[1]
        elif value == posiciones[1]:
            pos_cartas[key] = posiciones[0]

    return pos_cartas
   

def intento_jugador():
    return input("¿Which card has the Queen of Hearts? (LEFT, MIDDLE, RIGHT) ")
    
def comprueba_q(jugador,pos_cartas):
    if jugador != pos_cartas["Q"]:
        return False
    else:
        return True  

def impresion(key, numero):
        if "Q" in key: #Q (CARTA CONOCIDA)
            print("-----\n"+"|"+"Q"," |\n"+"| "+chr(9829)+" |\n"+"| "+" Q"+"|\n"+"-----")
        elif "DIAMANTES" in key: 
            print("-----\n"+"|"+numero," |\n"+"| "+chr(9830)+" |\n"+"| "+" "+numero+"|\n"+"-----")
        elif "PICAS" in key:
            print("-----\n"+"|"+numero," |\n"+"| "+chr(9824)+" |\n"+"| "+" "+numero+"|\n"+"-----")
        elif "TREBOL" in key:
            print("-----\n"+"|"+numero," |\n"+"| "+chr(9827)+" |\n"+"| "+" "+numero+"|\n"+"-----") 
        elif "CORAZONES" in key:
            print("-----\n"+"|"+numero," |\n"+"| "+chr(9829)+" |\n"+"| "+" "+numero+"|\n"+"-----") 

def comprueba_posicion_para_impresion(pos_cartas):
    '''imprime la carta segun la posicion'''
    for key, value in pos_cartas.items():
        numero = str(numero_cartas(key))
        if value == "LEFT":
            impresion(key,numero)
                
    for key, value in pos_cartas.items():
        numero = str(numero_cartas(key))
        if value == "MIDDLE":
            impresion(key,numero)

    for key, value in pos_cartas.items():
        numero = str(numero_cartas(key))
        if value == "RIGHT":
            impresion(key,numero)

def numero_cartas(key):
    '''primero comprobamos si es o no un número y devuelve el numero o letra correspondiente para la futura impresión'''
    if "J" in key:
        return "J"
    elif "K" in key:
        return "K"  
    else:         
        for num in range(2,10):
            if str(num) in key:
                return num



if __name__=="__main__":
    cartas = [] #baraja de cartas
    posiciones = ["LEFT","MIDDLE","RIGHT"] # todas las posiciones posibles de las cartas
    pos_cartas = {} #las 3 cartas elegidas de la baraja junto con su posición

    cartas = baraja(cartas)
    cartas = saco_dos_cartas(cartas)
    cartas = anadio_desordeno(cartas)

    carta_posicion(pos_cartas,cartas,posiciones)# cartas sin que las toque el cupier
    print(pos_cartas)
    comprueba_posicion_para_impresion(pos_cartas)

    NUMERO_INTERCAMBIOS = 10 #numero de intercambios que hace el cupier
    while(NUMERO_INTERCAMBIOS>0):
        cupier_modifica_pos(posiciones,pos_cartas)# cartas modificadas por el cupier
        time.sleep(0)
        NUMERO_INTERCAMBIOS -= 1

    jugador = intento_jugador()# intento del jugador
    '''el metodo comprobar impresion contiene el metodo imprimir, por eso imprime'''
    comprueba_posicion_para_impresion(pos_cartas)

    # comprueba si la carta del jugador está en la posicion que indica el usuario
    if comprueba_q(jugador,pos_cartas) == False:
        print("You lost!\nThanks for playing sucker")
    else:
        print("You win!\nYou are the best!") 





