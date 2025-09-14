'14. Crie um programa que calcule o desconto de um produto.'

prod = float (input ("Insira o valor do produto: "))
desc = float (input ("Insira o valor de desconto: "))
if (desc > prod):
   print (f"O valor de desconto {desc} é maior que o valor do produto {prod}, insira um valor menor!")
else:
    final = prod - desc
    print (f"O valor final com desconto é de R$ {final}")