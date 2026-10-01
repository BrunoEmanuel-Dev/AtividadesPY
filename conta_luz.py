horas_impressao = int (input("Quantas horas durou a impressao: "))
preco_kw = float (input("quanto custa o kwh: "))
custo_da_imprecao = 0.35 * horas_impressao
kw = custo_da_imprecao * preco_kw
print (f"Custo da impressao: R$ {kw:.2f}")