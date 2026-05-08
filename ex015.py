dias = int(input("quantos dias alugados: "))
km = float(input("quantos quilometros rodados: "))
pagar = (dias * 60) + (km * 0.15)
print("O total a pagar é R${}".format(pagar))