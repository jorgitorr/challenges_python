if __name__=="__main__":
    abecedario = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

    print("Do you want to (e)ncrypt or (d)ecrypt?")
    en_de_crypt = input("> ").lower()
    print("Please enter the key (0 to 25) to use.")
    key = int(input("> "))
    print("Enter the message to encrypt.")
    message = input("> ").lower()

    secret = "" # palabra secreta o palabra desvelada
    if en_de_crypt == "e":
        '''encripta el mensaje'''
        for i in range(len(message)):
            j = 0
            if message[i]==" ":
                secret += " "
            else:    
                for j in range(len(abecedario)):
                    if message[i] == abecedario[j]:
                        secret += abecedario[j+key].upper()
                        break
    elif en_de_crypt == "d":
        '''desencripta el mensaje'''
        for i in range(len(message)):
            j = 0
            if message[i]==" ":
                secret += " "
            else:    
                for j in range(len(abecedario)):
                    if message[i] == abecedario[j]:
                        secret += abecedario[j-key].upper()
                        break

    print(secret,"\nFull encrypted text copied to clipboard")



