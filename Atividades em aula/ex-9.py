soma = 0
num = 0
cont = 0
while True:
    num = int(input('Digite 0 para sair: '))
    if num == 0:
        break
    else:
        soma = soma + num
        cont = cont + 1
print(soma/cont)