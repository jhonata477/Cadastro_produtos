
precos = [15.50, 8.00, 32.90, 12.50, 20.00]

menor = min(precos)
maior = max(precos)
media = sum(precos) / len(precos)

estatisticas = (menor, maior, media)

print("Estatísticas dos preços:")
print("Menor preço: R$", estatisticas[0])
print("Maior preço: R$", estatisticas[1])
print("Média dos preços: R$", round(estatisticas[2], 2))
