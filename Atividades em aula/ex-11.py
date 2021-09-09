notas = [3, 7, 8, 10]

cont = 0
soma = 0

while cont <= len(notas)-1:
    soma = soma + notas[cont]
    cont = cont + 1

print(f'Média: {soma/len(notas): .2f}')