salario = float(input("Digite o salário do funcionário: "))

aumento1 = 10
aumento2 = 15

novo_salario = salario + (salario * aumento2 / 100) if salario <= 1250 else salario + (salario * aumento1 / 100)
aumento1 if salario <= 1250 else aumento2
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo_salario))
print(f'O bonus foi de {aumento1}%.' if salario <= 1250 else f'O bonus foi de {aumento2}%.')
