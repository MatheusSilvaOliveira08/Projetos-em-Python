import random 

escolha = ('pedra', 'papel', 'tesoura')

while (True):
    usuario_escolha = input ("Escolha entre pedra, papel ou tesoura: ").lower()

    if (usuario_escolha not in escolha): 
        print ('Resposta inválida...')
        continue

    computador_escolha = random.choice(escolha)

    if (usuario_escolha == computador_escolha): 
        print ('Empate!')

    elif ((usuario_escolha == 'pedra' and computador_escolha == 'tesoura') or 
          (usuario_escolha == 'tesoura' and computador_escolha == 'papel') or 
          (usuario_escolha == 'pepel' and computador_escolha == 'pedra')):
        print ('Parabéns! Você ganhou')
    
    else: 
        print ('Você perdeu...')
    
    Continua = input ('Deseja continuar? (s/n) ').lower()

    if (Continua == 'n'): 
        break
    