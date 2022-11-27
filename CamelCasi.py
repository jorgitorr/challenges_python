palabras = {}
palabras_num_mayus = []
num_mayus = 0
palabra = ""

for i in range(2):
    cont_palabras = 0
    num_casos = int(input())
    for i in range(num_casos):
        palabra = input()

        cont_mayus = 0

        for i in range(len(palabra)):
            if palabra[i] == palabra[i].upper():
                cont_mayus += 1

        palabras_num_mayus.append([palabra,cont_mayus])

    for i in range(len(palabras_num_mayus)):#coge la primera palabra 
        num_mayus = 0
        palabra = ""
        cont_palabras += 1
        for j in range(len(palabras_num_mayus)):#recorre toda la lista
            #compara la primera palabra con la lista
            if palabras_num_mayus[i][0].lower() == palabras_num_mayus[j][0].lower():
                if num_mayus<palabras_num_mayus[j][1]:#si hay una palabra mayor en la lista la guarda
                    num_mayus = palabras_num_mayus[j][1]
                    palabra = palabras_num_mayus[j][0]
                    palabras[cont_palabras] = palabras_num_mayus[j]
        print()            
        print(palabra) 

    '''
    for i in range(1,len(palabras)):
        print(palabras[i])
    '''

    palabras_num_mayus.clear()
    print("---------------------")            








