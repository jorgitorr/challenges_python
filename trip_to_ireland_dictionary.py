#variables globales
personas_ida_vuelta = []

avion = {
5:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
6:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
7:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
8:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
9:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
10:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
11:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
12:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
13:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
14:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
15:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
16:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
17:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
18:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
19:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
20:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
21:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
22:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
23:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
24:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
25:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
26:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
27:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
28:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
29:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
30:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
31:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
32:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
33:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
34:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
35:{'A':'-----','B':'-----','C':'-----','D':'-----','E':'-----'},
}

avion_vuelta = avion #asigna al otro diccionario los mismos valores

def pide_personas():
    for i in range(27):
        personas_ida_vuelta.append(input().split())


def comprueba_ida():
    for numero in avion:
        for i in range(len(personas_ida_vuelta)):
            if numero == int(personas_ida_vuelta[i][1][:2]):
                for letra in avion[numero]:
                    if letra == personas_ida_vuelta[i][1][2:]:
                        avion[numero][letra] = personas_ida_vuelta[i][0]
    return avion

def comprueba_vuelta():
    for numero2 in avion_vuelta:
        for i in range(len(personas_ida_vuelta)):
            if numero2 == int(personas_ida_vuelta[i][2][:2]):
                for letra2 in avion[numero2]:
                    if letra2 == personas_ida_vuelta[i][2][2:]:
                        avion_vuelta[numero2][letra2] = personas_ida_vuelta[i][0]
    return avion_vuelta

#un solo método para imprimir los dos aviones
def imprime(avion):
    print("VUELTA")
    filas = 5
    for filas2 in avion:
        print("row",filas,":",end=" ")
        filas += 1
        for celda in avion[filas2]:
            print(avion[filas2][celda],end=" ")
        print()    


def programa():
    pide_personas()
    avion = comprueba_ida()
    imprime(avion)
    print()
    avion_vuelta = comprueba_vuelta()
    imprime(avion_vuelta)

programa()    