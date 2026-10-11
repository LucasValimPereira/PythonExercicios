cores = {'amarelo': '\033[0;33m',
         'negrito': '\033[1;33m',
         'limpa': '\033[0;33m'}
nome = input(cores['amarelo'] + "digite seu nome: ")

print("Prazer em te conhercer, {}{}{}!".format(cores['amarelo'], cores['negrito'] + nome, cores['limpa']))