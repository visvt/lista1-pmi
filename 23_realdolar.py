'23. Escreva um programa que converta uma quantia em reais para dólares.'

real = float (input ("Digite o valor a converter em reais: "))
cot = float (input ("Digite a cotação atual do dolar: "))
conv = (real / cot)
print (f"R$ {real} convertido em dólares, é igual a U$ {conv:.2f}")