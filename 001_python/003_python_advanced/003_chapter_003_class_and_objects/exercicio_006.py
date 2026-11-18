"""
Exercício 16.6:
Classe Vetor3D para manipular vetores de três componentes (coordenadas x, y, z):
- Somente possui uma função construtora e é em linha.
- Tem uma função membro igual que permite saber se dois vetores têm seus componentes
  ou coordenadas iguais:
    a) Transmissão por valor
    b) Transmissão por endereço
    c) Transmissão por referência
"""

import copy
import math
from typing import Optional


class Vetor3D:
    """
    Representa um vetor tridimensional no espaço cartesiano (x, y, z).
    """

    # --- Norma 1: Somente possui uma função construtora e é em linha ---
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        """
        Único construtor da classe (em linha / inline).
        Graças aos parâmetros com valores padrão (0.0), atua tanto como construtor
        padrão (x=0, y=0, z=0) quanto como construtor com parâmetros.
        """
        self.x: float = float(x)
        self.y: float = float(y)
        self.z: float = float(z)

    # --- Norma 2: Funções membro 'igual' ---

    def igual_por_valor(self, outro: "Vetor3D") -> bool:
        """
        a) Transmissão por valor (Pass-by-value):
        No modelo clássico de C++ (bool igual(Vetor3D outro)), o objeto passado
        é inteiramente clonado/copiado para a pilha de execução da função.
        Em Python, simulamos a passagem por valor criando explicitamente uma cópia
        independente (cópia rasa via copy.copy) antes de inspecionar as coordenadas.
        """
        if not isinstance(outro, Vetor3D):
            return False

        # Cria uma cópia independente simulando a transmissão por valor
        copia_outro = copy.copy(outro)
        return (
            math.isclose(self.x, copia_outro.x, abs_tol=1e-9)
            and math.isclose(self.y, copia_outro.y, abs_tol=1e-9)
            and math.isclose(self.z, copia_outro.z, abs_tol=1e-9)
        )

    def igual_por_endereco(self, outro: Optional["Vetor3D"]) -> bool:
        """
        b) Transmissão por endereço / ponteiro (Pass-by-pointer/address):
        Em C++ (bool igual(const Vetor3D* outro)), a função recebe o endereço de
        memória do objeto. Ela verifica se o ponteiro é válido (não-nulo) e
        acessa os atributos através da desreferenciação (outro->x, outro->y, outro->z).
        Se self e outro apontarem para o mesmo endereço (self is outro), a igualdade é imediata.
        """
        if outro is None or not isinstance(outro, Vetor3D):
            return False

        # Otimização: se os dois apontam para o mesmo endereço de memória
        if self is outro:
            return True

        return (
            math.isclose(self.x, outro.x, abs_tol=1e-9)
            and math.isclose(self.y, outro.y, abs_tol=1e-9)
            and math.isclose(self.z, outro.z, abs_tol=1e-9)
        )

    def igual_por_referencia(self, outro: "Vetor3D") -> bool:
        """
        c) Transmissão por referência (Pass-by-reference):
        Em C++ (bool igual(const Vetor3D& outro)), o parâmetro é um alias/referência
        direta ao objeto original, evitando overhead de cópia.
        Em Python, este é o modelo nativo ('call-by-object-reference'): o parâmetro 'outro'
        já se vincula diretamente ao mesmo objeto em memória.
        """
        if not isinstance(outro, Vetor3D):
            return False

        return (
            math.isclose(self.x, outro.x, abs_tol=1e-9)
            and math.isclose(self.y, outro.y, abs_tol=1e-9)
            and math.isclose(self.z, outro.z, abs_tol=1e-9)
        )

    def igual(self, outro: Optional["Vetor3D"], modo: str = "referencia") -> bool:
        """
        Função membro unificada que despacha para a forma desejada de transmissão:
        'valor', 'endereco' ou 'referencia'.
        """
        modo = modo.lower()
        if modo == "valor":
            assert outro is not None
            return self.igual_por_valor(outro)
        elif modo == "endereco":
            return self.igual_por_endereco(outro)
        elif modo == "referencia":
            assert outro is not None
            return self.igual_por_referencia(outro)
        else:
            raise ValueError(
                f"Modo desconhecido: {modo!r}. Escolha 'valor', 'endereco' ou 'referencia'.")

    def __eq__(self, outro: object) -> bool:
        """Sobrecarga do operador de igualdade (==) em Python."""
        if not isinstance(outro, Vetor3D):
            return False
        return self.igual_por_referencia(outro)

    def __repr__(self) -> str:
        return f"Vetor3D(x={self.x}, y={self.y}, z={self.z})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"


