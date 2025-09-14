'42. Escreva um programa que determine o quadrante de um ponto no plano cartesiano. '

x = float (input ("Digite o valor de x: "))
y = float (input ("Digite o valor de y: "))
if (x > 0 and y > 0):
    print (f"O ponto {x}, {y} está localizado no primeiro quadrante.")
elif (x < 0 and y > 0):
    print (f"O ponto {x}, {y} está localizado no segundo quadrante.")
elif (x < 0 and y < 0):
    print (f"O ponto {x}, {y} está localizado no terceiro quadrante.")
elif (x > 0 and y < 0):
    print (f"O ponto {x}, {y} está localizado no quarto quadrante.")
elif (x == 0 and y == 0):
    print (f"O ponto {x} é zero.")
    