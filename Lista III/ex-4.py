num = int(input('Insira um número: '))

x, y = 1, 1
cont = 1

while cont <= num - 2:
    x, y = y, x + y
    cont = cont + 1   
print(y) 