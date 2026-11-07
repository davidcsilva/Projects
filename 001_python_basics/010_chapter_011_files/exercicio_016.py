'''
Exercício 9.16 Explique como os campos nome e telefone são armazenados no
arquivo de saída.

'''
codigo_agenda = '''# Programa da Agenda Telefônica com armazenamento de nome e telefone em arquivo

NOME_ARQUIVO = "agenda.txt"

def carregar_agenda():
    """Lê a agenda do arquivo e retorna uma lista de contatos [nome, telefone]."""
    agenda = []
    try:
        with open(NOME_ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    # Cada linha contém nome e telefone separados pelo caractere delimitador '#'
                    partes = linha.split("#")
                    if len(partes) == 2:
                        agenda.append([partes[0], partes[1]])
    except FileNotFoundError:
        # Se o arquivo ainda não existir, inicia com a agenda vazia
        pass
    return agenda

def salvar_agenda(agenda):
    """Grava os contatos no arquivo formatados como nome#telefone."""
    try:
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as f:
            for nome, telefone in agenda:
                f.write(f"{nome}#{telefone}\\n")
        print(f"Agenda salva com sucesso em '{NOME_ARQUIVO}'.")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

def listar_contatos(agenda):
    print("\\n--- CONTATOS CADASTRADOS ---")
    if not agenda:
        print("Nenhum contato na agenda.")
    else:
        for indice, (nome, telefone) in enumerate(agenda, start=1):
            print(f"{indice}. Nome: {nome:<20} | Telefone: {telefone}")
    print("-" * 35)

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
        print("\\n=== AGENDA TELEFÔNICA ===")
        print("1 - Listar contatos")
        print("2 - Adicionar contato")
        print("3 - Salvar e Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_contatos(agenda)
        elif opcao == "2":
            adicionar_contato(agenda)
        elif opcao == "3":
            salvar_agenda(agenda)
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
'''

with open("agenda_telefonica.py", "w", encoding="utf-8") as f:
    f.write(codigo_agenda)
