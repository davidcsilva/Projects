"""
Exercício 16.7:
Inclua na classe vetor3d do exercício anterior uma função membro denominada normamax,
que permita obter a norma maior de dois vetores.
(Nota: A norma de um vetor v = (x, y, z) é x² + y² + z² ou x*x + y*y + z*z.)
"""

import copy
import math
from typing import Optional, Union


class Vetor3D:
    """
    Representa um vetor tridimensional no espaço cartesiano (x, y, z).
    Inclui operações de comparação e cálculo de norma.
    """

    # --- Construtor único e em linha (inline) ---
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        self.x: float = float(x)
        self.y: float = float(y)
        self.z: float = float(z)

    # --- Cálculo de Norma (Exercício 16.7) ---

    def norma(self) -> float:
        """
        Calcula a norma do vetor conforme a nota do exercício:
        norma = x² + y² + z² (também conhecida como norma quadrada ou norma euclidiana ao quadrado).
        """
        return self.x * self.x + self.y * self.y + self.z * self.z

    def modulo(self) -> float:
        """
        Retorna o comprimento geométrico (módulo/magnitude euclidiana):
        sqrt(x² + y² + z²).
        """
        return math.sqrt(self.norma())

    def normamax(self, outro: "Vetor3D", retornar_vetor: bool = False) -> Union[float, "Vetor3D"]:
        """
        Função membro 'normamax':
        Compara a norma deste vetor (self) com a norma de 'outro' vetor e
        obtém a maior norma entre os dois.

        - Por padrão (retornar_vetor=False): retorna o valor numérico (float) da maior norma.
        - Se retornar_vetor=True: retorna a referência do próprio objeto Vetor3D que possui a maior norma.
        """
        if not isinstance(outro, Vetor3D):
            raise TypeError("O argumento deve ser uma instância de Vetor3D.")

        n1 = self.norma()
        n2 = outro.norma()

        if retornar_vetor:
            return self if n1 >= n2 else outro

        return max(n1, n2)

    def vetor_norma_max(self, outro: "Vetor3D") -> "Vetor3D":
        """
        Método auxiliar que retorna explicitamente o objeto Vetor3D com a maior norma.
        """
        return self if self.norma() >= outro.norma() else outro

    # --- Métodos de igualdade do Exercício 16.6 ---

    def igual_por_valor(self, outro: "Vetor3D") -> bool:
        """Transmissão por valor: opera em uma cópia independente do objeto."""
        if not isinstance(outro, Vetor3D):
            return False
        copia = copy.copy(outro)
        return (
            math.isclose(self.x, copia.x, abs_tol=1e-9)
            and math.isclose(self.y, copia.y, abs_tol=1e-9)
            and math.isclose(self.z, copia.z, abs_tol=1e-9)
        )

    def igual_por_endereco(self, outro: Optional["Vetor3D"]) -> bool:
        """Transmissão por endereço / ponteiro (const Vetor3D* em C++)."""
        if outro is None or not isinstance(outro, Vetor3D):
            return False
        if self is outro:
            return True
        return (
            math.isclose(self.x, outro.x, abs_tol=1e-9)
            and math.isclose(self.y, outro.y, abs_tol=1e-9)
            and math.isclose(self.z, outro.z, abs_tol=1e-9)
        )

    def igual_por_referencia(self, outro: "Vetor3D") -> bool:
        """Transmissão por referência (modelo nativo em Python)."""
        if not isinstance(outro, Vetor3D):
            return False
        return (
            math.isclose(self.x, outro.x, abs_tol=1e-9)
            and math.isclose(self.y, outro.y, abs_tol=1e-9)
            and math.isclose(self.z, outro.z, abs_tol=1e-9)
        )

    def igual(self, outro: Optional["Vetor3D"], modo: str = "referencia") -> bool:
        """Função membro unificada para teste de igualdade."""
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
            raise ValueError(f"Modo inválido: {modo!r}.")

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Vetor3D):
            return False
        return self.igual_por_referencia(outro)

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return f"Vetor3D(x={self.x}, y={self.y}, z={self.z})"


# Alias conforme enunciado
vetor3d = Vetor3D


def main() -> None:
    print("=== Exercício 16.7: Função Membro normamax na classe Vetor3D ===")

    # Criando instâncias de teste
    v1 = Vetor3D(1.0, 2.0, 2.0)   # norma = 1² + 2² + 2² = 1 + 4 + 4 = 9.0
    v2 = Vetor3D(3.0, 4.0, 0.0)   # norma = 3² + 4² + 0² = 9 + 16 + 0 = 25.0
    v3 = Vetor3D(2.0, 3.0, 4.0)   # norma = 2² + 3² + 4² = 4 + 9 + 16 = 29.0

    print(f"Vetor v1: {v1} -> norma = {v1.norma()} (módulo = {v1.modulo()})")
    print(f"Vetor v2: {v2} -> norma = {v2.norma()} (módulo = {v2.modulo()})")
    print(f"Vetor v3: {v3} -> norma = {v3.norma()} (módulo = {v3.modulo()})")

    # 1. Comparando v1 e v2
    maior_norma_v1_v2 = v1.normamax(v2)
    vetor_vencedor_1 = v1.normamax(v2, retornar_vetor=True)
    print(f"\nEntre v1 ({v1.norma()}) e v2 ({v2.norma()}):")
    print(f"  v1.normamax(v2) -> Maior valor de norma: {maior_norma_v1_v2}")
    print(f"  Vetor que possui essa maior norma: {vetor_vencedor_1}")

    # 2. Comparando v2 e v3
    maior_norma_v2_v3 = v2.normamax(v3)
    vetor_vencedor_2 = v2.normamax(v3, retornar_vetor=True)
    print(f"\nEntre v2 ({v2.norma()}) e v3 ({v3.norma()}):")
    print(f"  v2.normamax(v3) -> Maior valor de norma: {maior_norma_v2_v3}")
    print(f"  Vetor que possui essa maior norma: {vetor_vencedor_2}")

    # 3. Caso em que os vetores têm a mesma norma mas direções diferentes
    v4 = Vetor3D(2.0, 1.0, 2.0)  # norma = 4 + 1 + 4 = 9.0 (mesma que v1)
    print(
        f"\nEntre v1 {v1} (norma={v1.norma()}) e v4 {v4} (norma={v4.norma()}):")
    print(f"  v1.normamax(v4) -> {v1.normamax(v4)}")
    print(
        f"  v1.igual(v4)    -> {v1.igual(v4)} (vetores têm mesma norma mas não são iguais)")


if __name__ == "__main__":
    main()
