import os
from cryptography.fernet import Fernet


def escrever_chave (): 
    chave = Fernet.generate_key()
    with open ('key.key', 'wb') as arquivo_chave: 
        arquivo_chave.write(chave)


def carregar_chave (): 

    if not os.path.exists('key.key'): 
        escrever_chave()

    with open ('key.key', 'rb') as chave_arquivo: 
        return chave_arquivo.read()

chave = carregar_chave()
fer = Fernet (chave)

def view (): 
    with open ('senha.txt', 'r') as arquivo: 
        for linha in arquivo: 
            usuario, senha_cripto = linha.split(' - ')
            senha_descripto = fer.decrypt(senha_cripto.encode()).decode()

            print (f'Usuário: {usuario} - Senha: {senha_descripto}')

def add (): 
    nome = input ('Escreva o nome do usuário: ')
    senha = input ('Insira a sua senha: ')
    senha_cripto = fer.encrypt(senha.encode()).decode()

    with open ('senha.txt', 'a' ) as arquivo:
        arquivo.write(nome + ' - ' + senha_cripto + '\n')


while (True): 
    escolha = input ('Deseja adicionar uma nova senha ou visualizar uma existente (add/view), ou aperte s para sair? ')

    if (escolha == 's'): 
        break

    if (escolha == 'add'): 
        add()

    if (escolha == 'view'): 
        view ()