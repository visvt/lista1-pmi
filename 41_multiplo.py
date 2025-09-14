'41. Crie um programa que verifique se um número é múltiplo de outro. '

num1 = int (input ("Insira o primeiro número: "))
num2 = int (input ("Insira o múltiplo: "))
if (num1 % num2 == 0):
    print (f"{num1} é múltiplo de {num2}")
else:
    print (f"{num1} não é múltiplo de {num2}")