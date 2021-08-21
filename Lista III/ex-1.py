nota = int(input('Insira uma nota entre 0 e 10: '))

while nota>=10 or nota<=0:
    nota = int(input('Valor inválido! Insira novamene: '))

print(f'Valor válido! Nota: {nota}')