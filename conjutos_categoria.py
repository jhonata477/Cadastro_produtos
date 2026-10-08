produtos = []


for i in range(3):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: R$ "))
    categoria = input("Digite a categoria: ")

    produto = [nome, preco, categoria]
    produtos.append(produto)
categorias = set()

for produto in produtos:
    categorias.add(produto[2])

print("\nCategorias únicas:")
print(categorias)