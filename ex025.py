nome = str(input('Digite o seu nome completo: ')).strip()

print('O seu nome tem Silva?{}'.format('silva' in nome.lower()))
print("Seu nome formatado da forma adequada: {}".format(nome.title()))