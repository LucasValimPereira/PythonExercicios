frase = str(input("Digite uma frase:")).upper().strip()

qtd_a = frase.count("A")

print("A letra 'a' aparece {} vezes na frase.".format(qtd_a))

primeiro_a = frase.find("A")
print("A primeira letra 'a' aparece na posição {}.".format(primeiro_a+1))

ultimo_a = frase.rfind("A")
print("A última letra 'a' aparece na posição {}.".format(ultimo_a+1))