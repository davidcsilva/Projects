"""
Exercício 16.8:
Projete uma classe vetor3d que permita manipular vetores de três componentes (de tipo real),
que contenha uma função construtor com valores por default (0) e as funções membro:
- soma: soma de dois vetores
- produto_escalar: produto escalar de dois vetores
  (v1 = x1, y1, z1; v2 = x2, y2, z2; v1 * v2 = x1*x2 + y1*y2 + z1*z2)
"""

from typing import Union


class Vetor3D:
    """
    Representa um vetor tridimensional no espaço cartesiano (x, y, z) com componentes reais.
    """

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        """
        Função construtora com valores padrão (default) iguais a 0.0.
        Permite criar:
        - Vetor nulo: Vetor3D() -> (0.0, 0.0, 0.0)
        - Vetor com valores específicos: Vetor3D(1.5, 2.0, -3.2)
        """
        self.x: float = float(x)
        self.y: float = float(y)
        self.z: float = float(z)

    def soma(self, v2: "Vetor3D") -> "Vetor3D":
        """
        Calcula a soma deste vetor (self) com outro vetor (v2).
        Retorna um novo objeto Vetor3D com a soma das componentes:
        (x1 + x2, y1 + y2, z1 + z2)
        """
        if not isinstance(v2, Vetor3D):
            raise TypeError(
                "O argumento para soma deve ser uma instância de Vetor3D.")

        return Vetor3D(
            x=self.x + v2.x,
            y=self.y + v2.y,
            z=self.z + v2.z,
        )

    def produto_escalar(self, v2: "Vetor3D") -> float:
        """
        Calcula o produto escalar (dot product) entre este vetor (self) e outro vetor (v2).
        Fórmula: v1 * v2 = x1*x2 + y1*y2 + z1*z2
        Retorna um valor real (float).
        """
        if not isinstance(v2, Vetor3D):
            raise TypeError(
                "O argumento para produto escalar deve ser uma instância de Vetor3D.")

        return (self.x * v2.x) + (self.y * v2.y) + (self.z * v2.z)

    # Alias sem underline caso solicitado exatamente como produtoescalar
    produtoescalar = produto_escalar

    # --- Sobrecarga de Operadores em Python ---

    def __add__(self, outro: "Vetor3D") -> "Vetor3D":
        """Sobrecarga do operador '+': permite a sintaxe v1 + v2."""
        return self.soma(outro)

    def __mul__(self, outro: Union["Vetor3D", float, int]) -> Union[float, "Vetor3D"]:
        """
        Sobrecarga do operador '*':
        - Se multiplicado por outro Vetor3D: produto escalar (retorna float).
        - Se multiplicado por um escalar (float/int): multiplicação por escalar (retorna Vetor3D).
        """
        if isinstance(outro, Vetor3D):
            return self.produto_escalar(outro)
        elif isinstance(outro, (int, float)):
            return Vetor3D(self.x * outro, self.y * outro, self.z * outro)
        return NotImplemented

    def __rmul__(self, escalar: Union[float, int]) -> "Vetor3D":
        """Permite multiplicação escalar à esquerda: 2.5 * v1."""
        if isinstance(escalar, (int, float)):
            return Vetor3D(self.x * escalar, self.y * escalar, self.z * escalar)
        return NotImplemented

    def __matmul__(self, outro: "Vetor3D") -> float:
        """Sobrecarga do operador '@' (operador nativo de produto de matrizes/vetores no Python)."""
        return self.produto_escalar(outro)

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return f"Vetor3D(x={self.x}, y={self.y}, z={self.z})"


# Alias conforme convenção do enunciado
vetor3d = Vetor3D


def main() -> None:
    print("=== Exercício 16.8: Classe Vetor3D (Soma e Produto Escalar) ===")

    # 1. Demonstração do construtor com valores default (0) e com valores fixos
    v_padrao = Vetor3D()
    v1 = Vetor3D(1.0, 2.0, 3.0)
    v2 = Vetor3D(4.0, 5.0, 6.0)

    print(f"Vetor criado por default (zeros): {v_padrao}")
    print(f"Vetor v1: {v1}")
    print(f"Vetor v2: {v2}")

    # 2. Demonstração da função membro soma
    v_soma = v1.soma(v2)
    print("\n--- Operação de Soma de Dois Vetores ---")
    print(f"v1.soma(v2):")
    print(f"  Componente x: {v1.x} + {v2.x} = {v_soma.x}")
    print(f"  Componente y: {v1.y} + {v2.y} = {v_soma.y}")
    print(f"  Componente z: {v1.z} + {v2.z} = {v_soma.z}")
    print(f"  Resultado: {v1} + {v2} = {v_soma}")
    print(f"  Usando operador '+': {v1 + v2}")

    # 3. Demonstração da função membro produto_escalar
    # v1 * v2 = (1*4) + (2*5) + (3*6) = 4 + 10 + 18 = 32.0
    prod_esc = v1.produto_escalar(v2)
    print("\n--- Operação de Produto Escalar ---")
    print(f"v1.produto_escalar(v2):")
    print(
        f"  Cálculo: ({v1.x} * {v2.x}) + ({v1.y} * {v2.y}) + ({v1.z} * {v2.z})")
    print(
        f"  Cálculo: ({v1.x * v2.x}) + ({v1.y * v2.y}) + ({v1.z * v2.z}) = {prod_esc}")
    print(f"  Usando v1 * v2: {v1 * v2}")
    print(f"  Usando v1 @ v2: {v1 @ v2}")

    # 4. Demonstração com vetores ortogonais (produto escalar deve ser 0)
    # v_orto1 = (1, 0, 0), v_orto2 = (0, 1, 0)
    v_orto1 = Vetor3D(1.0, 0.0, 0.0)
    v_orto2 = Vetor3D(0.0, 1.0, 0.0)
    print("\n--- Teste com Vetores Ortogonais (Perpendiculares) ---")
    print(f"v_orto1: {v_orto1}")
    print(f"v_orto2: {v_orto2}")
    print(
        f"Produto escalar entre eixos X e Y: {v_orto1.produto_escalar(v_orto2)} (esperado: 0.0)")


if __name__ == "__main__":
    main()
