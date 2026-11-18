'''
Exercício 9.20 Adicione a opção de ordenar a lista por nome no menu principal.


'''

# Programa da Agenda Telefônica com opção de ordenação por nome no menu principal (Exercício 9.20)

NOME_ARQUIVO = "agenda.txt"


def carregar_agenda():
    """Lê a agenda do arquivo e retorna uma lista de contatos [nome, telefone]."""
    agenda = []
    try:
        with open(NOME_ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split("#")
                    if len(partes) == 2:
                        agenda.append([partes[0], partes[1]])
    except FileNotFoundError:
        pass
    return agenda


def salvar_agenda(agenda):
    """Grava os contatos no arquivo formatados como nome#telefone."""
    try:
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as f:
            for nome, telefone in agenda:
                f.write(f"{nome}#{telefone}\n")
        print(f"Agenda salva com sucesso em '{NOME_ARQUIVO}'.")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")


def lista(agenda):
    """Exibe os contatos com suas respectivas posições (Exercício 9.19)."""
    print("\n--- LISTA DE CONTATOS ---")
    if not agenda:
        print("A agenda está vazia.")
        return

    for posicao, contato in enumerate(agenda, start=1):
        nome, telefone = contato[0], contato[1]
        print(
            f"Posição: {posicao:<3} | Nome: {nome:<25} | Telefone: {telefone}")

    print("-" * 55)


def ordenar_por_nome(agenda):
    """Ordena a lista de contatos pelo campo nome em ordem alfabética."""
    if not agenda:
        print("A agenda está vazia. Nada para ordenar.")
        return

    # contato[0] é o nome. .lower() garante ordenação alfabética case-insensitive
    agenda.sort(key=lambda contato: contato[0].lower())
    print("Agenda ordenada por nome com sucesso!")


def adicionar_contato(agenda):
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    if nome and telefone:
        agenda.append([nome, telefone])
        salvar_agenda(agenda)
        print("Contato adicionado!")
    else:
        print("Nome e telefone não podem ser vazios.")


def menu():
    agenda = carregar_agenda()

    while True:
        total_contatos = len(agenda)
        print(
            f"\n=== AGENDA TELEFÔNICA ({total_contatos} contato(s) cadastrado(s)) ===")
        print("1 - Listar contatos")
        print("2 - Adicionar contato")
        print("3 - Ordenar por nome")
        print("4 - Salvar e Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            lista(agenda)
        elif opcao == "2":
            adicionar_contato(agenda)
        elif opcao == "3":
            ordenar_por_nome(agenda)
            salvar_agenda(agenda)
        elif opcao == "4":
            salvar_agenda(agenda)
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
