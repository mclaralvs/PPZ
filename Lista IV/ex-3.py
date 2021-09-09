from random import sample

a = sample(range(100), 10)
b = sample(range(100), 10)

c = []
k = count = 0

while k < 2: 
    while count < 10:
        c.append(a[count])
        c.append(b[count]) 
        count = count + 1
    k = k + 1

print(f'A: {a}\nB: {b}\nC: {c}')