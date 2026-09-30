pedacos = int (input("quantas fatias tem a pizza?: "))
amigos = int (input("quantos amigos tem na mesa?: "))  

fatias = pedacos // amigos
sobra = pedacos % amigos


if pedacos == amigos: 
 print ("cada amigo vai comer ", fatias, "pedaços e sobraram", sobra, "fatias")
elif pedacos > amigos:
 print ("sobraram", sobra, "fatias, , prepare-se pra briga") 

 




 
 