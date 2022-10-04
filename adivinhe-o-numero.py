from random import randint
computador = randint (0,10)
print ("Adivinhe que numero pensei:")
acertou = False
palpites = 0
while not acertou:
	jogador = int(input("Qual seu palpite? "))
	palpites += 1
	if jogador == computador:
		acertou = True
	else:
		if jogador < computador:
			print("Mais!")
		elif jogador > computador:
			print ("Menos!")
print ("Você acertou com {} palpites!" .format(palpites))