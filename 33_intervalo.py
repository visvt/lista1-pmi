'33. Crie um programa que verifique se um número está em um intervalo. '

num1 = float (input ("Digite o primeiro número do intervalo: "))
num2 = float (input ("Digite o segundo número do intervalo: "))
inter = float (input ("Digite o número a verificar se esta no intervalo: "))
if ((inter >= num1 and inter <=num2) or (inter >= num2 and inter <= num1)):
    print (f"O número {inter} está no intervalo informado")
else:
    print (f"O número {inter} não está no intervalo informado")