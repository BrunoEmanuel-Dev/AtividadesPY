megabyte = float (input("Qual o tamanho do arquivo? "))
net = float (input("Qual a velocidade da internet? "))
megabitis = megabyte * 8
tempo = megabitis // net
print("O download terminará em " , tempo, "segundos")
