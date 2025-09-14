'32. Escreva um programa que calcule o IMC e classifique o resultado. '

print ("Seja bem vindo(a) doutor(a)")
peso = float (input ("Por favor, digite o peso do paciente: "))
altura = float (input ("Agora digite a altura do paciente: "))
imc = (peso/(altura * altura))
if (imc >= 40):
    print ("Obesidade grave")
elif (imc >= 30 and imc < 40):
    print ("Obesidade")
elif (imc >= 25 and imc < 30):
    print ("Sobrepeso")
elif (imc >= 18.5 and imc < 25):
    print ("Normal")
else:
    print ("Magreza")