'''
Altere o programa abaixo de forma a solicitar ao usuário o
produto e a quantidade vendida. Verifique se o nome do produto digitado existe
no dicionário, e só então efetue a baixa em estoque.

estoque={ "tomate": [ 1000, 2.30],
			"alface": [ 500, 0.45],
			"batata": [ 2001, 1.20],
			"feijão": [ 100, 1.50] }
venda = [ ["tomate", 5], ["batata", 10], ["alface",5] ]
total = 0
print("Vendas:\n")
for operação in venda:
produto, quantidade = operação ❶
preço = estoque[produto][1] ❷
custo = preço * quantidade
print("%12s: %3d x %6.2f = %6.2f" %
		(produto, quantidade,preço,custo))
estoque[produto][0] -= quantidade ❸
total+=custo
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items(): ❹
print("Descrição: ", chave)
print("Quantidade: ", dados[0])
print("Preço: %6.2f\n" % dados[1])

'''

estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50],
}

total = 0

print("--- REGISTRO DE VENDAS ---")
print("Digite 'fim' no nome do produto para encerrar as vendas.\n")

while True:
    produto = input("Nome do produto: ").strip().lower()

    if produto == "fim":
        break

    # Verificação 1: Se o produto existe no dicionário de estoque
    if produto in estoque:
        quantidade = int(input(f"Quantidade de '{produto}' vendida: "))

        # Verificação 2: Se há quantidade suficiente em estoque
        if quantidade <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = preco * quantidade

            # Atualização do estoque e do total
            estoque[produto][0] -= quantidade
            total += custo

            print(
                f"-> Venda realizada: {produto} x {quantidade} = R$ {custo:.2f}\n"
            )
        else:
            print(
                f"-> Estoque insuficiente! Disponível: {estoque[produto][0]}\n"
            )
    else:
        print(f"-> Produto '{produto}' não encontrado no estoque!\n")

print("\n" + "=" * 40)
print(f"Custo total das vendas: R$ {total:21.2f}")
print("=" * 40)

print("\n--- ESTOQUE ATUALIZADO ---\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade:", dados[0])
    print("Preço:      %6.2f\n" % dados[1])
