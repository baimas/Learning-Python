'''
Jogo para sortear um numero de 1 a 100.

'''
from random import choice

#Inputs

while True:
    numero = int(input("Escolha um número de 1 a 100: "))
    sorteio = choice(range(1,101))

#Condição
    if numero == sorteio:
        print("\nVocê venceu")
        break
    else:
        print("\nA banca sempre vence!!")