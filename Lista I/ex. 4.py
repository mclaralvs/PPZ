print("Reajuste Salarial")

print("")

sal = float(input("Insira o valor do seu salário: "))

print("")

porcen = float(input("Insira a porcentagem de aumento: "))

print("")

porcen = 1 + (porcen / 100)

print(f"O valor do salário após o aumento salarial é igual à R${sal * porcen: .2f}")
