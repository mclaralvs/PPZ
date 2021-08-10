print("Preço e Desconto")

print("")

preço = float (input("Insira o valor do produto: "))

print("")

percen = float (input("Insira o percentual de desconto do produto: "))

print("")

print (f"O valor do desconto é de R${preço * (percen/100): .2f} e o preço final é R${preço - (preço * (percen/100)): .2f}")
