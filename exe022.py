nome = str(input("Digite seu nome completo: "))

print("Nome em maiúsculas: {}".format(nome.upper()))
print("Nome em minúsculas: {}".format(nome.lower()))
qtd = len (nome.replace(" ",""))
print("Quantidade de caracteres que possui o nome completo: {}".format(qtd))
primeiro_nome = nome.split()[0]
print("Primeiro nome tem quantidade de letras: {}".format(len(primeiro_nome)))