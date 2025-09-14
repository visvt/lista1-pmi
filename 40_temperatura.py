'40. Escreva um programa que classifique a temperatura.'

temp = int (input ("Insira a temperatura: "))
if (temp > 30):
    print (f"{temp}° é calor")
elif (temp >= 20 and temp < 30):
    print (f"{temp}° é ameno")
else:
    print (f"{temp}° é frio")