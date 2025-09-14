'43. Crie um programa que verifique se um número é divisível por 3 e por 5. '

num = int (input ("Digite o número: "))
if (num % 3 == 0 and num % 5 == 0):
    print (f"{num} é divisível por 3 e por 5")
else:
    print (f"{num} não é divisível por 3 e por 5")