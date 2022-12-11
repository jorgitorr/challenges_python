import random, time

'''constantes'''
TREBOL = chr(9827)
CORAZONES = chr(9829)
PICAS = chr(9824)
DIAMANTES = chr(9830)
DELAY = 0.5

def get_baraja(baraja):
    valor = random.choice("23456789JQKA")
    palo = random.choice([TREBOL,CORAZONES,PICAS,DIAMANTES])
    baraja.append((valor,palo))
    return baraja


def get_valor_cartas(baraja,valor_cartas):
    num = "23456789"
    valor = 0
    for carta in baraja:
        if carta[0] in num:
            valor += int(carta[0])    
        elif "A" in carta[0]:
            if valor_cartas<21:#le suma 1 o 10 dependiendo del valor de las cartas
                valor += 10
            elif valor_cartas+10>=21:
                valor += 10    
        else:    
            valor += 10
    return valor


def imprimir(baraja):
    for carta in baraja:
        print(" _____ " + "  \n"\
            "|" + carta[0] + "    |\n"\
            "|  " + carta[1] + "  |\n"\
            "|____" + carta[0] + "|")


        
if __name__=="__main__":
    baraja_cupier = []
    baraja_jugador = []
    money =  5000

    print("Blackjack, by Al Sweigart al@inventwithpython.com\n Rules:"\
        "Try to get as close to 21 without going over.\n"\
        "Kings, Queens, and Jacks are worth 10 points.\n"\
        "Aces are worth 1 or 11 points.\n"\
        "Cards 2 through 10 are worth their face value.\n"\
        "(H)it to take another card.\n"\
        "(S)tand to stop taking cards.\n"\
        "On your first play, you can (D)ouble down to increase your bet\n"\
        "but must hit exactly one more time before standing.\n"\
        "In case of a tie, the bet is returned to the player.\n"\
        "The dealer stops hitting at 17.\n"\
        "How much do you bet? (1-5000, or QUIT)")
    
    print("Money:",money)
    bet = int(input("> "))
    print("Bet:",bet)

    '''primera jugada'''
    get_baraja(baraja_cupier)
    get_baraja(baraja_cupier)#esta carta se ocultará
    get_baraja(baraja_jugador)
    get_baraja(baraja_jugador)

    '''valor de las cartas del cupier y el jugador'''
    valor_cartas_cupier = get_valor_cartas(baraja_cupier,0)# 0 porque al principio A siempre vale 10
    valor_cartas_jugador = get_valor_cartas(baraja_jugador,0)

    '''impresion de las cartas del dealer y player y de su valor'''
    print("DEALER: ??")
    baraja_imprimir_cupier = [baraja_cupier[0],("#","#")]# nueva baraja para poder imprimir la segunda carta oculta
    imprimir(baraja_imprimir_cupier)
    print("\nPLAYER:",valor_cartas_jugador)
    imprimir(baraja_jugador)


    while money > 0:
        '''jugada siguiente'''
        print("\n(H)it, (S)tand, (D)ouble down")
        play = input("> ").upper()

        if play == "H" or play == "D":
            get_baraja(baraja_jugador)
            get_baraja(baraja_cupier)

            '''se suman las nuevas cartas al valor'''
            valor_cartas_cupier = get_valor_cartas(baraja_cupier,valor_cartas_cupier)
            valor_cartas_jugador = get_valor_cartas(baraja_jugador,valor_cartas_jugador)
            if play=="D":
                bet = bet*2

            '''imprime las cartas'''
            print("DEALER:",valor_cartas_cupier)
            imprimir(baraja_cupier)
            print("\nPLAYER:",valor_cartas_jugador)
            imprimir(baraja_jugador)

        '''saldrá cuando el jugador decida parar de apostar o haya perdido alguno de los dos'''
        if valor_cartas_cupier>=21 or valor_cartas_jugador>=21 or play=="S":
            if valor_cartas_jugador>21 and valor_cartas_cupier<=21 or (valor_cartas_cupier>valor_cartas_jugador and valor_cartas_cupier<=21):
                money -= bet
                print("You lose","€",bet,"!") 
                break
            elif valor_cartas_jugador==valor_cartas_cupier:
                print("Empate")
                break
            elif valor_cartas_jugador>valor_cartas_cupier or valor_cartas_jugador<=21:
                money += bet
                print("You won","€",bet,"!")  
                break

print("You live the game with",money)