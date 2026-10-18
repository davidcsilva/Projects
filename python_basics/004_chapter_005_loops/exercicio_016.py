'''
Execute o programa (Listagem 5.14) para os seguintes valores: 501,
745, 384, 2, 7 e 1.
'''

quantidade = 0
soma = 0

while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))

    # Condição de parada: encerra o loop se o usuário digitar 0
    if numero == 0:
        break

    soma += numero
    quantidade += 1

print("\n--- RESUMO DOS DADOS ---")
if quantidade > 0:
    media = soma / quantidade
    print(f"Quantidade de números digitados: {quantidade}")
    print(f"Soma dos números:                {soma}")
    print(f"Média aritmética:                {media:.2f}")
else:
    print("Nenhum número diferente de zero foi digitado.")
