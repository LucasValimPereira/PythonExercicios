salario = float(input("Digite o salário do funcionário: "))

aumento1 = 0.10
aumento2 = 0.15
if salario <= 1250:
    aumento = salario * aumento1
    novo_salario = salario + aumento
    print("O seu novo salário é {:.2f} e o aumento foi de {:.2f}".format(novo_salario, aumento1))
else:
    aumento = salario * aumento2
    novo_salario = salario + aumento
    print("O seu novo salário é {:.2f} e o aumento foi de {:.2f}".format(novo_salario, aumento2))


