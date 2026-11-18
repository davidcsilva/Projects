"""
Exercício 16.5:
Efetue um programa que calcule a distância média correspondente a 100 distâncias
entre cidades dadas, cada uma delas em quilômetros e metros.
"""

import random
import sys
from typing import Optional


class Distancia:
    """
    Representa uma distância entre cidades expressa em quilômetros e metros.
    Mantém os valores normalizados (1000 metros = 1 quilômetro).
    """

    def __init__(self, quilometros: int = 0, metros: float = 0.0) -> None:
        self.quilometros: int = int(quilometros)
        self.metros: float = float(metros)
        self._ajustar()

    def _ajustar(self) -> None:
        """
        Normaliza a distância para garantir que 0 <= metros < 1000.
        Cada 1000 metros completados são convertidos em 1 quilômetro.
        """
        if self.metros >= 1000.0 or self.metros < 0:
            extra_km = int(self.metros // 1000)
            self.metros = self.metros % 1000.0
            self.quilometros += extra_km

    def em_metros(self) -> float:
        """Retorna o valor total da distância convertido para metros."""
        return self.quilometros * 1000.0 + self.metros

    @classmethod
    def de_metros(cls, total_metros: float) -> "Distancia":
        """Cria e retorna uma nova Distancia a partir de um valor escalar em metros."""
        km = int(total_metros // 1000)
        m = total_metros % 1000.0
        return cls(quilometros=km, metros=m)

    def ler_dados(self, prompt_prefixo: str = "") -> None:
        """Lê os quilômetros e metros a partir do teclado."""
        while True:
            try:
                km_in = input(
                    f"{prompt_prefixo}Digite os quilômetros (km): ").strip()
                m_in = input(f"{prompt_prefixo}Digite os metros (m): ").strip()
                self.quilometros = int(km_in)
                self.metros = float(m_in)
                if self.quilometros < 0 or self.metros < 0:
                    print("Por favor, digite valores não-negativos.")
                    continue
                self._ajustar()
                break
            except ValueError:
                print("Entrada inválida! Digite números válidos.")

    def visualizar(self) -> None:
        """Exibe a distância no formato legível."""
        print(f"{self.quilometros} km e {self.metros:.2f} m")

    def somar(self, outra: "Distancia") -> "Distancia":
        """Soma duas distâncias e retorna um novo objeto Distancia."""
        return Distancia.de_metros(self.em_metros() + outra.em_metros())

    def dividir(self, divisor: float) -> "Distancia":
        """Divide a distância por um número escalar."""
        if divisor <= 0:
            raise ValueError("O divisor deve ser um número positivo.")
        return Distancia.de_metros(self.em_metros() / divisor)

    def __add__(self, outra: "Distancia") -> "Distancia":
        return self.somar(outra)

    def __truediv__(self, divisor: float) -> "Distancia":
        return self.dividir(divisor)

    def __str__(self) -> str:
        return f"{self.quilometros} km e {self.metros:.2f} m"

    def __repr__(self) -> str:
        return f"Distancia(km={self.quilometros}, m={self.metros:.2f})"


# Quantidade de distâncias especificada no enunciado
TOTAL_DISTANCIAS: int = 100


def calcular_distancia_media(distancias: list[Distancia]) -> Distancia:
    """
    Calcula a distância média a partir de uma lista de objetos Distancia.
    """
    if not distancias:
        raise ValueError("A lista de distâncias não pode ser vazia.")

    # Soma de todas as distâncias acumuladas
    soma_total = Distancia(0, 0.0)
    for d in distancias:
        soma_total = soma_total + d

    # Média = soma_total / quantidade
    return soma_total / len(distancias)


def gerar_distancias_amostra(quantidade: int = TOTAL_DISTANCIAS) -> list[Distancia]:
    """
    Gera distâncias realistas simuladas entre cidades (ex: entre 50 km e 1200 km)
    para permitir teste e demonstração imediata do cálculo de 100 cidades.
    """
    random.seed(42)  # Semente fixa para resultados reproduzíveis
    amostras: list[Distancia] = []
    for _ in range(quantidade):
        km = random.randint(50, 1200)
        metros = round(random.uniform(0.0, 999.9), 2)
        amostras.append(Distancia(quilometros=km, metros=metros))
    return amostras


def ler_distancias_teclado(quantidade: int) -> list[Distancia]:
    """Lê as distâncias interativamente do usuário."""
    distancias: list[Distancia] = []
    print(f"\nColetando {quantidade} distâncias via teclado...")
    for i in range(quantidade):
        print(f"\n--- Distância {i + 1} de {quantidade} ---")
        d = Distancia()
        d.ler_dados(prompt_prefixo="  ")
        distancias.append(d)
    return distancias


def main() -> None:
    print("=== Exercício 16.5: Distância Média entre 100 Cidades ===")

    quantidade = TOTAL_DISTANCIAS

    # Suporte a parâmetro via linha de comando para quantidade personalizada (ex: python3 exercicio_005.py 5)
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        quantidade = int(sys.argv[1])

    # Verifica se a execução é interativa e se o usuário prefere gerar ou digitar
    distancias: list[Distancia] = []
    if sys.stdin.isatty():
        print(
            f"\nO exercício solicita o cálculo para {quantidade} distâncias.")
        print("Opções:")
        print("  1 - Gerar dados automaticamente (recomendado para 100 distâncias)")
        print("  2 - Digitar manualmente do teclado")
        escolha = input("Escolha uma opção [1/2] (padrão=1): ").strip()

        if escolha == "2":
            distancias = ler_distancias_teclado(quantidade)
        else:
            print(
                f"\nGerando {quantidade} distâncias representativas entre cidades...")
            distancias = gerar_distancias_amostra(quantidade)
    else:
        # Modo não-interativo / execução em script
        print(
            f"Execução automatizada: gerando {quantidade} distâncias de cidades...")
        distancias = gerar_distancias_amostra(quantidade)

    # Exibição das primeiras e últimas distâncias para conferência
    print("\n--- Amostra das Distâncias Coletadas ---")
    qtd_exibir = min(5, len(distancias))
    for i in range(qtd_exibir):
        print(f"Distância {i + 1:03d}: {distancias[i]}")
    if len(distancias) > qtd_exibir:
        print(
            f"... ({len(distancias) - (qtd_exibir * 2)} outras distâncias) ...")
        for i in range(len(distancias) - qtd_exibir, len(distancias)):
            print(f"Distância {i + 1:03d}: {distancias[i]}")

    # Cálculo da distância total e média
    soma_total = Distancia(0, 0.0)
    for d in distancias:
        soma_total += d

    media = calcular_distancia_media(distancias)

    print("\n" + "=" * 50)
    print(f"Quantidade de distâncias processadas: {len(distancias)}")
    print(f"Distância total acumulada: {soma_total}")
    print(f"Distância média: {media}")
    print(
        f"Distância média (em formato decimal): {media.em_metros() / 1000.0:.3f} km")
    print("=" * 50)


if __name__ == "__main__":
    main()
