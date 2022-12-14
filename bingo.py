from random import randint, shuffle
import time

#constantes
LIMITE_INFERIOR = 100 # num serie cartones
LIMITE_SUPERIOR = 200
NUMERO_MENOR = 1 #numero bolas
NUMERO_MAYOR = 90
TACHADO = 'X'
DELAY = 0.8

# representa los números de serie de cada carton
def generar_numeros_serie(num_cartones):
    numeros_serie = []
    for i in range(num_cartones):
        numeros_serie.append(randint(LIMITE_INFERIOR,LIMITE_SUPERIOR))
    return sorted(numeros_serie) 

#genera carton de cada jugador
def generar_cartones(num_cartones):
    carton = [[],[],[]]
    cartones = {}
    numero_serie = generar_numeros_serie(num_cartones)
    for i in range(num_cartones):
        for fil in range(3):
            for col in range(5):
                num = randint(NUMERO_MENOR,NUMERO_MAYOR)  
                while num in carton[fil]:
                    num = randint(NUMERO_MENOR,NUMERO_MAYOR)  
                carton[fil].append(num)

        cartones[numero_serie[i]] = carton.copy()
        carton = [[],[],[]]

    return cartones
            


def imprimir(cartones):
    for carton in cartones:
        print("carton nº",carton,"\n--------------")
        for linea in cartones[carton]:
            for num in linea:
                print(num,end=" ")
            print()
        print()

def sacar_bola(bombo):
    shuffle(bombo)# mezcla de nuevo el bombo
    return bombo.pop()

def es_linea(cartones):
    encontrada_en_linea = 0
    x_encontradas = 0
    for carton in cartones:
        encontrada_en_linea = 0
        for linea in cartones[carton]:
            x_encontradas = 0 # las x encontradas en cada linea del cartón
            encontrada_en_linea += 1 # cada linea del carton
            for num in range(len(linea)):
                if linea[num] == 'X':
                    x_encontradas += 1  
            if x_encontradas==5:
                return encontrada_en_linea, carton
            

def es_bingo(cartones):
    for carton in cartones:
        num_x = 0
        for linea in cartones[carton]:
            for num in range(len(linea)):
                if linea[num] == 'X':
                    num_x += 1
        if num_x == 15:
            return carton
    

if __name__=="__main__":
    ronda = 0
    bombo = [int(bola) for bola in range(NUMERO_MENOR,NUMERO_MAYOR+1)]
    shuffle(bombo)
    bolas_jugadas = []
    bingo = None
    linea_encontrada = False

    # 1 carton x jugador
    num_cartones = int(input("Dime la cantidad de jugadores en la partida: "))
    numeros_serie = generar_numeros_serie(num_cartones)
    cartones = generar_cartones(num_cartones)
    
    print("\n\nComienza el juego con los siguientes cartones:")
    imprimir(cartones)

    while bingo==None:
        time.sleep(DELAY)
        ronda += 1
        bola = sacar_bola(bombo)
        print("Sale la bola:",bola)
        bolas_jugadas.append(bola) # todas las bolas jugadas

        # comprobar si la bola está en el carton
        for carton in cartones:
            for linea in cartones[carton]:
                if bola in linea: # si la bola está en la linea
                    for num in range(len(linea)):
                        if linea[num]==bola:
                            linea[num] = TACHADO
                            break   

        imprimir(cartones) # imprime el cartón
        linea = es_linea(cartones) #comprueba si hay linea

        if linea != None and linea_encontrada==False:                              
            print("!LINEA¡ Se ha completado la linea",linea[0], "en el cartón",linea[1])
            linea_encontrada = True
        
        #comprueba si hay bingo
        bingo = es_bingo(cartones)
        if bingo != None:
            print("!BINGO¡ El carton",bingo,"ha ganado\nSe ha terminado el juego en la ronda",ronda,"\n")
            break

        #imprime las bolas jugadas hasta ahora 
        if len(bolas_jugadas)>0:# imprime las bolas jugadas si hay más de una
            print("Estos son los números jugados hasta ahora ",end="")
            for i in range(len(bolas_jugadas)):
                print(bolas_jugadas[i],end=" ")# bola jugada
            print()
        



            
            
    


