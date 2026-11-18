"""
Exercício 16.14:
Implemente uma classe Random (aleatória) para gerar números pseudoaleatórios.

A classe implementa um Gerador Linear Congruencial (LCG - Linear Congruential Generator),
o algoritmo clássico fundamental utilizado em bibliotecas padrão de linguagens como C e Java.
Fórmula de recorrência:
    X_{n+1} = (a * X_n + c) mod m
"""

import time
from typing import Any, Optional, Sequence, TypeVar

T = TypeVar("T")


class Random:
    """
    Gerador de números pseudoaleatórios baseado no algoritmo Linear Congruential Generator (LCG).

    Parâmetros clássicos adotados (padrão ANSI C / glibc):
    - m (módulo): 2^31 = 2147483648
    - a (multiplicador): 1103515245
    - c (incremento): 12345
    """

    # Constantes do LCG (padrão POSIX / ANSI C)
    MODULO: int = 2**31          # 2.147.483.648
    MULTIPLICADOR: int = 1103515245
    INCREMENTO: int = 12345

    def __init__(self, semente: Optional[int] = None) -> None:
        """
        Inicializa o gerador.
        - Se 'semente' for informada: garante reprodutibilidade (determinismo).
        - Se for None: utiliza o relógio do sistema em microssegundos para gerar uma semente dinâmica.
        """
        self._semente_original: int = 0
        self._estado_atual: int = 0
        self.definir_semente(semente)

    def definir_semente(self, semente: Optional[int] = None) -> None:
        """
        Define ou redefine a semente (seed) do gerador.
        """
        if semente is None:
            # Usa o tempo atual do sistema em microssegundos
            semente = int(time.time() * 1_000_000)

        self._semente_original = int(semente) % self.MODULO
        self._estado_atual = self._semente_original

    # Alias convencionais
    set_seed = definir_semente

    def proximo_inteiro_bruto(self) -> int:
        """
        Calcula o próximo estado do LCG e retorna um inteiro no intervalo [0, MODULO - 1].
        X_{n+1} = (a * X_n + c) mod m
        """
        self._estado_atual = (
            (self.MULTIPLICADOR * self._estado_atual) + self.INCREMENTO
        ) % self.MODULO
        return self._estado_atual

    def real(self) -> float:
        """
        Gera um número real pseudoaleatório no intervalo semiaberto [0.0, 1.0).
        """
        return self.proximo_inteiro_bruto() / float(self.MODULO)

    # Alias comum
    random = real

    def real_entre(self, minimo: float, maximo: float) -> float:
        """
        Gera um número real no intervalo [minimo, maximo).
        """
        if minimo > maximo:
            minimo, maximo = maximo, minimo
        return minimo + (maximo - minimo) * self.real()

    # Alias comum
    uniform = real_entre

    def inteiro_entre(self, minimo: int, maximo: int) -> int:
        """
        Gera um número inteiro pseudoaleatório no intervalo fechado [minimo, maximo].
        """
        if minimo > maximo:
            minimo, maximo = maximo, minimo

        alcance = (maximo - minimo) + 1
        return minimo + int(self.real() * alcance)

    # Alias comum
    randint = inteiro_entre

    def booleano(self, probabilidade_verdadeiro: float = 0.5) -> bool:
        """
        Gera um booleano True ou False com base na probabilidade informada (padrão 50%).
        """
        return self.real() < probabilidade_verdadeiro

    def escolher(self, sequencia: Sequence[T]) -> T:
        """
        Escolhe e retorna aleatoriamente um elemento da sequência fornecida.
        """
        if not sequencia:
            raise IndexError("Não é possível escolher de uma sequência vazia.")
        indice = self.inteiro_entre(0, len(sequencia) - 1)
        return sequencia[indice]

    def embaralhar(self, lista: list[Any]) -> None:
        """
        Embaralha uma lista in-place utilizando o algoritmo de Fisher-Yates (Knuth shuffle).
        """
        for i in range(len(lista) - 1, 0, -1):
            j = self.inteiro_entre(0, i)
            lista[i], lista[j] = lista[j], lista[i]

    def __repr__(self) -> str:
        return f"Random(semente={self._semente_original}, estado_atual={self._estado_atual})"


# Alias conforme enunciado
random_cls = Random


def main() -> None:
    print("=== Exercício 16.14: Classe Random (Gerador de Números Pseudoaleatórios) ===")

    # 1. Demonstração de determinismo (mesma semente gera a mesma sequência)
    print("\n--- 1. Testando Determinismo com Semente Fixa (seed=12345) ---")
    rng1 = Random(semente=12345)
    rng2 = Random(semente=12345)

    seq1 = [rng1.inteiro_entre(1, 100) for _ in range(6)]
    seq2 = [rng2.inteiro_entre(1, 100) for _ in range(6)]

    print(f"Instância 1 (6 inteiros entre 1 e 100): {seq1}")
    print(f"Instância 2 (6 inteiros entre 1 e 100): {seq2}")
    print(
        f"As sequências são rigorosamente idênticas? {seq1 == seq2} (esperado: True)")

    # 2. Geração de números reais (floats) no intervalo [0.0, 1.0)
    print("\n--- 2. Números Reais no intervalo [0.0, 1.0) ---")
    rng_dinamico = Random()  # Semente baseada no relógio do sistema
    for i in range(4):
        print(f"  real() #{i + 1}: {rng_dinamico.real():.6f}")

    # 3. Geração em intervalos personalizados
    print("\n--- 3. Intervalos Personalizados ---")
    print(
        f"Float entre 10.0 e 20.0:  {rng_dinamico.real_entre(10.0, 20.0):.4f}")
    print(f"Inteiro entre -50 e +50:  {rng_dinamico.inteiro_entre(-50, 50)}")
    print(
        f"Booleano (cara ou coroa): {'Cara' if rng_dinamico.booleano() else 'Coroa'}")

    # 4. Escolha e embaralhamento
    print("\n--- 4. Escolha e Embaralhamento de Coleções ---")
    frutas = ["Maçã", "Banana", "Laranja", "Uva", "Manga", "Morango"]
    fruta_sorteada = rng_dinamico.escolher(frutas)
    print(f"Lista original:    {frutas}")
    print(f"Fruta sorteada:    {fruta_sorteada}")

    copia_frutas = list(frutas)
    rng_dinamico.embaralhar(copia_frutas)
    print(f"Lista embaralhada: {copia_frutas}")

    # 5. Teste de Distribuição: Simulação de 6.000 lançamentos de um dado de 6 faces
    print("\n--- 5. Teste de Frequência: 6.000 Lançamentos de um Dado (1 a 6) ---")
    contadores = {face: 0 for face in range(1, 7)}
    TOTAL_LANCAMENTOS = 6000

    for _ in range(TOTAL_LANCAMENTOS):
        face = rng_dinamico.inteiro_entre(1, 6)
        contadores[face] += 1

    print(
        f"Distribuição esperada teórica por face: {TOTAL_LANCAMENTOS // 6} (~16.67%)")
    for face, contagem in contadores.items():
        porcentagem = (contagem / TOTAL_LANCAMENTOS) * 100
        barra = "#" * int(porcentagem)
        print(
            f"  Face {face}: {contagem:4d} ocorrências ({porcentagem:5.2f}%) | {barra}")


if __name__ == "__main__":
    main()
