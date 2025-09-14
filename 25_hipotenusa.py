'25. Escreva um programa que calcule a hipotenusa de um triângulo retângulo.'

cat1 = float (input ("Insira o valor do primeiro cateto: "))
cat2 = float (input ("Insira o valor do segundo cateto: "))
hip = ((cat1 ** 2) + (cat2 ** 2))
hip = (hip ** 0.5)
print (f"A hipotenusa do triângulo retângulo é {hip:.1f}")