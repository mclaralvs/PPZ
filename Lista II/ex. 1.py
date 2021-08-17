lado1 = float(input('Indique o primeiro lado do triângulo: '))
lado2 = float(input('Indique o segundo lado do triângulo: '))
lado3 = float(input('Indique o terceiro lado do triângulo: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print('Esse triângulo é equilátero.')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('Esse trângulo é isósceles.')
    else:
        print('Esse triângulo é escaleno.')
else:
    print('Não é um triângulo.')