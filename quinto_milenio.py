casos = int(input())

while(casos>0):
	cont = 0
	
	frase = input()
	palabra = input()

	for i in range(len(palabra)):
		if i>0 and cont==0:
			break
		while palabra[i]==" ":
			i+=1
		for j in range(len(frase)):
			if frase[j].lower()==palabra[i]:
				cont+=1


	if cont>=len(palabra):
		print("SI")
	else:
		print("NO")	
					
	casos-=1
