'''
Exercício 9.18 O que acontece se nome ou telefone contiverem o caractere usado
como separador em seus conteúdos? Explique o problema e proponha uma solução.

'''

import csv

# Gravando com segurança


def salvar_agenda(agenda):
    with open("agenda.csv", "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f, delimiter="#")
        escritor.writerows(agenda)

# Lendo com segurança


def carregar_agenda():
    agenda = []
    try:
        with open("agenda.csv", "r", encoding="utf-8") as f:
            leitor = csv.reader(f, delimiter="#")
            for linha in leitor:
                if linha:
                    agenda.append(linha)
    except FileNotFoundError:
        pass
    return agenda


def adicionar_contato(agenda):
    nome = input("Nome: ").replace("#", "-").strip()
    telefone = input("Telefone: ").replace("#", "-").strip()
    agenda.append([nome, telefone])
