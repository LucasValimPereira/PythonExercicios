valor = input("digite qualquer valor: ")
print("O valor do tipo é ", type(int(valor)))
print("Só tem espaços? ", valor.isspace())
print("É um número? ", valor.isnumeric())
print("É um alfabeto? ", valor.isalpha())
print("É um alfanúmerico? ", valor.isalnum())
print("Esta em maiúsculas? ", valor.isupper())
print("Esta em minúsculas? ", valor.islower())
print("Esta capitalizada? ", valor.istitle())

# valor tem caracteristica e métodos