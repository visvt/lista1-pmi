'35. Crie um programa que determine o tipo de triângulo. '

lado1 = float (input ("Digite o tamanho do primeiro lado: "))
lado2 = float (input ("Digite o tamanho do segundo lado: "))
lado3 = float (input ("Digite o tamanho do terceiro lado: "))
if (lado1 == lado2 and lado2 == lado3 and lado1 == lado3):
    print ("É um triângulo equilatero")
elif (lado1 == lado2 or lado2 == lado3 or lado3 == lado1):
    print ("É um triângulo isóceles")
else:
    print ("É um triângulo escaleno")