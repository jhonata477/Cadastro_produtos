
produtos = [
    ["Arroz", 25.90, "Alimentos"],
    ["Sabonete", 3.50, "Higiene"],
    ["Feijão", 8.00, "Alimentos"],
    ["Detergente", 4.75, "Limpeza"]
]

precos = [produto[1] for produto in produtos]
categorias = set(produto[2] for produto in produtos)

menor = min(precos)
maior = max(precos)
media = sum(precos) / len(precos)

crescente = sorted(produtos, key=lambda produto: produto[1])
decrescente = sorted(produtos, key=lambda produto: produto[1], reverse=True)

print("=" * 40)
print("         RELATÓRIO DE PRODUTOS")
print("=" * 40)

print("\nPRODUTOS CADASTRADOS:")
for nome, preco, categoria in produtos:
    print(f"Produto: {nome:<15} | Preço: R$ {preco:7.2f} | Categoria: {categoria}")

print("\nCATEGORIAS ÚNICAS:")
print(f"{', '.join(sorted(categorias))}")

print("\nPREÇOS EM ORDEM CRESCENTE:")
for nome, preco, categoria in crescente:
    print(f"{nome}: R$ {preco:.2f}")

print("\nPREÇOS EM ORDEM DECRESCENTE:")
for nome, preco, categoria in decrescente:
    print(f"{nome}: R$ {preco:.2f}")

print("\nESTATÍSTICAS:")
print(f"Menor preço: R$ {menor:.2f}")
print(f"Maior preço: R$ {maior:.2f}")
print(f"Média dos preços: R$ {media:.2f}")

print("\n" + "=" * 40)
print("           FIM DO RELATÓRIO")
print("=" * 40)
