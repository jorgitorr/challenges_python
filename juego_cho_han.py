import random

D1 = ['+-------+',
      '|       |',
      '|   O   |',
      '|       |',
      '+-------+']

D2 = ['+-------+',
      '| O     |',
      '|       |',
      '|     O |',
      '+-------+']

D3 = ['+-------+',
      '| O     |',
      '|   O   |',
      '|     O |',
      '+-------+']

D4 = ['+-------+',
      '| O   O |',
      '|       |',
      '| O   O |',
      '+-------+']

D5 = ['+-------+',
      '| O   O |',
      '|   O   |',
      '| O   O |',
      '+-------+']

D6 = ['+-------+',
      '| O   O |',
      '| O   O |',
      '| O   O |',
      '+-------+']


def devuelve_dado():
    return random.randint(1,6)
    
def imprimir(pos_dado1, pos_dado2):
    dados = [(D1),(D2),(D3),(D4), (D5), (D6)]  
    pos_dado1 -= 1
    pos_dado2 -= 1 

    print(dados[pos_dado1][0], dados[pos_dado2][0] + "\n" +
        dados[pos_dado1][1], dados[pos_dado2][1] + "\n" +
        dados[pos_dado1][2], dados[pos_dado2][2] + "\n" +
        dados[pos_dado1][3], dados[pos_dado2][3] + "\n" +
        dados[pos_dado1][4], dados[pos_dado2][4] + "\n")

def es_suma_par(suma):
    if suma % 2 == 0:
        return True
    else:
        return False

if __name__=="__main__":
    dinero = 5000

    print("Cho-Han\nEn este juego de dados tradicional japonés, el croupier, sentado en el suelo\n" 
    "lanza dos dados en un cubilete de bambú. El jugador debe adivinar si los\n"
    "dados suman un número par (cho) o impar (han).")
    
    while dinero>0:
        print("tienes",dinero,"euros. ¿Cuánto apuestas? (o SALIR)")
        apuesta_dinero = input("> ")


        if apuesta_dinero == "SALIR":
            break

        print("El cupier hace girar el cubilete y se oye el traqueteo de los dados.\n"
        "El cupier gira el cubilete contra el suelo, todavía cubriendo los\n"
        "dados y pide tu apuesta.\n\nCHO (par) or HAN (impar)?")
        apuesta_dados = input("> ").upper()
        print("El cupier levanta el cubilete para revelar:")
        dado1, dado2 = devuelve_dado(),devuelve_dado() 
        
        match(dado1):
            case 1:
                print("     ICHI",end="-")
            case 2:
                print("      Ni",end="-")
            case 3:
                print("     SAN",end="-")
            case 4:
                print("     SHI",end="-")
            case 5:
                print("      GO",end="-")
            case 6:
                print("     ROKU",end="-")  

        match(dado2):
            case 1:
                print("ICHI")
            case 2:
                print("Ni")
            case 3:
                print("SAN")
            case 4:
                print("SHI")
            case 5:
                print("GO")
            case 6:
                print("ROKU")          

        imprimir(dado1,dado2)
        
        suma = dado1 + dado2
        par = es_suma_par(suma)

        #comprobación de apuesta
        if (par and apuesta_dados=="CHO") or (par == False and apuesta_dados=="HAN"):
            print("!Has ganado!")
            apuesta_dinero = int(apuesta_dinero)
            tasa = (apuesta_dinero * 10)/100
            print("La casa se lleva",tasa,"euros en tasas")
            apuesta_dinero -= tasa
            dinero += apuesta_dinero
        elif (par and apuesta_dados=="HAN") or (par == False and apuesta_dados=="CHO"):
            print("!Has perdido!")   
            dinero -= int(apuesta_dinero)
        else:
            print("No es una apuesta correcta")


if dinero==0:
    print("Te quedaste sin blanca huevón")    

        

