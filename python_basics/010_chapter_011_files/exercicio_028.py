'''
Exercício 9.28 Modifique o programa de forma a poder registrar vários
telefones para a mesma pessoa. Permita também cadastrar o tipo de telefone:
celular, fixo, residência, trabalho ou fax.

'''
# Programa Completo da Agenda Telefônica com Múltiplos Telefones e Tipos (Exercício 9.28)

ARQUIVO_CONFIG = "ultima_agenda.cfg"
ARQUIVO_PADRAO = "agenda.txt"

alterada = False
nome_arquivo_atual = ARQUIVO_PADRAO

TIPOS_TELEFONE_VALIDOS = ["celular", "fixo", "residência", "trabalho", "fax"]


def pede_dado(campo, padrao=""):
    """Solicita um dado ao utilizador, aceitando valor padrão caso pressione Enter."""
    prompt = f"{campo} [{padrao}]: " if padrao else f"{campo}: "
    valor = input(prompt).strip()
    return padrao if valor == "" else valor


def pede_telefones(telefones_atuais=None):
    """
    Permite cadastrar ou gerenciar múltiplos telefones com tipo para um contato.
    Cada telefone é representado por uma lista: [numero, tipo].
    """
    telefones = list(telefones_atuais) if telefones_atuais else []

    if telefones:
        print("\nTelefones atuais cadastrados:")
        for idx, (num, tipo) in enumerate(telefones, start=1):
            print(f"  {idx}. {num} ({tipo})")

        resp = input(
            "Deseja alterar/substituir a lista de telefones? (S/N): ").strip().upper()
        if resp != "S":
            return telefones
        telefones = []

    print("\nCadastro de telefones (deixe o número em branco para encerrar):")
    print(f"Tipos disponíveis: {', '.join(TIPOS_TELEFONE_VALIDOS)}")

    while True:
        numero = input("Número de telefone (Enter para finalizar): ").strip()
        if not numero:
            if not telefones:
                print("Aviso: É necessário informar ao menos um telefone.")
                continue
            break

        while True:
            tipo = input(
                f"Tipo do telefone {numero} (celular/fixo/residência/trabalho/fax) [celular]: ").strip().lower()
            if not tipo:
                tipo = "celular"
            if tipo in TIPOS_TELEFONE_VALIDOS:
                break
            print(
                f"Tipo inválido! Escolha entre: {', '.join(TIPOS_TELEFONE_VALIDOS)}")

        telefones.append([numero, tipo])

    return telefones


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
                if not linha:
                    continue
                partes = linha.split("#")

                # Formato completo: nome, aniversario, email, telefones_str
                if len(partes) >= 4:
                    nome = partes[0]
                    aniversario = partes[1]
                    email = partes[2]
                    telefones_str = partes[3]

                    telefones = []
                    if telefones_str:
                        for item in telefones_str.split(","):
                            if "@" in item:
                                num, tipo = item.split("@", 1)
                                telefones.append([num, tipo])
                            else:
                                telefones.append([item, "celular"])
                    agenda.append([nome, telefones, aniversario, email])

                # Compatibilidade legada com arquivos de 2 campos (nome#telefone)
                elif len(partes) == 2:
                    agenda.append(
                        [partes[0], [[partes[1], "celular"]], "", ""])

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
            for nome, telefones, aniversario, email in agenda:
                nome_limpo = nome.replace("#", "-")
                aniv_limpo = aniversario.replace("#", "-")
                email_limpo = email.replace("#", "-")

                # Serializa a lista de telefones
                tels_formatados = []
                for num, tipo in telefones:
                    num_limpo = num.replace(
                        "#", "-").replace("@", "-").replace(",", "-")
                    tipo_limpo = tipo.replace(
                        "#", "-").replace("@", "-").replace(",", "-")
                    tels_formatados.append(f"{num_limpo}@{tipo_limpo}")
                telefones_str = ",".join(tels_formatados)

                f.write(
                    f"{nome_limpo}#{aniv_limpo}#{email_limpo}#{telefones_str}\n")

        print(f"Agenda guardada com sucesso em '{nome_ficheiro}'.")
        nome_arquivo_atual = nome_ficheiro
        salvar_ultima_agenda(nome_ficheiro)
        alterada = False
    except Exception as e:
        print(f"Erro ao gravar agenda: {e}")
