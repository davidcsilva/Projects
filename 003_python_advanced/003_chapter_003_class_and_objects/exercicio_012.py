"""
Exercício 16.12:
Classe Complexo para gerenciar números complexos com as seguintes operações:
- Soma: a + c = (A + C, (B + D)i)
- Subtração: a - c = (A - C, (B - D)i)
- Multiplicação entre complexos: a * c = (A * C - B * D, (A * D + B * C)i)
- Multiplicação por número real: x * c = (x * C, (x * D)i)
- Conjugado: ~a = (A, -Bi)
"""

import math
from typing import Union


class Complexo:
    """
    Representa um número complexo da forma:
    z = (real, imag * i)  <=>  z = A + Bi
    """

    def __init__(self, real: float = 0.0, imag: float = 0.0) -> None:
        """
        Inicializa o número complexo com parte real e imaginária.
        """
        self.real: float = float(real)
        self.imag: float = float(imag)

    # 1. Soma: a + c = (A + C, (B + D)i)
    def somar(self, outro: Union["Complexo", float, int]) -> "Complexo":
        """
        Soma este número complexo com outro complexo ou escalar real.
        """
        if isinstance(outro, Complexo):
            return Complexo(self.real + outro.real, self.imag + outro.imag)
        elif isinstance(outro, (int, float)):
            return Complexo(self.real + float(outro), self.imag)
        raise TypeError(
            f"Operando inválido para soma: {type(outro).__name__}.")

    # 2. Subtração: a - c = (A - C, (B - D)i)
    def subtrair(self, outro: Union["Complexo", float, int]) -> "Complexo":
        """
        Subtrai outro número complexo ou escalar real deste complexo.
        """
        if isinstance(outro, Complexo):
            return Complexo(self.real - outro.real, self.imag - outro.imag)
        elif isinstance(outro, (int, float)):
            return Complexo(self.real - float(outro), self.imag)
        raise TypeError(
            f"Operando inválido para subtração: {type(outro).__name__}.")

    # 3. & 4. Multiplicação
    def multiplicar(self, outro: Union["Complexo", float, int]) -> "Complexo":
        """
        Multiplicação:
        - a * c = (A*C - B*D, (A*D + B*C)i) quando 'outro' é Complexo.
        - x * c = (x*C, (x*D)i) quando 'outro' é um escalar real x.
        """
        if isinstance(outro, Complexo):
            # Fórmula: (A*C - B*D) + (A*D + B*C)i
            novo_real = (self.real * outro.real) - (self.imag * outro.imag)
            novo_imag = (self.real * outro.imag) + (self.imag * outro.real)
            return Complexo(novo_real, novo_imag)
        elif isinstance(outro, (int, float)):
            # Fórmula: (x*C) + (x*D)i
            x = float(outro)
            return Complexo(self.real * x, self.imag * x)
        raise TypeError(
            f"Operando inválido para multiplicação: {type(outro).__name__}.")

    # 5. Conjugado: ~a = (A, -Bi)
    def conjugado(self) -> "Complexo":
        """
        Calcula o conjugado do número complexo:
        Se a = A + Bi, então ~a = A - Bi.
        """
        return Complexo(self.real, -self.imag)

    # --- Sobrecarga de Operadores Mágicos do Python ---

    def __add__(self, outro: Union["Complexo", float, int]) -> "Complexo":
        """Operador '+': a + c ou c + x."""
        return self.somar(outro)

    def __radd__(self, outro: Union[float, int]) -> "Complexo":
        """Operador '+' à esquerda: x + c."""
        return self.somar(outro)

    def __sub__(self, outro: Union["Complexo", float, int]) -> "Complexo":
        """Operador '-': a - c ou c - x."""
        return self.subtrair(outro)

    def __rsub__(self, outro: Union[float, int]) -> "Complexo":
        """Operador '-' à esquerda: x - c = (x - C, -D i)."""
        return Complexo(float(outro) - self.real, -self.imag)

    def __mul__(self, outro: Union["Complexo", float, int]) -> "Complexo":
        """Operador '*': a * c ou c * x."""
        return self.multiplicar(outro)

    def __rmul__(self, outro: Union[float, int]) -> "Complexo":
        """Operador '*' à esquerda: x * c."""
        return self.multiplicar(outro)

    def __invert__(self) -> "Complexo":
        """
        Operador unário '~': permite calcular o conjugado diretamente com ~a.
        Exemplo: ~Complexo(4.5, 3.0) -> (4.5 - 3.0i).
        """
        return self.conjugado()

    def __eq__(self, outro: object) -> bool:
        """Operador '==': compara a igualdade das partes real e imaginária."""
        if not isinstance(outro, Complexo):
            return False
        return math.isclose(self.real, outro.real, abs_tol=1e-9) and math.isclose(
            self.imag, outro.imag, abs_tol=1e-9
        )

    def __str__(self) -> str:
        """Formatação usual (A + Bi) ou (A - Bi)."""
        sinal = "+" if self.imag >= 0 else "-"
        return f"({self.real} {sinal} {abs(self.imag)}i)"

    def __repr__(self) -> str:
        return f"Complexo(real={self.real}, imag={self.imag})"


