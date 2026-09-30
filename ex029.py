kmultrapassado = float(input('Digite a velocidade do carro (km/h): '))

if kmultrapassado > 80:
    multa = (kmultrapassado - 80) * 7
    print(f'Você foi multado! O valor da multa é R${multa:.2f}.')
else:
    print('dentro do limite de velocidade permitido.')
print('Fim do programa. ')