#casos de prueba 
casos = 2
lista_tunel = []
num = []

while casos>0:
    tunel = input()
    lista_tunel.clear()
    num.clear()

    for i in range(len(tunel)):
        lista_tunel.append(tunel[i])

    numero_consultas = int(input())
    for i in range(numero_consultas):
        num.append(int(input())) 

    for n in range(len(num)):#recorre el num
        x = 0
        if lista_tunel[(num[n]-1)] =='T':
            print("AQUÍ")
        else:
            while x<len(lista_tunel):
                if x==len(lista_tunel)-1:
                    print("PENINSULA")
                    break
                if lista_tunel[(num[n]-1)+x] == 'T': 
                    #si encuentra primero la t sumando tiene que coger el tunel hacia las islas
                    print("ISLAS")  
                    break
                elif lista_tunel[(num[n]-1)-x] == 'T':
                    #si encuentra primero la t restando tiene que coger el tunel hacia la peninsula
                    print("PENINSULA")  
                    break 
                x+=1
    casos -= 1