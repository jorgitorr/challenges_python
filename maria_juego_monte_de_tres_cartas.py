from random import sample, randint

#constantes palo
CORAZONES = chr(9829)
DIAMANTES = chr(9830)
PICAS = chr(9824)
TREBOL = chr(9827)

def dibujar_cartas(cartas):
    print(" _____ " + " " + " _____ " + " " + " _____ \n"\
          "|" + cartas[0][0] + "    |" + " " + "|" + cartas[1][0] + "    |" + " " + "|" + cartas[2][0] + "    |\n"\
          "|  " + cartas[0][1] + "  |" + " " + "|  " + cartas[1][1] + "  |" + " " + "|  " + cartas[2][1] + "  |\n"\
          "|____" + cartas[0][0] + "|" + " " + "|____" + cartas[1][0] + "|" + " " + "|____" + cartas[2][0] + "|")

def generar_cartas():
    palos = [CORAZONES, DIAMANTES, PICAS, TREBOL]
    numeros = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "K", "A"]
    lista = [(numeros[randint(0, 10)], palos[randint(0, 3)]), (numeros[randint(0, 10)], palos[randint(0, 3)]), ("Q", palos[0])]
    return sample(lista, len(lista)) 

def generar_movimientos():    
    movimientos = ["izq-med", "izq-dcha", "med-izq", "med-dcha", "dcha-izq", "dcha-med"]
    return sample(movimientos, 6)

def mover_cartas(movimientos, cartas):
    for movimiento in movimientos:
        if movimiento == "izq-med" or movimiento == "med-izq": 
            aux = cartas[0] 
            cartas[0] = cartas[1]
            cartas[1] = aux
        elif movimiento == "dcha-med" or movimiento == "med-dcha":
            aux = cartas[1]
            cartas[1] = cartas[2]
            cartas[2] = aux
        elif movimiento == "dcha-izq" or movimiento == "izq-dcha":
            aux = cartas[0]
            cartas[0] = cartas[2]
            cartas[2] = aux
    
def determinar_victoria(opcion, cartas):
    acierto = False
    if opcion == "IZQUIERDA": 
        if cartas[0][0] == 'Q' and cartas[0][1] == CORAZONES: acierto = True
    elif opcion == "MEDIO":
        if cartas[1][0] == 'Q' and cartas[1][1] == CORAZONES: acierto = True
    elif opcion == "DERECHA":
        if cartas[2][0] == 'Q' and cartas[2][1] == CORAZONES: acierto = True
    return acierto
    

#principal

print("---------------------\n" + \
      "Monte de Tres Cartas \n" + \
      "---------------------\n")
print("¡Encuentra la dama roja (la Reina de Corazones)! Presta atención en como se mueven las cartas.\n")
print("Aquí están las cartas:")

cartas = generar_cartas()

dibujar_cartas(cartas)

input("\nPulsa \"enter\" cuando estés preparado para empezar...")

movimientos = generar_movimientos()

for movimiento in movimientos:    
    if movimiento == "izq-med":
        print("intercambiando izquierda y medio...")
    elif movimiento == "dcha-med":
        print("intercambiando derecha y medio...")
    elif movimiento == "dcha-izq":
        print("intercambiando derecha e izquierda...")
    elif movimiento == "med-dcha":
        print("intercambiando medio y derecha...")
    elif movimiento == "izq-dcha":
        print("intercambiando izquierda y derecha...")
    elif movimiento == "med-izq":
        print("intercambiando medio e izquierda...")

mover_cartas(movimientos, cartas)

print("\n¿Qué carta tiene la Reina de Corazones? (IZQUIERDA MEDIO DERECHA)")
opcion = input().upper()

dibujar_cartas(cartas)

if determinar_victoria(opcion, cartas):
    print("\n¡Ganaste!")
else:
    print("\n¡Perdiste!")

print("¡Gracias por jugar!")