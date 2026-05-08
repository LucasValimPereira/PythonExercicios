import math
cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = (math.hypot(cateto_oposto, cateto_adjacente))
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

# hi = (co ** 2 + ca ** 2) ** (1/2