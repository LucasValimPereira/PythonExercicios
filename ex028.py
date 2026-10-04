 
from time import sleep
import random

adivinha = random.randint(0, 5)

print('=== Jogo de adivinhar o número ===')
print('Tente adivinhar o número que estou pensando entre 0 e 5!')

tentativa = int(input('Qual é o número que estou pensando? '))
print('PROCESSANDO...')
sleep(2)

if tentativa == adivinha:
    print('Parabéns! Você acertou!')
else:
    print(f'Que pena! Eu estava pensando no número {adivinha}.')