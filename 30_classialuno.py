'30. Escreva um programa que classifique a nota de um aluno. '

nota = float (input ("Digite a nota do aluno: "))
if (nota >= 7):
    print ("Aluno aprovado")
elif (nota >= 5 and nota < 6.9):
    print ("Aluno de recuperação")
else:
    print ("Aluno reprovado")