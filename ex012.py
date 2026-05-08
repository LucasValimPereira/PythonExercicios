preco = float(input("Digite o preço de um produto: "))
novo = preco - (preco * 5 / 100)
print("O produto que custava {}, na promoção com desconto de 5% vai custar R${}.".format(preco, novo))
