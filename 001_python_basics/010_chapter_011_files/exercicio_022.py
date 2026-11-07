'''
Exercício 9.22 Ao ler ou gravar uma nova lista, verifique se a agenda atual já foi
gravada. Você pode usar uma variável para controlar quando a lista foi alterada
(novo, altera, apaga) e reinicializar esse valor quando ela for lida ou gravada.


'''
# Programa da Agenda Telefônica com controle de alterações não salvas (Exercício 9.22)

NOME_ARQUIVO = "agenda.txt"

# Variável de controle: True indica que há alterações na memória que ainda não foram gravadas
alterada = False


def carregar_agenda(nome_arquivo=NOME_ARQUIVO):
    """Lê a agenda do arquivo e reinicializa a flag de alteração."""
    global alterada
    agenda = []
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split("#")
                    if len(partes) == 2:
                        agenda.append([partes[0], partes[1]])
        print(f"Agenda carregada com sucesso de '{nome_arquivo}'.")
    except FileNotFoundError:
        print(
            f"Arquivo '{nome_arquivo}' não encontrado. Iniciando agenda vazia.")

    # Ao ler um arquivo, a lista está sincronizada com o disco
    alterada = False
    return agenda


def salvar_agenda(agenda, nome_arquivo=NOME_ARQUIVO):
    """Grava os contatos no arquivo formatados como nome#telefone e zera a flag de alteração."""
    global alterada
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            for nome, telefone in agenda:
                f.write(f"{nome}#{telefone}\n")
        print(f"Agenda salva com sucesso em '{nome_arquivo}'.")
        # Após salvar com sucesso, não há alterações pendentes
        alterada = False
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
    global alterada
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    if nome and telefone:
        agenda.append([nome, telefone])
        alterada = True
        print("Contato adicionado com sucesso!")
    else:
        print("Nome e telefone não podem ser vazios.")


def apaga(agenda):
    global alterada
    nome = input("Nome do contato a apagar: ").strip()
    indice = pesquisa(agenda, nome)

    if indice is not None:
        contato = agenda[indice]
        confirmacao = input(
            f"Tem certeza que deseja apagar o contato '{contato[0]}' (Telefone: {contato[1]})? (S/N): "
        ).strip().upper()
        if confirmacao == "S":
            del agenda[indice]
            alterada = True
            print(f"Contato '{contato[0]}' apagado com sucesso!")
        else:
            print("Operação de exclusão cancelada.")
    else:
        print(f"Contato '{nome}' não encontrado.")


def altera(agenda):
    global alterada
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
            alterada = True
            print("Contato alterado com sucesso!")
        else:
            print("Operação de alteração cancelada.")
    else:
        print(f"Contato '{nome}' não encontrado.")


def ordenar_por_nome(agenda):
    global alterada
    if not agenda:
        print("A agenda está vazia. Nada para ordenar.")
        return
    agenda.sort(key=lambda contato: contato[0].lower())
    alterada = True
    print("Agenda ordenada por nome com sucesso!")


def menu():
    global alterada
    agenda = carregar_agenda()

    while True:
        total_contatos = len(agenda)
        status_alteracao = " [ALTERAÇÕES NÃO SALVAS]" if alterada else ""
        print(
            f"\n=== AGENDA TELEFÔNICA ({total_contatos} contato(s)){status_alteracao} ===")
        print("1 - Listar contatos")
        print("2 - Adicionar contato (novo)")
        print("3 - Alterar contato")
        print("4 - Apagar contato")
        print("5 - Ordenar por nome")
        print("6 - Gravar agenda no arquivo")
        print("7 - Ler nova lista do arquivo")
        print("8 - Sair")
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
        elif opcao == "7":
            # Verifica se há modificações antes de sobrepor a agenda com um novo arquivo
            if alterada:
                resp = input(
                    "A agenda atual possui alterações não gravadas! Deseja salvar antes de ler? (S/N/Cancela): ").strip().upper()
                if resp == "S":
                    salvar_agenda(agenda)
                elif resp != "N":
                    print("Operação cancelada.")
                    continue
            nome_arq = input(
                f"Nome do arquivo para ler (pressione Enter para '{NOME_ARQUIVO}'): ").strip()
            agenda = carregar_agenda(nome_arq if nome_arq else NOME_ARQUIVO)
        elif opcao == "8":
            # Alerta ao tentar sair sem gravar
            if alterada:
                resp = input(
                    "Há alterações não salvas na agenda. Deseja salvar antes de sair? (S/N/Cancela): ").strip().upper()
                if resp == "S":
                    salvar_agenda(agenda)
                    print("Encerrando programa...")
                    break
                elif resp == "N":
                    print("Saindo sem salvar as alterações...")
                    break
                else:
                    print("Operação de saída cancelada.")
            else:
                print("Encerrando programa...")
                break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
