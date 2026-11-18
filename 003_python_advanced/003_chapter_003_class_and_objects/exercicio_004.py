"""
Exercício 16.4:
Crie uma classe chamada empregado que contenha como membro dado o nome e o número de empregado
e como funções membro Lerdados() e verdados() que leiam os dados do teclado e os visualize
na tela, respectivamente.

Escreva um programa que utilize a classe, criando um array de tipo empregado e logo
preenchendo-o com dados correspondentes a 50 empregados. Uma vez preenchido o array,
visualize os dados de todos os empregados.
"""

import sys
from typing import Optional


class Empregado:
    """
    Representa um empregado com nome e número de identificação.
    """

    def __init__(self, nome: str = "", numero: int = 0) -> None:
        self.nome: str = nome
        self.numero: int = numero

    def Lerdados(self, prompt_prefixo: str = "") -> None:
        """
        Lê os dados do empregado a partir do teclado (entrada padrão).
        """
        self.nome = input(f"{prompt_prefixo}Digite o nome do empregado: ").strip()
        while True:
            try:
                entrada_numero = input(f"{prompt_prefixo}Digite o número do empregado: ").strip()
                self.numero = int(entrada_numero)
                break
            except ValueError:
                print("Valor inválido! Por favor, digite um número inteiro para o número do empregado.")

    # Alias em minúsculas conforme convenções PEP 8
    lerdados = Lerdados

    def verdados(self) -> None:
        """
        Visualiza os dados do empregado na tela de forma formatada.
        """
        print(f"ID / Número: {self.numero:<6} | Nome: {self.nome}")

    def __repr__(self) -> str:
        return f"Empregado(numero={self.numero}, nome={self.nome!r})"


# Alias para o nome em minúsculo conforme enunciado
empregado = Empregado

# Quantidade solicitada no enunciado
QUANTIDADE_EMPREGADOS: int = 50


def cadastrar_empregados(quantidade: int = QUANTIDADE_EMPREGADOS) -> list[Empregado]:
    """
    Cria uma lista (array) e lê os dados de cada empregado do teclado.
    """
    array_empregados: list[Empregado] = []
    print(f"\nCadastrando {quantidade} empregado(s)...")

    try:
        for i in range(quantidade):
            print(f"\n--- Empregado {i + 1} de {quantidade} ---")
            emp = Empregado()
            emp.Lerdados()
            array_empregados.append(emp)
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada interrompida pelo usuário. Prosseguindo com os já cadastrados...")

    return array_empregados


def visualizar_todos(array_empregados: list[Empregado]) -> None:
    """
    Percorre o array e visualiza os dados de todos os empregados cadastrados.
    """
    print("\n" + "=" * 55)
    print(f"{'QUADRO DE EMPREGADOS CADASTRADOS':^55}")
    print("=" * 55)
    print(f"{'Índice':<8} {'Número':<12} {'Nome'}")
    print("-" * 55)

    for i, emp in enumerate(array_empregados, start=1):
        print(f"[{i:02d}]     {emp.numero:<12} {emp.nome}")

    print("=" * 55)
    print(f"Total de empregados listados: {len(array_empregados)}\n")


def main() -> None:
    """
    Função principal do programa:
    1. Cria um array (lista) de tipo empregado.
    2. Preenche-o com dados correspondentes a 50 empregados (ou quantidade informada via argumento).
    3. Uma vez preenchido o array, visualiza os dados de todos os empregados.
    """
    print("=== Exercício 16.4: Cadastro e Visualização de Empregados ===")

    # Permite especificar quantidade via argumento de linha de comando (ex: python3 exercicio_004.py 3)
    # Por padrão, utiliza os 50 empregados solicitados pelo exercício
    quantidade = QUANTIDADE_EMPREGADOS
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        quantidade = int(sys.argv[1])
    elif not sys.stdin.isatty():
        # Modo de demonstração automática quando executado sem terminal interativo
        print(f"[Modo Demonstração]: Criando array com {quantidade} empregados...")
        array_empregados = [
            Empregado(nome=f"Empregado Exemplo {i:02d}", numero=1000 + i)
            for i in range(1, quantidade + 1)
        ]
        visualizar_todos(array_empregados)
        return

    # Preenche o array com os empregados lidos do teclado
    array_empregados = cadastrar_empregados(quantidade)

    # Uma vez preenchido o array, visualiza os dados de todos os empregados
    if array_empregados:
        visualizar_todos(array_empregados)
    else:
        print("Nenhum empregado foi cadastrado.")


if __name__ == "__main__":
    main()
