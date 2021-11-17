count = 0
for x in range(1067, 3627 + 1):
    if x % 2 == 0:
        if x % 7 == 0:
            count = count + 1
print(count)