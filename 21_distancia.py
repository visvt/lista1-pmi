'''21. Escreva um programa que calcule a distância entre dois pontos.'''

d1 = int (input ("Digite o ponto 1: "))
d2 = int (input ("Digite o ponto 2: "))
if (d1 > d2):
    distan = (d1 - d2)
    print (f"A distância é de {distan}")
else:
    distan = (d2 - d1)
    print (f"A distância é de {distan}")