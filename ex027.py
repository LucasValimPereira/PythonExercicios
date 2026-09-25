nome_completo = str(input('Digite seu nome completo: '))

print("Nome Completo : {}".format(nome_completo))
primeiro_nome = nome_completo.split()[0]
print("Primeiro Nome : {}".format(primeiro_nome))
ultimo_nome = nome_completo.split()[-1]
print("Último Nome : {}".format(ultimo_nome))