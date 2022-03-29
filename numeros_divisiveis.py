'''
Escrever todos os números de um range de (1000 a 5000), divisiveis por 5 e 3 ao mesmo tempo
Imprima a quantidade de números que satisfaça essa condição
'''

numeros = range(1000, 5001)

for i in numeros:
    if i % 5 == 0 and i % 3 == 0:
        print(f"{i} ," , end='')
