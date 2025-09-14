'16. Crie um programa que converta segundos em horas, minutos e segundos.'

seg = int (input ("Insira a quantidade de segundos que você quer converter: "))
hrs = (seg // 3600)
rseg = (seg % 3600)
min = (rseg // 60)
segfim = (rseg % 60)
print (f"{seg} segundos é igual a: {hrs} horas, {min} minutos e {segfim} segundos.")