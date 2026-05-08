largura = input("Digite a área de largura: ")
altura = input("Digite a área da altura: ")
metrospare = float(largura)
alturapare = float(altura)
area = metrospare * alturapare
areapintar = area / 2 * 1
print("sua parede tem dimensão de {}X{} e sua área de {}m.".format(metrospare,alturapare, area))
print("Você precisara de tinta para pintar: ",areapintar)