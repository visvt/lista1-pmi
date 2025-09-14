'48. Escreva um programa que determine o maior e menor entre três números.'

num1 = float (input ("Digite o primeiro número: "))
num2 = float (input ("Digite o segundo número: "))
num3 = float (input ("Digite o terceiro número: "))
if (num1 > num2 and num1 > num3):
    maior = num1
elif (num2 > num1 and num2 > num3):
    maior = num2
else:
    maior = num3
if (num1 < num2 and num1 < num3):
    menor = num1
elif (num2 < num1 and num2 < num3):
    menor = num2
else:
    menor = num3
print (f"O maior número é {maior} e o menor é {menor}")