print("Cálculo de Redução de Vida de Fumante")

print("")

qntdia = int(input("Insira quantos cigarros você fuma por dia: "))

print("")

qntano = int(input("Insira há quantos anos você fuma: "))

print("")

totcig = qntano * 365 * qntdia

perd = totcig / 144

print(f"Sua vida foi reduzida em {perd: .1f} dias")
