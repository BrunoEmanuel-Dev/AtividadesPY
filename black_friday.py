valor_compra = float (input("Qual o valor da compra: "))
desconto = (valor_compra * 0.15) 
preco_final = valor_compra - desconto
if valor_compra > 100:
 print (f"valor final é R${preco_final:.2f} (economia de R$ {desconto:.2f})") 
else:
 print ("sem desconto")