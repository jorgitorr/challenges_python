casos = int(input())
frase = ""
palabra = ""
for i in range(casos):
    frase = input().lower().replace(" ", "")
    palabra = input().lower().replace(" ", "")
    iguales = False
    contador = 0
    j = 0
    while j < len(frase):
        if frase[j] == palabra[contador]:
            contador += 1

            if contador == len(palabra):
                iguales = True
                break
        j += 1
    print("SI" if iguales else "NO")

    #de esta forma no vuelve a recorrer la frase ya que la recorre y la j sigue conservando el mismo valor