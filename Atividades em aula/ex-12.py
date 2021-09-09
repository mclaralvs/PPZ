notas = []
cont = 0
soma = 0

while cont <= 3:
    notas.append(float(input('Nota:')))
    soma = soma + notas[cont]
    cont = cont + 1

print(f'Média: {soma/4: .2f}')