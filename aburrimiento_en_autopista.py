casos = int(input())



while(casos>0):
    antiguo = 0
    moderno = 0
    matriculas = input().split(" ")

    for i in range(1,len(matriculas)-1):
        if matriculas[0][0:4]>matriculas[i][0:4]:
            antiguo+=1
            continue
        elif matriculas[0][0:4]==matriculas[i][0:4]:
            for j in range(4,7):
                if matriculas[0][j]<matriculas[i][j]:
                    antiguo+=1
                    continue
            else:
                moderno+=1
                continue
        else:
            moderno+=1
            continue

    casos-=1
    print(antiguo," ",moderno)

