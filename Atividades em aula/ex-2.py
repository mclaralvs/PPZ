vel = int(input("Insira sua velocidade: "))

if vel > 110:
    print(f"Você foi multado no valor de R${(vel-110)*5}.")
else:
    print("Está dentro da norma.")