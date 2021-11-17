peso = float(input('Insira o peso do peixe em Kg: '))

if peso > 50 :
    exc = peso - 50
    multa = exc * 4
    print(f'Há um excesso de {exc: .1f} Kg e há uma multa de R${multa: .2f}')
else:
    exc = 0
    multa = 0
    print(f'Excesso: {exc: .1f} Kg \nMulta: R${multa: .2f}')