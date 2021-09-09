def fat(n):
    k = 1
    fat = 1
    while k <= n:
        fat = fat * k
        k = k + 1
    return fat