# Alias conforme convenção
complexo = Complexo


def main() -> None:
    print("=== Exercício 16.12: Classe Complexo com Operações Matemáticas ===")

    # Definindo os números complexos conforme exemplo do enunciado:
    # a = (A, Bi) e c = (C, Di)
    a = Complexo(4.5, 3.0)
    c = Complexo(2.0, -1.5)

    print(f"Número complexo a = {a}")
    print(f"Número complexo c = {c}")

    # 1. Soma: a + c = (A + C, (B + D)i)
    # (4.5 + 2.0, (3.0 + (-1.5))i) = (6.5 + 1.5i)
    soma_metodo = a.somar(c)
    soma_operador = a + c
    print("\n--- 1. Soma (a + c) ---")
    print(f"  Fórmula: ({a.real} + {c.real}) + ({a.imag} + ({c.imag}))i")
    print(f"  Via a.somar(c): {soma_metodo}")
    print(f"  Via operador a + c: {soma_operador}")

    # 2. Subtração: a - c = (A - C, (B - D)i)
    # (4.5 - 2.0, (3.0 - (-1.5))i) = (2.5 + 4.5i)
    sub_metodo = a.subtrair(c)
    sub_operador = a - c
    print("\n--- 2. Subtração (a - c) ---")
    print(f"  Fórmula: ({a.real} - {c.real}) + ({a.imag} - ({c.imag}))i")
    print(f"  Via a.subtrair(c): {sub_metodo}")
    print(f"  Via operador a - c: {sub_operador}")

    # 3. Multiplicação entre complexos: a * c = (A*C - B*D, (A*D + B*C)i)
    # real: 4.5*2.0 - 3.0*(-1.5) = 9.0 - (-4.5) = 13.5
    # imag: 4.5*(-1.5) + 3.0*2.0 = -6.75 + 6.0 = -0.75
    mul_metodo = a.multiplicar(c)
    mul_operador = a * c
    print("\n--- 3. Multiplicação entre complexos (a * c) ---")
    print(
        f"  Parte real: ({a.real} * {c.real}) - ({a.imag} * {c.imag}) = 13.5")
    print(
        f"  Parte imag: ({a.real} * {c.imag}) + ({a.imag} * {c.real}) = -0.75")
    print(f"  Via a.multiplicar(c): {mul_metodo}")
    print(f"  Via operador a * c:   {mul_operador}")

    # 4. Multiplicação por escalar real: x * c = (x*C, (x*D)i)
    x = 3.0
    mul_esc_metodo = c.multiplicar(x)
    mul_esc_operador = x * c
    print(f"\n--- 4. Multiplicação por número real (x = {x}) ---")
    print(f"  Fórmula: ({x} * {c.real}, ({x} * {c.imag})i)")
    print(f"  Via c.multiplicar({x}): {mul_esc_metodo}")
    print(f"  Via operador {x} * c:    {mul_esc_operador}")
    print(f"  Via operador c * {x}:    {c * x}")

    # 5. Conjugado: ~a = (A, -Bi)
    # Se a = (4.5 + 3.0i), ~a = (4.5 - 3.0i)
    conj_metodo = a.conjugado()
    conj_operador = ~a
    print("\n--- 5. Conjugado (~a) ---")
    print(f"  Original a:             {a}")
    print(f"  Via a.conjugado():      {conj_metodo}")
    print(f"  Via operador unário ~a: {conj_operador}")

    # Conjugado de c: (2.0 - 1.5i) -> (2.0 + 1.5i)
    print(f"  Original c:             {c}")
    print(f"  Conjugado ~c:           {~c}")


if __name__ == "__main__":
    main()
