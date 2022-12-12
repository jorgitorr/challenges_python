num_lineas = int(input())
palabra_num = {}

while num_lineas!=0:
    for num in range(num_lineas):
        linea = input().lower().split(" ")
        for i in range(len(linea)):
            if len(linea[i]) > 2:# que la palabra sea de +2 length
                if linea[i] in palabra_num:
                    if str(num+1) not in palabra_num[linea[i]]:
                        palabra_num[linea[i]] += " " + str(num+1)
                else:
                    palabra_num[linea[i]] = str(num+1)    

    palabra_num = dict(sorted(palabra_num.items()))# ordena el diccionario
    for palabra in palabra_num:
        print(palabra," ",palabra_num[palabra])
    print("------------")
    num_lineas = int(input())




