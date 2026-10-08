produtos = []

for i in range(3):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: R$ "))
    categoria = input("Digite a categoria: ")

    produto = [nome, preco, categoria]
    produtos.append(produto)


produtos.sort(key=lambda produto: produto[1])

print("\nProdutos por preço crescente:")
for produto in produtos:
    print(produto[0], "- R$", produto[1], "-", produto[2])

produtos_decrescente = sorted(produtos, key=lambda produto: produto[1], reverse=True)

print("\nProdutos por preço decrescente:")
for produto in produtos_decrescente:
    print(produto[0], "- R$", produto[1], "-", produto[2])