from random import sample

num = sample(range(100), 20)

par = []
impar = []
count = 0

while count < 20:
    if num[count] % 2 == 0:
        par.append(num[count])
    else:
        impar.append(num[count])
    count = count + 1

print(f'Vetor: {num}\nPares: {par}\nÍmpares: {impar}')