area = float(input('Indique o tamanho, em metros quadrados, da área a ser pintada: '))

cobertura = area / 3
lata = 18
preçolata = 80

if cobertura <= lata:
    print(f'A quantidade de latas de tinta a serem compradas é igual à 1 e o preço total é R${preçolata}')
else:
    qntlata = cobertura / lata
    preçotot = round(qntlata+0.5) * preçolata
    print(f'\nA quantidade de latas de tinta a serem compradas é igual à {round(qntlata+0.5)} e o preço total é R${preçotot}')