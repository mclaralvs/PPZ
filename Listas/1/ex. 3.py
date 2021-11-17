d = int(input("Insira a quantidade de dias: "))

h = int(input("Insira a quantidade de horas: "))

m = int(input("Insira a quantidade de minutos: "))

s = int(input("Insira a quantidade de segundos: "))

print(f"O total convertido em segundos é igual à {d*24*60*60 + h*60*60 + m*60 + s}")
