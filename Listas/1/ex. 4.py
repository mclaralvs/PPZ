sal = float(input("Insira o valor do seu salário: "))

porcen = float(input("Insira a porcentagem de aumento: "))

porcen = 1 + (porcen / 100)

print(f"O valor do salário após o aumento salarial é igual à R${sal * porcen: .2f}")
