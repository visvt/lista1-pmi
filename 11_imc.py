'11. Escreva um programa que calcule o IMC (Índice de Massa Corporal).'

print ("Seja bem vindo(a) doutor(a)")
peso = float (input ("Por favor, digite o peso do paciente: "))
altura = float (input ("Agora digite a altura do paciente: "))
imc = (peso/(altura * altura))
print (f"O IMC do paciente é: {imc:.1f}")