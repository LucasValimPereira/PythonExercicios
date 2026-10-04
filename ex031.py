distancia = float(input('Digite a distância da viagem em km: '))

valor1 = 0.50
valor2 = 0.45
men1 = f'O valor por Km é R${valor1}.'  
men2 = f'O valor por Km é R${valor2}.' 
    
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(f'O preço da passagem é R${preco}.')
print(men1 if distancia <= 200 else men2)
print('Fim do programa.')