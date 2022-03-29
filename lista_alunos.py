'''
Programa para solicitar cinco nomes de alunos e suas respectivas notas e imprimir a média do grupo.
Usar uma lista para armazenar os nomes e outra para guardar as notas dos estudantes. 
'''

alunos = []
notas = []


interador = 1

while(interador <= 2):
     nome = input(f"Insira o nome do aluno {interador}: ")
     nota = float(input(f"Insira a nota do aluno(a) {nome}: "))
     alunos.append(nome)
     notas.append(nota)
     interador += 1

media = (sum(notas)/5)

print(f"Esse são os nomes dos alunos: {alunos}")
print(f"\nMedia do grupo: {media}")

#Update do Exercicio proposto
print(f"As notas em ordem Crescente são {sorted(notas)}")

