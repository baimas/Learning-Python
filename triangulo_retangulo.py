'''
Pedir ao usuário 3 Seguimentos de reta e verificar se eles podem virar um Triangulo Retangulo
'''

def forma_triangulo(hipotenusa, cateto1, cateto2):
    if (hipotenusa**2) == (cateto1**2) + (cateto2**2):
        return print ("\nOs lados fornecidos formam um triangulo retangulo")
    else:
        return print ("\nOs lados fornecidos não formam um triangulo retangulo")

#Entrada
lado = []
for i in range(1,4):
    print(f"Informe o lado {i} do Triangulo")
    triangulo = float(input())
    lado.append(triangulo)

#Processamento

todos_lados = lado.sort(reverse=True)
hipotenusa = lado[0]
cateto1 = lado[1]
cateto2 = lado[2]

print (f"\nLados do Triangulo, Hipotenusa {hipotenusa}, 1º Cateto {cateto1}, 2º Cateto {cateto2}")

forma_triangulo(hipotenusa,cateto1,cateto2)
