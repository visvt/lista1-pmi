'13. Escreva um programa que calcule a idade em dias.'

idade = int (input ("Digite a idade atual: "))
if (idade > 4):
    bis = int (idade / 4)
    diasa = ((idade * 365) + bis)
else:
    diasa = (idade * 365)
diasa = int(diasa)
print (f"A idade em dias é = {diasa} dias")

