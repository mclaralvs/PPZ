x = int(input('Insira um número: '))
y = int(input('Insira outro número: '))

r = 0
if x >= y:
    if x % y == 0:
            print(f'MDC: {y}')
    else:
        while x % y != 0:
            x, y = y, x % y

        print(f'MDC: {y}')
else:
    if y % x == 0:
            print(f'MDC: {x}')
    else:
        while y % x != 0:
            y, x = x, y % x

        print(f'MDC: {x}')