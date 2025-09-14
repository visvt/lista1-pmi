'31. Crie um programa que verifique se um ano é bissexto. '

ano = int (input ("Insira o ano: "))
if ((ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)):
    print (f"{ano} é um ano bissexto")
else:
    print (f"{ano} não é um ano bissexto")