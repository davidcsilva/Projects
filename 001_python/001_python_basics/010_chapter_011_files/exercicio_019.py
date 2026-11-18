'''
Exercício 9.19 Altere a função lista para que exiba também a posição de cada
elemento.

'''


def lista(agenda):
    print("\n--- LISTA DE CONTATOS ---")
    if not agenda:
        print("A agenda está vazia.")
        return

    # Usamos enumerate() começando em 1 (ou 0, dependendo da preferência)
    # para exibir a posição de cada contato na lista
    for posicao, contato in enumerate(agenda, start=1):
        nome, telefone = contato[0], contato[1]
        print(
            f"Posição: {posicao:<3} | Nome: {nome:<25} | Telefone: {telefone}")

    print("-" * 55)
