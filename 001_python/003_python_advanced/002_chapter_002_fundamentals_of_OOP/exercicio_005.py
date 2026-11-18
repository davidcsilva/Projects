'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 15.5

Enunciado:
Deduzir os objetos necessários para projetar um programa de computador que
permita jogar diferentes jogos de cartas.
'''

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
import random


# ==============================================================================
# 1. ELEMENTOS BÁSICOS DO BARALHO (Comuns a Qualquer Jogo de Cartas)
# ==============================================================================

class Naipe(Enum):
    COPAS = "♥ Copas"
    ESPADAS = "♠ Espadas"
    OUROS = "♦ Ouros"
    PAUS = "♣ Paus"


class Valor(Enum):
    AS = (1, "Ás")
    DOIS = (2, "2")
    TRES = (3, "3")
    QUATRO = (4, "4")
    CINCO = (5, "5")
    SEIS = (6, "6")
    SETE = (7, "7")
    OITO = (8, "8")
    NOVE = (9, "9")
    DEZ = (10, "10")
    VALETE = (11, "Valete")
    DAMA = (12, "Dama")
    REI = (13, "Rei")

    def __init__(self, peso_padrao: int, simbolo: str) -> None:
        self.peso_padrao = peso_padrao
        self.simbolo = simbolo


@dataclass(frozen=True)
class Carta:
    """
    Representa uma carta individual.
    Possui naipe, valor facial e pode ter sua visibilidade controlada.
    """
    valor: Valor
    naipe: Naipe

    def __str__(self) -> str:
        return f"[{self.valor.simbolo} de {self.naipe.value}]"


# ==============================================================================
# 2. CONTÊINERES DE CARTAS (Baralho, Mão, Descarte)
# ==============================================================================

class GrupoDeCartas:
    """Classe base para qualquer coleção ou conjunto de cartas."""

    def __init__(self) -> None:
        self.cartas: list[Carta] = []

    def adicionar(self, carta: Carta) -> None:
        self.cartas.append(carta)

    def remover(self, indice: int = -1) -> Carta:
        if not self.cartas:
            raise IndexError("Não há cartas disponíveis para remover.")
        return self.cartas.pop(indice)

    @property
    def quantidade(self) -> int:
        return len(self.cartas)

    def esta_vazio(self) -> bool:
        return len(self.cartas) == 0

    def __str__(self) -> str:
        return ", ".join(str(c) for c in self.cartas) if self.cartas else "(vazio)"


class Baralho(GrupoDeCartas):
    """Representa o monte de compra de cartas (padrão 52 cartas)."""

    def __init__(self, incluir_coringas: bool = False) -> None:
        super().__init__()
        self.incluir_coringas = incluir_coringas
        self.reiniciar()

    def reiniciar(self) -> None:
        """Recria todas as 52 cartas e embaralha."""
        self.cartas = [Carta(v, n) for n in Naipe for v in Valor]
        self.embaralhar()

    def embaralhar(self) -> None:
        random.shuffle(self.cartas)

    def comprar(self) -> Carta:
        """Retira e retorna a carta do topo do baralho."""
        return self.remover()


class Mao(GrupoDeCartas):
    """Representa as cartas que um jogador específico segura."""
    pass


class MonteDeDescarte(GrupoDeCartas):
    """Representa as cartas que foram jogadas na mesa ou descartadas."""
    pass


# ==============================================================================
# 3. PARTICIPANTES (Jogador e Crupiê/Mesa)
# ==============================================================================

@dataclass
class Jogador:
    """Representa um participante da partida (humano ou bot)."""
    nome: str
    mao: Mao = field(default_factory=Mao)
    pontos: int = 0
    fichas: int = 100
    ativo: bool = True

    def receber_carta(self, carta: Carta) -> None:
        self.mao.adicionar(carta)

    def limpar_mao(self) -> None:
        self.mao = Mao()


# ==============================================================================
# 4. POLIMORFISMO E REGRAS: ESTRUTURA PARA DIFERENTES JOGOS (Template Method)
# ==============================================================================

class JogoDeCartas(ABC):
    """
    Classe Abstrata que define o esqueleto (Template Method) de qualquer
    jogo de cartas, garantindo que diferentes jogos possam ser implementados.
    """

    def __init__(self, nome_jogo: str, jogadores: list[Jogador]) -> None:
        self.nome_jogo: str = nome_jogo
        self.jogadores: list[Jogador] = jogadores
        self.baralho: Baralho = Baralho()
        self.descarte: MonteDeDescarte = MonteDeDescarte()

    def iniciar_partida(self) -> None:
        """Método modelo (Template Method) que orquestra a partida."""
        print(f"\n{'='*50}")
        print(f"Iniciando o jogo: {self.nome_jogo}")
        print(f"{'='*50}")
        self.baralho.reiniciar()
        for j in self.jogadores:
            j.limpar_mao()

        self.distribuir_cartas_iniciais()
        self.executar_rodadas()
        vencedor = self.determinar_vencedor()
        print(f"\n>>> Vencedor da partida: {vencedor.nome} <<<")

    @abstractmethod
    def distribuir_cartas_iniciais(self) -> None:
        """Cada jogo define quantas cartas cada jogador recebe no início."""
        pass

    @abstractmethod
    def executar_rodadas(self) -> None:
        """Cada jogo define sua lógica de turnos e jogadas."""
        pass

    @abstractmethod
    def determinar_vencedor(self) -> Jogador:
        """Cada jogo possui sua regra de cálculo de pontos ou vitória."""
        pass


# ==============================================================================
# 5. EXEMPLO CONCRETO: JOGO BLACKJACK (Vinte-e-Um) SIMPLIFICADO
# ==============================================================================

class JogoBlackjack(JogoDeCartas):
    """Implementação concreta de um jogo específico usando a estrutura comum."""

    def __init__(self, jogadores: list[Jogador]) -> None:
        super().__init__("Blackjack (Vinte-e-Um)", jogadores)

    def calcular_pontos(self, mao: Mao) -> int:
        total = 0
        ases = 0
        for c in mao.cartas:
            if c.valor == Valor.AS:
                ases += 1
                total += 11
            elif c.valor in (Valor.VALETE, Valor.DAMA, Valor.REI):
                total += 10
            else:
                total += c.valor.peso_padrao

        # Ajuste do Ás (11 para 1 se estourar 21)
        while total > 21 and ases > 0:
            total -= 10
            ases -= 1
        return total

    def distribuir_cartas_iniciais(self) -> None:
        print("[Distribuição Inicial] Entregando 2 cartas para cada jogador...")
        for _ in range(2):
            for jogador in self.jogadores:
                jogador.receber_carta(self.baralho.comprar())

    def executar_rodadas(self) -> None:
        for jogador in self.jogadores:
            pts = self.calcular_pontos(jogador.mao)
            print(
                f"\nJogador {jogador.nome} com a mão: {jogador.mao} (Total: {pts} pts)")

            # Regra simples de IA: se tiver menos de 16 pontos, compra mais uma carta
            while pts < 16 and not self.baralho.esta_vazio():
                nova_carta = self.baralho.comprar()
                jogador.receber_carta(nova_carta)
                pts = self.calcular_pontos(jogador.mao)
                print(
                    f"  -> {jogador.nome} comprou {nova_carta}. Novo total: {pts} pts")

    def determinar_vencedor(self) -> Jogador:
        melhor_jogador = None
        maior_pontuacao = -1

        for j in self.jogadores:
            pts = self.calcular_pontos(j.mao)
            print(f"Resultado final - {j.nome}: {pts} pontos")
            if pts <= 21 and pts > maior_pontuacao:
                maior_pontuacao = pts
                melhor_jogador = j

        # Caso todos estourem 21, vence o que menos estourou
        if melhor_jogador is None:
            melhor_jogador = min(
                self.jogadores, key=lambda j: self.calcular_pontos(j.mao))

        return melhor_jogador


# ==============================================================================
# Execução e Demonstração
# ==============================================================================
if __name__ == "__main__":
    p1 = Jogador("Alice")
    p2 = Jogador("Bob")
    p3 = Jogador("Crupiê (Mesa)")

    blackjack = JogoBlackjack([p1, p2, p3])
    blackjack.iniciar_partida()
