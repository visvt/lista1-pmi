'44. Escreva um programa que determine o preço da passagem baseado na idade.'

idade = int (input ("Digite a idade do passageiro: "))
if (idade > 60):
    print (f"{idade} anos não paga passagem")
elif (idade >= 18 and idade < 60):
    print (f"{idade} anos deve pagar R$ 5,00")
elif (idade >= 8 and idade < 18):
    print (f"{idade} anos paga meia passagem, R$ 2,50")
else:
    print (f"{idade} anos pode entrar como acompanhante e não paga passagem")