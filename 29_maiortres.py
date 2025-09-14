'29. Crie um programa que determine o maior entre três números. '

num1 = float (input ("Digite o primeiro número: "))
num2 = float (input ("Digite o segundo número: "))
num3 = float (input ("Digite o terceiro número: "))
if (num1 > num2 and num1 > num3):
    print (f"{num1} é o maior número")
elif (num2 > num1 and num2 > num3):
    print (f"{num2} é o maior número")
else:
    print (f"{num3} é o maior número")