count = 0
v = ''

for x in range(18644 - 1, 33087 + 1):
    v = str(x)
    if '2' in v:
        if '7' not in v:
            count += 1
print(count)