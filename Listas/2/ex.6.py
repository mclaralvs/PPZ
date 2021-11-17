salhora = float(input('Insira quanto você ganha por hora: '))
horasmes = int(input('Insira o número de horas trabalhadas no mês: '))

salbruto = salhora * horasmes
ir = salbruto * 0.11
inss = salbruto * 0.08
sind = salbruto * 0.05
salliquido = salbruto - (ir + inss + sind)

print('\nSegue os respectivos valores')
print(f'\nSalário bruto: R${salbruto: .2f}')
print(f'\nIR: R${ir:.2f}')
print(f'\nINSS: R${inss: .2f}')
print(f'\nSindicato: R${sind: .2f}')
print(f'\nSalário líquido: R${salliquido: .2f}')