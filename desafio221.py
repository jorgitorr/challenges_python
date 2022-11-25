#inicialización de variables
casos = int(input())
ramiro = True
cont_pares = 0
butaca = []

while(casos>0):
    butaca.clear()
    cont_pares = 0
    ramiro = True
    
    vecinos = int(input())
    num = input().split(" ")
    for i in range(vecinos):
        butaca.append(int(num[i])) 

    for i in range(len(butaca)-1):
        if butaca[i]%2!=0:
            for j in range(i+1,len(butaca)-1):
                if butaca[j]%2==0:#si hay un numero después de la i que sea par Ramiro no puede abrir la puerta
                    ramiro = False
                    break
        else:#cuenta los impares
            cont_pares+=1

    if ramiro:
        print("SI",cont_pares)
    else:
        print("NO")  

    casos -= 1      
