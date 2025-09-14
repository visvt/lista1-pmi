'47. Crie um programa que simule um jogo de adivinhação. '

num = 77
resp = int (input ("Insira o número secreto: "))
while (resp != num):
    if (resp < num):
        print ("O número secreto é maior!")
    else:
        print ("O número secreto é menor!")
    resp = int (input ("Tente mais uma vez: "))
print ("Parabéns, você acertou!")