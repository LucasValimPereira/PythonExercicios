distancia = float(input('Digite a distância da viagem em km: '))

valor1 = 0.50
valor2 = 0.45
if distancia <= 200:
    preco = distancia * valor1
    men1 = f'O valor por Km é R${valor1}.'
    
else:
    preco = distancia * valor2
    men2 = f'O valor por Km é R${valor2}.'

print(f'O preço da passagem é R${preco}.')
print(men1 if distancia <= 200 else men2)
print('Fim do programa.')