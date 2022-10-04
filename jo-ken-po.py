print(f'{"=":=^25}')
print("Vamos jogar jo ken pô?")
print(f'{"=":=^25}')
from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
print ("""Escolha uma opção:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")
computador = randint (0, 2)
jogador = int(input("Qual a sua jogada? "))
print ("JÔ")
sleep (1)
print ("KEN")
sleep (1)
print ("PÔ")
sleep (1)
print ("Computador jogou {}" .format(itens[computador]))
print ("Jogador jogou {}" .format(itens[jogador]))
print ("-"*10)
if computador == 0:
    if jogador == 0:
        print ("Empate!")
    if jogador == 1:
        print ("O jogador ganhou!")
    if jogador == 2:
        print ("O computador venceu!")
elif computador == 1:
    if jogador == 0:
        print ("Jogador perdeu!")
    if jogador == 1:
        print ("Empate!")
    if jogador == 2:
        print ("Jogador Venceu!")
elif computador == 2:
    if jogador == 0:
        print ("Jogador venceu!")
    if jogador == 1:
        print ("Computador venceu!")
    if jogador == 2:
        print ("Empate!")
print(f'{"=":=^25}')