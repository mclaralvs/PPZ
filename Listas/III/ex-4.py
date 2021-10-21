num = int(input('Insira um número: '))

a, b = 1, 1
cont = 1

while cont <= num-2: #n-2 pq eh a posição do número que está sendo lido
    a, b = b, a+b
    cont = cont+1
else:
    print(b)