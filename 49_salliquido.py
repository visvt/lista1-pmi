'49. Crie um programa que calcule o salário líquido com base no salário bruto. '

bruto = float (input ("Digite o salário bruto: "))
vt = (bruto * 0.06)
va = (bruto * 0.2)
desc = (va + vt)
liqui = bruto - desc
print (f"O salário líquido é de {liqui:.2f}")