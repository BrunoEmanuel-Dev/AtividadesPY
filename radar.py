velo_max= float(input("Qual a velocidade máxima da via? "))
velocidade=float(input("Qual velocidade registrada pelo radar? "))
conta= velocidade - velo_max
if velocidade> velo_max:
    print(f"Você excedeu o limite por {conta} km/h e recebeu uma multa de R$130,16")
else:
    print("Boa viagem, motorista!")