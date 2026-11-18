'''
14.8 Escreva uma função recursiva que calcule a função de Ackermann definida da seguinte maneira:

A(m, n) = n + 1                  se m = 0
A(m, n) = A(m – 1, 1)            se n = 0
A(m, n) = A(m – 1, A(m, n – 1))  se m > 0 e n > 0
'''


def ackermann(m: int, n: int) -> int:
    """Calcula a função de Ackermann-Péter A(m, n) de forma recursiva.

    Parâmetros:
        m (int): Inteiro não negativo.
        n (int): Inteiro não negativo.

    Retorna:
        int: O resultado de A(m, n).
    """
    if m < 0 or n < 0:
        raise ValueError(
            "Os parâmetros m e n devem ser inteiros não negativos (m >= 0, n >= 0).")

    # Caso 1: se m = 0
    if m == 0:
        return n + 1

    # Caso 2: se m > 0 e n = 0
    elif n == 0:
        return ackermann(m - 1, 1)

    # Caso 3: se m > 0 e n > 0
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


if __name__ == "__main__":
    print("=== Tabela de valores da Função de Ackermann A(m, n) ===")
    for m in range(4):
        for n in range(5):
            print(f"A({m}, {n}) = {ackermann(m, n):<4}", end="  ")
        print()

    print("\nExemplo adicional:")
    print(f"A(3, 3) = {ackermann(3, 3)}")
