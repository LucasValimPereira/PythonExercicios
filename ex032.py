import datetime
ano_bissexto = int(input("Que ano quer analisar? Coloque 0 para verificar o ano atual: "))
if ano_bissexto == 0:
    ano_bissexto = datetime.datetime.now().year

if ( ano_bissexto % 4 == 0 and ano_bissexto % 100 != 0) or (ano_bissexto % 400 == 0):
    print(f'O ano {ano_bissexto} é bissexto.')
else:
    print(f'O ano {ano_bissexto} não é bissexto.')
print("Fim do programa.")