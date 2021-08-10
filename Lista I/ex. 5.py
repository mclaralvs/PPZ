preço = float (input("Insira o valor do produto: "))

percen = float (input("Insira o percentual de desconto do produto: "))

print (f"O valor do desconto é de R${preço * (percen/100): .2f} e o preço final é R${preço - (preço * (percen/100)): .2f}")
