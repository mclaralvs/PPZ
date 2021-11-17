a = 80000
b = 200000
x = 0

while b>a:
    a = a * 1.03
    b = b * 1.015
    x = x  + 1

print(f'São necessários {x} anos até que a população do país A ultrapasse ou iguale-se a população do país B.')