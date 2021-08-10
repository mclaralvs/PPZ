kmp = int(input("Insira a quantidade de quilômetros percorridos: "))

d = int(input("Insira a quantidade de dias de aluguel do carro: "))

print(f"O valor a ser pago é de R${(d*60) + (0.15*kmp): .2f}")
