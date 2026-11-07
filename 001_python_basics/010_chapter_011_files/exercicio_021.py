'''
Exercício 9.21 Nas funções de altera e apaga, peça que o usuário confirme a alte-
ração e exclusão do nome antes de realizar a operação em si.

'''

# Programa da Agenda Telefônica com confirmação para alterar e apagar (Exercício 9.21)

NOME_ARQUIVO = "agenda.txt"


def carregar_agenda():
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
    try:
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as f:
            for nome, telefone in agenda:
                f.write(f"{nome}#{telefone}\n")
        print(f"Agenda salva com sucesso em '{NOME_ARQUIVO}'.")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")


def lista(agenda):
    print("\n--- LISTA DE CONTATOS ---")
    if not agenda:
        print("A agenda está vazia.")
        return

    for posicao, contato in enumerate(agenda, start=1):
        nome, telefone = contato[0], contato[1]
        print(
            f"Posição: {posicao:<3} | Nome: {nome:<25} | Telefone: {telefone}")

    print("-" * 55)


def pesquisa(agenda, nome_pesquisado):
    nome_pesquisado = nome_pesquisado.lower()
    for indice, contato in enumerate(agenda):
        if contato[0].lower() == nome_pesquisado:
            return indice
    return None


def novo(agenda):
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    if nome and telefone:
        agenda.append([nome, telefone])
        salvar_agenda(agenda)
        print("Contato adicionado com sucesso!")
    else:
        print("Nome e telefone não podem ser vazios.")


def apaga(agenda):
    nome = input("Nome do contato a apagar: ").strip()
    indice = pesquisa(agenda, nome)

    if indice is not None:
        contato = agenda[indice]
        confirmacao = input(
            f"Tem certeza que deseja apagar o contato '{contato[0]}' (Telefone: {contato[1]})? (S/N): "
        ).strip().upper()
        if confirmacao == "S":
            del agenda[indice]
            salvar_agenda(agenda)
            print(f"Contato '{contato[0]}' apagado com sucesso!")
        else:
            print("Operação de exclusão cancelada.")
    else:
        print(f"Contato '{nome}' não encontrado.")


def altera(agenda):
    nome = input("Nome do contato a alterar: ").strip()
    indice = pesquisa(agenda, nome)

    if indice is not None:
        contato = agenda[indice]
        print(f"Dados atuais -> Nome: {contato[0]} | Telefone: {contato[1]}")

        novo_nome = input(
            f"Novo nome (pressione Enter para manter '{contato[0]}'): ").strip()
        novo_telefone = input(
            f"Novo telefone (pressione Enter para manter '{contato[1]}'): ").strip()

        nome_final = novo_nome if novo_nome else contato[0]
        telefone_final = novo_telefone if novo_telefone else contato[1]

        confirmacao = input(
            f"Confirma alterar '{contato[0]}' para '{nome_final}' e telefone '{telefone_final}'? (S/N): "
        ).strip().upper()
        if confirmacao == "S":
            agenda[indice] = [nome_final, telefone_final]
            salvar_agenda(agenda)
            print("Contato alterado com sucesso!")
        else:
            print("Operação de alteração cancelada.")
    else:
        print(f"Contato '{nome}' não encontrado.")


def ordenar_por_nome(agenda):
    if not agenda:
        print("A agenda está vazia. Nada para ordenar.")
        return
    agenda.sort(key=lambda contato: contato[0].lower())
    salvar_agenda(agenda)
    print("Agenda ordenada por nome com sucesso!")


def menu():
    agenda = carregar_agenda()

    while True:
        total_contatos = len(agenda)
        print(
            f"\n=== AGENDA TELEFÔNICA ({total_contatos} contato(s) cadastrado(s)) ===")
        print("1 - Listar contatos")
        print("2 - Adicionar contato")
        print("3 - Alterar contato")
        print("4 - Apagar contato")
        print("5 - Ordenar por nome")
        print("6 - Salvar e Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            lista(agenda)
        elif opcao == "2":
            novo(agenda)
        elif opcao == "3":
            altera(agenda)
        elif opcao == "4":
            apaga(agenda)
        elif opcao == "5":
            ordenar_por_nome(agenda)
        elif opcao == "6":
            salvar_agenda(agenda)
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
