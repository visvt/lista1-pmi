'38. Escreva um programa que verifique se um caractere é vogal ou consoante.'

palavra = str (input ("Escreva uma palavra: "))
carac = int (input ("Agora digite o número do caracterece que deseja conferir (começando por 0): "))
if (palavra[carac] == "a" or palavra[carac] == "e" or palavra[carac] == "i" or palavra[carac] == "o" or palavra[carac] == "u"):
    print ("É uma vogal")
else:
    print ("É uma consoante")
