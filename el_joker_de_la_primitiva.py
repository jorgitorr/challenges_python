casos = int(input())


while casos>0:
    num = input().split(" ")

    num2 = num[1]
    num = num[0]
    gana = True

    i = 0
    j = 0
    cont = 0

    while i<len(num) and j<len(num2):
        if num[i]==num2[j]:
            cont += 1  
            num2 = num2.replace(num2[j],"",1)
            j = 0
            if i<len(num):
                i += 1
        else:
            j += 1


    if cont==len(num):
        print("GANA")
    else:
        print("PIERDE")

    cont = 0

    casos-=1