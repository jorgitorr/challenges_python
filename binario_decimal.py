#DE BINARIO A DECIMAL

binario = input("Introduce binario")
resultado = 0

for i in range(len(binario)):
    resultado += int(binario[(len(binario) - 1) - i]) * pow(2, i)

print(binario, "=", resultado)


#DE DECIMAL A BINARIO
decimal = int(input("Introduce decimal "))
resultado_resto= 1
resultado_divisor = decimal
resultado_binario = ""

while(resultado_divisor!=1):
    resultado_binario += str(resultado_divisor%2)
    resultado_divisor = resultado_divisor//2

#le añadimos uno al resultado del divisor de 2
resultado_binario += "1"
#ponemos el numero binario al revés
resultado_binario = resultado_binario[::-1]
print(resultado_binario)
