import random 

numero_random = random.randint(1,100)

while (True): 
    try: 
        adivinhe = int ( input ("Tente adivinhar o número: "))

        if (adivinhe < numero_random): 
            print ("Tente um número mais alto")

        elif (adivinhe > numero_random): 
            print ("Tente um número mais baixo")
        
        else: 
            print ("Parabéns! Você acertou o número")
            break
    
    except ValueError: 
        print ("Tente um número válido")
