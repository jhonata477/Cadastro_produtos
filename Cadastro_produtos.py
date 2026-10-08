nome = str(input("Digite o nome do produto: "))
preco = float(input("Digite o preço do produto: "))
categoria = str(input("Digite a categoria do produto: "))
produto = [nome, preco, categoria]
print("\nProduto cadastrado:")
print("Nome:", produto[0])
print("Preço: R$", produto[1])
print("Categoria:", produto[2])