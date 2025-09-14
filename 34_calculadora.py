'34. Escreva um programa que simule uma calculadora simples'

opera = str (input ("Digite a operação que gostaria de fazer conforme indicado abaixo: \n Soma = +, Subtração = -, Divisão = /, Multiplicação = *: "))
if (opera == "+"):
    num1 = float (input ("Digite o primeiro número: "))
    num2 = float (input ("Digite o segundo número: "))
    calc = num1 + num2
    print (f"{num1} + {num2} = {calc}")
elif (opera == "-"):
    num1 = float (input ("Digite o primeiro número: "))
    num2 = float (input ("Digite o segundo número: "))
    calc = num1 - num2
    print (f"{num1} - {num2} = {calc}")
elif (opera == "/"):
    num1 = float (input ("Digite o primeiro número: "))
    num2 = float (input ("Digite o segundo número: "))
    calc = num1 / num2
    print (f"{num1} / {num2} = {calc}")
elif (opera == "*"):
    num1 = float (input ("Digite o primeiro número: "))
    num2 = float (input ("Digite o segundo número: "))
    calc = num1 * num2
    print (f"{num1} * {num2} = {calc}")
else:
    print ("Operação inválida")