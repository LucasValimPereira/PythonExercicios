frase = str(input("Digite uma frase:"))

qtd_a = frase.count("a")

print("A letra 'a' aparece {} vezes na frase.".format(qtd_a))

primeiro_a = frase.find("a")
print("A primeira letra 'a' aparece na posição {}.".format(primeiro_a))

ultimo_a = frase.rfind("a")
print("A última letra 'a' aparece na posição {}.".format(ultimo_a))