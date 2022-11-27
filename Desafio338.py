for i in range(3):
    examenes = {}
    ex_detectados_x_profesor = {}
    total_ex_copiados = 0
    cont_ex_detectados = 0
    cont_ex_repetidos = 0

    num_examenes = input().split(" ")
    respuestas_examenes = input().split(" ")

    #convierte las listas de string a entero
    for i in range(len(num_examenes)):
        num_examenes[i] = int(num_examenes[i])

    for i in range(len(respuestas_examenes)):
        respuestas_examenes[i] = int(respuestas_examenes[i])

    copias_detectadas = num_examenes[1]
    #guarda las repeticiones de examenes
    cont_ex_repetidos = 0
    for i in range(len(respuestas_examenes)):
        if respuestas_examenes[i] in examenes:
            examenes[respuestas_examenes[i]]+=1
        else:    
            examenes[respuestas_examenes[i]] = cont_ex_repetidos

    #suma los valores para saber cuantos examenes copiados hay
    for repeticiones in examenes.values():
        total_ex_copiados+=repeticiones

    #guarda los examenes detectados por el profesor
    for i in range(len(respuestas_examenes)-1):#empieza el len()-1 porque empieza en 0 y sino sobrepasa el rango
        if copias_detectadas>0:
            #guardo el num con la ubicación 
            ex_detectados_x_profesor[((len(respuestas_examenes)-1))] = respuestas_examenes[(len(respuestas_examenes)-1)] 
            respuestas_examenes.pop((len(respuestas_examenes)-1))#como es pop el primero es 0
            copias_detectadas -= 1
        else:
            break    

    #comprueba que el valor del examen no sea el mismo que el que estoy comprbando
    #para que no añada al contador el mismo numero
    for i in range(len(respuestas_examenes)-1):
        for examen in ex_detectados_x_profesor:
            if len(respuestas_examenes)==0:
                break
            elif respuestas_examenes[(len(respuestas_examenes)-1)]==ex_detectados_x_profesor[examen]:
                cont_ex_repetidos += 1
                respuestas_examenes.pop(len(respuestas_examenes)-1)  


    print(total_ex_copiados,cont_ex_repetidos)        