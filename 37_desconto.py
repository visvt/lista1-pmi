'37. Crie um programa que determine o desconto baseado no valor da compra. '

produto = float (input ("Insira o valor do produto: "))
if (produto >= 200 and produto < 400):
    porc = (produto * 0.10)
    desc = (produto - porc)
    print (f"O produto no valor de R$ {produto} tem um desconto de R$ {porc}, sendo assim seu valor final é de R$ {desc}")
elif (produto >= 400 and produto < 1000):
    porc = (produto * 0.20)
    desc = (produto - porc)
    print (f"O produto no valor de R$ {produto} tem um desconto de R$ {porc}, sendo assim seu valor final é de R$ {desc}")
elif (produto >= 1000):
    porc = (produto * 0.40)
    desc = (produto - porc)
    print (f"O produto no valor de R$ {produto} tem um desconto de R$ {porc}, sendo assim seu valor final é de R$ {desc}")
else:
    print (f"O produto no valor de R$ {produto} não tem desconto!")