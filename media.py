nota1 = float (input("Primeira nota do aluno: "))
nota2 = float (input("Segunda nota do aluno: "))
nota3 = float (input("Terceira nota nota do aluno: "))
media = (nota1 + nota2 + nota3) / 3

if media >= 6.0:
    print (f"Aprovado {media :.2f}")
else:
    print (f"Reprovado {media :.2f}")