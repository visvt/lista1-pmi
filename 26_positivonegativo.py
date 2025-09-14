"26. Escreva um programa que verifique se um número é positivo ou negativo. "

num = int (input ("Insira o número: "))
if (num > 0):
    print(f"O número {num} é positivo")
elif (num == 0):
    print (f"O número é zero.")
else:
    print (f"O número {num} é negativo")