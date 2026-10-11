cores = {'amarelo': '\033[0;33m',
         'vermelho': '\033[0;31m',
         'cinza': '\033[0;37m',
         'limpa': '\033[0;33m'}
    
n1 = int(input(cores['amarelo'] + "Digite um numero: "))
n2 = int(input(cores['amarelo'] + "Digite outro: "))
s = n1 + n2
print("A soma entre {}{} e {}{} vale {}{}.".format(cores['vermelho'] + str(n1), cores['limpa'], cores['vermelho'] + str(n2), cores['limpa'], cores['vermelho'] + str(s), cores['limpa']))