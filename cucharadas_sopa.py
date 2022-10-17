casos = int(input())

while casos>0:
    if casos == 0:
        break

    for i in range(casos):
        fila = input().split(" ")
        cont = 0
        for i in range(int(fila[1]), 0, -1):
            min_mafalda = int(fila[0])
            max_padre = i
            if min_mafalda + max_padre == int(fila[2]):
                break
        if min_mafalda + max_padre != int(fila[2]):
            for j in range(min_mafalda,int(fila[2])):
                min_mafalda = j
                max_padre = int(fila[1])
                if min_mafalda + max_padre == int(fila[2]):
                    break
        while min_mafalda + max_padre == int(fila[2]):
            cont += 1
            min_mafalda +=1
            max_padre -= 1
            if max_padre < 0:
                break

        print(cont)


    casos = int(input())



