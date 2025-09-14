'50. Escreva um programa que verifique se três lados podem formar um triângulo e classifique-o.'

lado1 = float (input ("Digite o tamanho do primeiro lado: "))
lado2 = float (input ("Digite o tamanho do segundo lado: "))
lado3 = float (input ("Digite o tamanho do terceiro lado: "))
if ((lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)):
    if (lado1 == lado2 and lado2 == lado3 and lado1 == lado3):
        print ("É um triângulo equilatero")
    elif (lado1 == lado2 or lado2 == lado3 or lado3 == lado1):
        print ("É um triângulo isóceles")
    else:
        print ("É um triângulo escaleno")
else:
    print ("Os lados não formam um triângulo")