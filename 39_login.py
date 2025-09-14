'39. Crie um programa que simule um sistema de login. '

print ("Bem vindo(a), vamos criar seu cadastro")
user1 = str (input ("Digite o nome de usuário: "))
senha1 = str (input ("Digite uma senha: "))
print ("Cadastro criado, faça login agora na sua conta:")
user2 = str (input ("Digite o seu nome de usuário: "))
senha2 = str (input ("Digite a sua senha: "))
if (user1 == user2 and senha1 == senha2):
    print (f"Seja bem vindo(a), {user1}")
else:
    print ("Usuário ou senha inválido, verifique novamente")