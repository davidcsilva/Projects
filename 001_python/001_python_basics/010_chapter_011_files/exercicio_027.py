'''
Exercício 9.27 Modifique o programa para também controlar a data de aniversário
e o e-mail de cada pessoa.

'''
# Programa Completo da Agenda Telefônica com Aniversário e E-mail (Exercício 9.27)

ARQUIVO_CONFIG = "ultima_agenda.cfg"
ARQUIVO_PADRAO = "agenda.txt"

alterada = False
nome_arquivo_atual = ARQUIVO_PADRAO


def pede_dado(campo, padrao=""):
    """Solicita um dado ao utilizador, aceitando valor padrão caso pressione Enter."""
    prompt = f"{campo} [{padrao}]: " if padrao else f"{campo}: "
    valor = input(prompt).strip()
    return padrao if valor == "" else valor


def obter_ultima_agenda():
    try:
        with open(ARQUIVO_CONFIG, "r", encoding="utf-8") as f:
            nome = f.readline().strip()
            if nome:
                return nome
    except FileNotFoundError:
        pass
    return ARQUIVO_PADRAO


def salvar_ultima_agenda(nome_ficheiro):
    try:
        with open(ARQUIVO_CONFIG, "w", encoding="utf-8") as f:
            f.write(nome_ficheiro.strip() + "\n")
    except Exception as e:
        print(f"Erro ao guardar configuração: {e}")


def carregar_agenda(nome_ficheiro):
    global alterada, nome_arquivo_atual
    agenda = []
    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split("#")
                    # Novo formato com 4 campos
                    if len(partes) >= 4:
                        agenda.append(
                            [partes[0], partes[1], partes[2], partes[3]])
                    # Compatibilidade com arquivos antigos de 2 campos
                    elif len(partes) == 2:
                        agenda.append([partes[0], partes[1], "", ""])
        print(f"Agenda carregada com sucesso de '{nome_ficheiro}'.")
    except FileNotFoundError:
        print(
            f"Ficheiro '{nome_ficheiro}' não encontrado. A iniciar com agenda vazia.")
    except Exception as e:
        print(f"Erro ao ler ficheiro '{nome_ficheiro}': {e}")

    nome_arquivo_atual = nome_ficheiro
    salvar_ultima_agenda(nome_ficheiro)
    alterada = False
    return agenda


def salvar_agenda(agenda, nome_ficheiro=None):
    global alterada, nome_arquivo_atual
    if nome_ficheiro is None:
        nome_ficheiro = nome_arquivo_atual

    try:
        with open(nome_ficheiro, "w", encoding="utf-8") as f:
            for nome, telefone, aniversario, email in agenda:
                nome_limpo = nome.replace("#", "-")
                telefone_limpo = telefone.replace("#", "-")
                aniversario_limpo = aniversario.replace("#", "-")
                email_limpo = email.replace("#", "-")
                f.write(
                    f"{nome_limpo}#{telefone_limpo}#{aniversario_limpo}#{email_limpo}\n")
        print(f"Agenda guardada com sucesso em '{nome_ficheiro}'.")
        nome_arquivo_atual = nome_ficheiro
        salvar_ultima_agenda(nome_ficheiro)
        alterada = False
    except Exception as e:
        print(f"Erro ao gravar ficheiro: {e}")


def lista(agenda):
    print("\n" + "=" * 80)
    print("                              LISTA DE CONTACTOS")
    print("=" * 80)
    if not agenda:
        print("A agenda está vazia.")
        return

    for posicao, contato in enumerate(agenda, start=1):
        nome, telefone, aniversario, email = contato
        print(
            f"Posição: {posicao:<3} | Nome: {nome:<20} | Tel: {telefone:<13} | "
            f"Aniv: {aniversario:<10} | E-mail: {email}"
        )
    print("=" * 80)


def pesquisa(agenda, nome_pesquisado):
    termo = nome_pesquisado.lower()
    for indice, contato in enumerate(agenda):
        if contato[0].lower() == termo:
            return indice
    return None


def novo(agenda):
    global alterada
    nome = pede_dado("Nome")
    if not nome:
        print("Erro: O nome não pode ser deixado em branco.")
        return

    if pesquisa(agenda, nome) is not None:
        print(f"Erro: Já existe um contacto com o nome '{nome}' na agenda.")
        return

    telefone = pede_dado("Telefone")
    aniversario = pede_dado("Data de aniversário (DD/MM/AAAA)")
    email = pede_dado("E-mail")

    if telefone:
        agenda.append([nome, telefone, aniversario, email])
        alterada = True
        print("Contacto adicionado com sucesso!")
    else:
        print("Erro: O telefone não pode ser deixado em branco.")


