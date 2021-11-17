from random import sample

num = sample(range(100), 10)

count = 1
min = num[0]
max = num[0]

while count < 10:
    if num[count] < min:
        min = num[count]
        
    if num[count] > max:
        max = num[count]
        
    count = count + 1

print(f'Vetor: {num}\nMáximo: {max}\nMínimo: {min}')