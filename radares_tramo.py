introduce = input().split(" ")
while(introduce[0] != "0" or introduce[1]!="0" or introduce[2]!="0"):

    while int(introduce[0]) < 0 or int(introduce[1]) < 0 \
            or int(introduce[2]) < 0:
        print("ERROR")
        introduce = input().split(" ")
        
    #pasamos de metros a km
    introduce[0] = int(introduce[0])/1000
    #pasamos de segundos a horas
    introduce[2] = int(introduce[2])/3600


    #calcular la velocidad
    velocidad = introduce[0]/introduce[2]
    porcentaje = int(introduce[1]) + int(int(introduce[1])*20)/100


    #comparamos la velocidad máxima
    if velocidad == introduce[1]:
        if len(velocidad)>len(introduce[1]):
            print("MULTA")
        else:
            print("OK")
    elif int(velocidad) < int(introduce[1]):
        print("OK")
    else:
        if int(velocidad) < porcentaje:
            print("MULTA")
        elif velocidad > porcentaje:
            print("PUNTOS")

    introduce = input().split(" ")