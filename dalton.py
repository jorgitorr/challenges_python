n = int(input())

dalton = True
alturaAnterior= 0

while(n!=0):
	alturaAnterior = 0
	for i in range(n):
		altura = input()
		dalton = True
		alturaAnterior = 0
		for j in range(len(altura)):
			if(altura[j]!=" "):
				if int(alturaAnterior)>int(altura[j]):
					dalton = False
				if int(altura[j]) == int(alturaAnterior):
					dalton = False
				alturaAnterior = int(altura[j])

		if(dalton):
			print("DALTON")
		else:
			print("DESCONOCIDO")		
		
		n = int(input())
		if(n==0):
			break	
