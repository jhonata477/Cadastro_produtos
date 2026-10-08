produtos = []
nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
categoria = input("Digite a categoria do produto: ")
produto = [nome, preco, categoria]
produtos.append(produto)
valor = float(input("Digite o valor máximo para filtrar os produtos: "))
print("\nProdutos cadastrados:")
for produto in produtos:
    if produto[1] <= valor:
        print("Nome:", produto[0])
        print("Preço: R$", produto[1])
        print("Categoria:", produto[2])
        