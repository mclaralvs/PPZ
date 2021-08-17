num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))
num3 = float(input('Insira o terceiro número: '))

if num1 >= num2 and num1 >= num3:
    print(f'O maior número é {num1}.')
elif num2 >= num3:
    print(f'O maior número é {num2}')
else:
    print(f'O maior número é {num3}')