'45. Crie um programa que verifique se uma data é válida (formato simples).'

dia = int (input ("Digite o dia: "))
mes = int (input ("Digite o mês: "))
ano = int (input ("Digite o ano: "))
if ((dia >= 1 and dia <= 31) and (mes >= 1 and mes <= 12) and (ano <= 2025)):
    print (f"{dia}/{mes}/{ano} é uma data válida.")
else:
    print (f"{dia}/{mes}/{ano} é uma data inválida.")