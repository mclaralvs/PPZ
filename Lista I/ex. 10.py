qntdia = int(input("Insira quantos cigarros você fuma por dia: "))

qntano = int(input("Insira há quantos anos você fuma: "))

totcig = qntano * 365 * qntdia

perd = totcig / 144

print(f"Sua vida foi reduzida em {perd: .1f} dias")
