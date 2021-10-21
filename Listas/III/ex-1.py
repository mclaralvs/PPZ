nota = float(input('Insira uma nota entre 0 e 10: '))

while nota>10 or nota<0:
    nota = float(input('Valor inválido! Insira novamente: '))
else:
    print(f'Valor válido! Nota: {nota: .2f}')