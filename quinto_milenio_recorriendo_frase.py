casos = int(input())

while (casos > 0):
    cont = 0

    frase = input()
    palabra = input()

    for i in range(len(palabra) - 1):
        if i > 0 and cont == 0:
            break
        while palabra[i] == " ":
            i += 1
        for j in range(len(frase) - 1):
            aux_j += 1  # se le agrega 1
            j = aux_j  # para seguir la frase
            if j >= len(frase) - 1:
                break
            if frase[j].lower() == palabra[i]:
                cont += 1
                aux_j = j
                break

    if cont >= len(palabra):
        print("SI")
    else:
        print("NO")

    casos -= 1