# Alias em minúsculo conforme enunciado
vetor3d = Vetor3D


def main() -> None:
    print("=== Exercício 16.6: Classe Vetor3D e Métodos de Comparação ===")

    # 1. Demonstração do construtor único em linha (inline)
    v_padrao = Vetor3D()             # Inicializa em (0.0, 0.0, 0.0)
    v1 = Vetor3D(3.0, 4.0, 5.0)      # Inicializa com valores fixos
    v2 = Vetor3D(3.0, 4.0, 5.0)      # Outro objeto, mesmas coordenadas
    v3 = Vetor3D(1.0, 2.0, 3.0)      # Outro objeto, coordenadas diferentes
    v_mesmo = v1                     # Referência ao mesmo objeto de v1

    print(f"Vetor padrão:  {v_padrao}")
    print(f"Vetor v1:      {v1} (id: {id(v1)})")
    print(f"Vetor v2:      {v2} (id: {id(v2)})")
    print(f"Vetor v3:      {v3} (id: {id(v3)})")
    print(f"Vetor v_mesmo: {v_mesmo} (id: {id(v_mesmo)})")

    # a) Transmissão por valor
    print("\n--- a) Transmissão por Valor ---")
    print(
        f"v1.igual_por_valor(v2) -> {v1.igual_por_valor(v2)} (coordenadas iguais: True)")
    print(
        f"v1.igual_por_valor(v3) -> {v1.igual_por_valor(v3)} (coordenadas diferentes: False)")

    # b) Transmissão por endereço
    print("\n--- b) Transmissão por Endereço (Ponteiro) ---")
    print(
        f"v1.igual_por_endereco(v_mesmo) -> {v1.igual_por_endereco(v_mesmo)} (mesmo endereço: True)")
    print(
        f"v1.igual_por_endereco(v2)      -> {v1.igual_por_endereco(v2)} (endereços diferentes, coordenadas iguais: True)")
    print(
        f"v1.igual_por_endereco(v3)      -> {v1.igual_por_endereco(v3)} (coordenadas diferentes: False)")
    print(
        f"v1.igual_por_endereco(None)    -> {v1.igual_por_endereco(None)} (ponteiro nulo: False)")

    # c) Transmissão por referência
    print("\n--- c) Transmissão por Referência ---")
    print(
        f"v1.igual_por_referencia(v2) -> {v1.igual_por_referencia(v2)} (esperado: True)")
    print(
        f"v1.igual_por_referencia(v3) -> {v1.igual_por_referencia(v3)} (esperado: False)")

    # Testando com a função membro unificada igual() e sobrecarga ==
    print("\n--- Função igual() com parâmetro de modo e operador == ---")
    print(f"v1.igual(v2, modo='valor')      -> {v1.igual(v2, modo='valor')}")
    print(
        f"v1.igual(v2, modo='endereco')   -> {v1.igual(v2, modo='endereco')}")
    print(
        f"v1.igual(v2, modo='referencia') -> {v1.igual(v2, modo='referencia')}")
    print(f"v1 == v2                        -> {v1 == v2}")
    print(f"v1 == v3                        -> {v1 == v3}")


if __name__ == "__main__":
    main()