def apaga(agenda):
    global alterada
    nome = pede_dado("Nome do contacto a apagar")
    indice = pesquisa(agenda, nome)

    if indice is not None:
        contato = agenda[indice]
        confirmacao = input(
            f"Tem a certeza de que deseja apagar '{contato[0]}' (Tel: {contato[1]})? (S/N): "
        ).strip().upper()
        if confirmacao == "S":
            del agenda[indice]
            alterada = True
            print(f"Contacto '{contato[0]}' apagado com sucesso!")
        else:
            print("Operação de eliminação cancelada.")
    else:
        print(f"Contacto '{nome}' não encontrado.")


def altera(agenda):
    global alterada
    nome = pede_dado("Nome do contacto a alterar")
    indice = pesquisa(agenda, nome)

    if indice is not None:
        contato = agenda[indice]
        print(
            f"Dados atuais -> Nome: {contato[0]} | Tel: {contato[1]} | "
            f"Aniv: {contato[2]} | E-mail: {contato[3]}"
        )
        print("(Prima Enter para manter o valor atual exibido entre colchetes)")

        novo_nome = pede_dado("Nome", contato[0])

        if novo_nome.lower() != contato[0].lower():
            if pesquisa(agenda, novo_nome) is not None:
                print(
                    f"Erro: Já existe outro contacto registado como '{novo_nome}'. Alteração cancelada.")
                return

        novo_telefone = pede_dado("Telefone", contato[1])
        novo_aniversario = pede_dado("Data de aniversário", contato[2])
        novo_email = pede_dado("E-mail", contato[3])

        confirmacao = input(
            f"Confirma a alteração dos dados de '{contato[0]}'? (S/N): "
        ).strip().upper()
        if confirmacao == "S":
            agenda[indice] = [novo_nome, novo_telefone,
                              novo_aniversario, novo_email]
            alterada = True
            print("Contacto alterado com sucesso!")
        else:
            print("Operação de alteração cancelada.")
    else:
        print(f"Contacto '{nome}' não encontrado.")


def ordenar_por_nome(agenda):
    global alterada
    if not agenda:
        print("A agenda está vazia. Nada para ordenar.")
        return
    agenda.sort(key=lambda item: item[0].lower())
    alterada = True
    print("Agenda ordenada alfabeticamente por nome!")


def menu():
    global alterada, nome_arquivo_atual

    arquivo_inicial = obter_ultima_agenda()
    agenda = carregar_agenda(arquivo_inicial)

    while True:
        total = len(agenda)
        status_alteracao = " [ALTERAÇÕES NÃO SALVAS]" if alterada else ""
        print(
            f"\n=== AGENDA: '{nome_arquivo_atual}' ({total} contacto(s)){status_alteracao} ===")
        print("1 - Listar contactos")
        print("2 - Adicionar contacto (novo)")
        print("3 - Alterar contacto")
        print("4 - Apagar contacto")
        print("5 - Ordenar por nome")
        print("6 - Gravar agenda no ficheiro")
        print("7 - Ler agenda de outro ficheiro")
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
            nome_arq = input(
                f"Nome do ficheiro para guardar (Enter para '{nome_arquivo_atual}'): ").strip()
            salvar_agenda(agenda, nome_arq if nome_arq else nome_arquivo_atual)
        elif opcao == "7":
            if alterada:
                resp = input(
                    "A agenda tem alterações não gravadas! Deseja gravar antes de trocar? (S/N/Cancela): ").strip().upper()
                if resp == "S":
                    salvar_agenda(agenda, nome_arquivo_atual)
                elif resp != "N":
                    print("Operação cancelada.")
                    continue
            nome_arq = input("Nome do ficheiro a abrir: ").strip()
            if nome_arq:
                agenda = carregar_agenda(nome_arq)
            else:
                print("Nome de ficheiro inválido.")
        elif opcao == "8":
            if alterada:
                resp = input(
                    "Existem alterações não gravadas. Deseja guardar antes de sair? (S/N/Cancela): ").strip().upper()
                if resp == "S":
                    salvar_agenda(agenda, nome_arquivo_atual)
                    print("A terminar o programa...")
                    break
                elif resp == "N":
                    print("A sair sem gravar alterações...")
                    break
                else:
                    print("Operação de saída cancelada.")
            else:
                print("A terminar o programa...")
                break
        else:
            print("Opção inválida")
