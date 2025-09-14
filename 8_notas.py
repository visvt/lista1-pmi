'8. Crie um programa que calcule a média de três notas.'

print ("Seja bem-vindo professor(a)!")
nome = str (input ("Digite o nome do aluno: "))
n1 = float (input ("Digite a primeira nota: "))
n2 = float (input ("Digite a segunda nota: "))
n3 = float (input ("Digite a terceira nota: "))
final = ((n1 + n2 + n3) / 3)
print (f"A média final de {nome} é de {final}")