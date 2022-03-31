'''
Jogo de dados com 2 pessoas, onde o programa solicitara os nomes
sorteará o número, quem tirar o maior número de 1 a 6 é o campeão da Rodada
serão 3 rodas
'''

from random import choice
from time import sleep

print("Bem vindo ao jogo do dados!!, em nosso jogo ganha quem tiver o maior número da rodada :) \n")

player1 = input("Insira o nome do Jogador(a) 1: ")
player2 = input("Insira o nome do Jogador(a) 2: ")
print("\nVamos começar a brincadeira !! ")
sleep(2) #Esperando 2 segundos

#Variáveis
contador = 1
rodada_play1 = 0
rodada_play2 = 0

#Processamento do Jogo
while contador <=3:
    print(f"\n************ RODADA {contador} ************")
    print(f"\nJogando o dado para {player1} !!")
    sleep(5)
    num_player1 = choice(range(1,7))
    print(f"O número sorteado para {player1}, foi: {num_player1}")

    print(f"\nJogando o dado para {player2} !!")
    sleep(5)
    num_player2 = choice(range(1,7))
    print(f"O número sorteado para {player2}, foi: {num_player2}")

    if num_player1 > num_player2:
        print(f"\nParabéns o ganhador da rodada foi {player1}")
        rodada_play1 += 1
        contador +=1
    
    elif num_player1 < num_player2:
        print(f"\nParabéns o ganhador da rodada foi {player2}")
        rodada_play2 += 1
        contador +=1

    else:
        print(f"\nO numeros foram iguais portanto a rodada não foi valida, vamos novamente!!")
        if contador == 1:
            contador = 1
        else:
            continue

#Definindo o Campeão de 3 Rodadas Válidas
if rodada_play1 > rodada_play2:
    print(f"\n\nO maior pontuador de 3 rodadas válidas foi {player1}!!")
else:
    print(f"\n\nO maior pontuador de 3 rodadas válidas foi {player2}!!")

    
    

    

