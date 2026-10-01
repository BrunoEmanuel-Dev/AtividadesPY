peso_aluno = float (input("Qual o peso do aluno: "))
peso_mochila = float (input("Qual o peso da mochila: "))
recomendacao = (0.10 * peso_aluno)
porcentagem = (peso_mochila / peso_aluno) *100

if peso_mochila > recomendacao:
    print(f"pesada demais {porcentagem} % do seu peso")
else:
    print ("tranquilo")