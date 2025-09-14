'12. Crie um programa que troque os valores de duas variáveis.'

x = int (input ("Insira o primeiro valor: "))
y = int (input ("Insira o segundo valor: "))
z = x
x = y 
y = z
print (f"O primeiro valor agora é {x} e o segundo valor agora é {y}")