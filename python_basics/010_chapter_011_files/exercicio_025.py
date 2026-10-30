'''
Exercício 9.25 Altere as funções pede_nome e pede_telefone de forma a receberem
um parâmetro opcional. Caso esse parâmetro seja passado, utilize-o como retorno
caso a entrada de dados seja vazia.

'''
# Programa Completo da Agenda Telefônica (Capítulo 9)
# Incorpora as soluções dos exercícios 9.17 a 9.25

ARQUIVO_CONFIG = "ultima_agenda.cfg"
ARQUIVO_PADRAO = "agenda.txt"

alterada = False
nome_arquivo_atual = ARQUIVO_PADRAO


def pede_nome(padrao=""):
    """Solicita o nome ao utilizador, aceitando valor padrão se premido Enter (Ex. 9.25)."""
    prompt = f"Nome [{padrao}]: " if padrao else "Nome: "
    nome = input(prompt).strip()
    return padrao if nome == "" else nome


def pede_telefone(padrao=""):
    """Solicita o telefone ao utilizador, aceitando valor padrão se premido Enter (Ex. 9.25)."""
    prompt = f"Telefone [{padrao}]: " if padrao else "Telefone: "
    telefone = input(prompt).strip()
    return padrao if telefone == "" else telefone


def obter_ultima_agenda():
    """Lê o nome do último ficheiro utilizado no ficheiro de configuração (Ex. 9.23)."""
    try:
        with open(ARQUIVO_CONFIG, "r", encoding="utf-8") as f:
            nome = f.readline().strip()
            if nome:
                return nome
    except FileNotFoundError:
        pass
    return ARQUIVO_PADRAO


def salvar_ultima_agenda(nome_ficheiro):
    """Guarda o nome do ficheiro ativo no ficheiro de configuração (Ex. 9.23)."""
    try:
        with open(ARQUIVO_CONFIG, "w", encoding="utf-8") as f:
            f.write(nome_ficheiro.strip() + "\n")
    except Exception as e:
        print(f"Erro ao guardar configuração: {e}")


def carregar_agenda(nome_ficheiro):
    """Lê a agenda do ficheiro e reinicializa o controlo de alterações (Ex. 9.22 e 9.23)."""
    global alterada, nome_arquivo_atual
    agenda = []
    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split("#")
                    if len(partes) == 2:
                        agenda.append([partes[0], partes[1]])
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
    """Grava a agenda no disco e desativa o indicador de alterações pendentes (Ex. 9.22 e 9.23)."""
    global alterada, nome_arquivo_atual
    if nome_ficheiro is None:
        nome_ficheiro = nome_arquivo_atual

    try:
        with open(nome_ficheiro, "w", encoding="utf-8") as f:
            for nome, telefone in agenda:
                # Trata caracteres delimitadores caso ocorram (Ex. 9.18)
                nome_limpo = nome.replace("#", "-")
                telefone_limpo = telefone.replace("#", "-")
                f.write(f"{nome_limpo}#{telefone_limpo}\n")
        print(f"Agenda guardada com sucesso em '{nome_ficheiro}'.")
        nome_arquivo_atual = nome_ficheiro
        salvar_ultima_agenda(nome_ficheiro)
        alterada = False
    except Exception as e:
        print(f"Erro ao gravar ficheiro: {e}")


def lista(agenda):
    """Apresenta a lista de contactos exibindo a respetiva posição (Ex. 9.19)."""
    print("\n--- LISTA DE CONTACTOS ---")
    if not agenda:
        print("A agenda está vazia.")
        return

    for posicao, contacto in enumerate(agenda, start=1):
        nome, telefone = contacto[0], contacto[1]
        print(
            f"Posição: {posicao:<3} | Nome: {nome:<25} | Telefone: {telefone}")

    print("-" * 55)


def pesquisa(agenda, nome_pesquisado):
    """Procura um contacto pelo nome (case-insensitive) e devolve o índice."""
    termo = nome_pesquisado.lower()
    for indice, contacto in enumerate(agenda):
        if contacto[0].lower() == termo:
            return indice
    return None


def novo(agenda):
    """Insere um novo contacto na lista e ativa a flag de alteração (Ex. 9.22 e 9.25)."""
    global alterada
    nome = pede_nome()
    telefone = pede_telefone()
    if nome and telefone:
        agenda.append([nome, telefone])
        alterada = True
        print("Contacto adicionado com sucesso!")
    else:
        print("Nome e telefone não podem ser deixados em branco.")


def apaga(agenda):
    """Remove um contacto pedindo confirmação explícita ao utilizador (Ex. 9.21 e 9.22)."""
    global alterada
    nome = pede_nome()
    indice = pesquisa(agenda, nome)

    if indice is not None:
        contato = agenda[indice]
        confirmacao = input(
            f"Tem a certeza de que deseja apagar '{contato[0]}' (Telefone: {contato[1]})? (S/N): "
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
    """Altera os dados mantendo os valores originais por defeito se premido Enter (Ex. 9.21, 9.22 e 9.25)."""
    global alterada
    nome = pede_nome()
    indice = pesquisa(agenda, nome)

    if indice is not None:
        contato = agenda[indice]
        print(f"Dados atuais -> Nome: {contato[0]} | Telefone: {contato[1]}")
        print("(Prima Enter para manter o valor atual exibido entre colchetes)")

        novo_nome = pede_nome(contato[0])
        novo_telefone = pede_telefone(contato[1])

        confirmacao = input(
            f"Confirma alterar para '{novo_nome}' e telefone '{novo_telefone}'? (S/N): "
        ).strip().upper()
        if confirmacao == "S":
            agenda[indice] = [novo_nome, novo_telefone]
            alterada = True
            print("Contacto alterado com sucesso!")
        else:
            print("Operação de alteração cancelada.")
    else:
        print(f"Contacto '{nome}' não encontrado.")


def ordenar_por_nome(agenda):
    """Ordena os contactos alfabeticamente pelo nome (Ex. 9.20 e 9.22)."""
    global alterada
    if not agenda:
        print("A agenda está vazia. Nada para ordenar.")
        return
    agenda.sort(key=lambda item: item[0].lower())
    alterada = True
    print("Agenda ordenada alfabeticamente por nome!")


def menu():
    global alterada, nome_arquivo_atual

    # Carrega a última agenda utilizada ao iniciar (Ex. 9.23)
    arquivo_inicial = obter_ultima_agenda()
    agenda = carregar_agenda(arquivo_inicial)

    while True:
        # Exibe o tamanho da agenda e aviso de alterações não gravadas (Ex. 9.17 e 9.22)
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
            # Confere alterações não salvas antes de carregar outro ficheiro (Ex. 9.22)
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
            # Alerta se houver modificações pendentes antes de fechar o programa (Ex. 9.22)
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
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
