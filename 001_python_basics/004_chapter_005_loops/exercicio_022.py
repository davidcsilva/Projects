'''
Escreva um programa que exiba uma lista de opções (menu): adição,
subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
Repita até que a opção saída seja escolhida.
'''

while True:
    print("\n--- MENU DE OPÇÕES ---")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    opcao = input("Escolha uma opção (1-5): ")

    if opcao == '5':
        print("A encerrar o programa... Até breve!")
        break

    if opcao in ['1', '2', '3', '4']:
        numero = int(input("Digite o número para ver a tabuada: "))
        print(f"\n--- Tabuada do {numero} ---")

        for i in range(1, 11):
            if opcao == '1':
                print(f"{numero} + {i:2d} = {numero + i}")
            elif opcao == '2':
                print(f"{numero} - {i:2d} = {numero - i}")
            elif opcao == '3':
                print(f"{numero} x {i:2d} = {numero * i}")
            elif opcao == '4':
                print(f"{numero} / {i:2d} = {numero / i:.2f}")
    else:
        print("Opção inválida! Por favor, escolha um número de 1 a 5.")
