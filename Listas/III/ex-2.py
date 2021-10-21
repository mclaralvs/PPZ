user = str(input('Insira seu nome de usuário: '))
senha = str(input('Insira sua senha: '))

while user == senha:
    print('Usuário e/ou senha inválidos. Insira seus dados novamente.')
    user = str(input('Nome de usuário: '))
    senha = str(input('Senha: '))

print('Usuário e senha corretos! Pode entrar!')