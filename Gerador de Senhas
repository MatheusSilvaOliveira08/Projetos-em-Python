import random
import string

def gerar_senha (tamanho, number, special_character): 
    letras = string.ascii_letters
    digitos = string.digits
    special_char = string.punctuation

    senha = ''

    if (numeros == 's'): 
        letras += digitos
    
    if (special == 's'): 
        letras += special_char

    if (numeros == 's'): 
        letras += random.choice (digitos)

    if (special == 's' ):
        letras += random.choice (special_char)

    while (len(senha) < tamanho_senha): 
        letra_nova = random.choice(letras)
        senha += letra_nova

    return senha


tamanho_senha = int(input('Qual o tamanho da senha que você deseja gerar? '))
numeros = input('Deseja que sua senha contenha números (s/n)? ').lower()
special = input('Deseja que sua senha contenha caracteres especiais (s/n)? ').lower()

senha = gerar_senha(tamanho_senha, numeros,special)

print ('A sua senha gerada é: ', senha)
