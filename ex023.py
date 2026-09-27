digito = int(input("Digite um número: "))
u = digito // 1 % 10
d = digito // 10 % 10
c = digito // 100 % 10
m = digito // 1000 % 10
print(f"Analisando o número {digito}")


print(f"Unidade: {u}")
print(f"Dezena: {d}") 
print(f"Centena: {c}")
print(f"Milhar: {m}")


