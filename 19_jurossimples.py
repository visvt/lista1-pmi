'''19. Escreva um programa que calcule juros simples.'''

val = float (input ("Insira o valor bruto: "))
porc = float (input ("Insira a porcentagem do juros: "))
juros = ((val * porc) / 100) 
print (f"O juros de {porc} % sobre o valor de R$ {val} é de R$ {juros}")