'''
Exercício 9.26 Altere o programa de forma a verificar a repetição de nomes. Gere
uma mensagem de erro caso duas entradas na agenda tenham o mesmo nome.

'''

# Programa Completo da Agenda Telefônica (Capítulo 9)
# Incorpora as soluções dos exercícios 9.17 até 9.26

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
    print
