'''
A expressão matemática C(m, n) no mundo da teoria combinatória dos números representa o
número de combinações de m elementos assumidos de n em n elementos:

C(m, n) = m! / (n! * (m – n)!)

Escreva e teste uma função que calcule C(m, n) onde n! é o fatorial de n.
'''


def fatorial(n: int) -> int:
    """Calcula o fatorial de um número inteiro não negativo recursivamente."""
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos.")
    if n in (0, 1):
        return 1
    return n * fatorial(n - 1)


def combinacao(m: int, n: int) -> int:
    """Calcula o número de combinações de m elementos tomados n a n: C(m, n).

    Fórmula:
        C(m, n) = m! / (n! * (m - n)!)
    """
    if m < 0 or n < 0:
        raise ValueError(
            "Os parâmetros m e n devem ser inteiros não negativos (m >= 0, n >= 0).")

    if n > m:
        return 0

    return fatorial(m) // (fatorial(n) * fatorial(m - n))


def combinacao_recursiva_pascal(m: int, n: int) -> int:
    """Calcula C(m, n) de forma 100% recursiva utilizando a Relação de Pascal:

    C(m, 0) = 1
    C(m, m) = 1
    C(m, n) = C(m - 1, n - 1) + C(m - 1, n)
    """
    if m < 0 or n < 0 or n > m:
        return 0
    if n == 0 or n == m:
        return 1
    return combinacao_recursiva_pascal(m - 1, n - 1) + combinacao_recursiva_pascal(m - 1, n)


if __name__ == "__main__":
    testes = [
        (5, 2),
        (6, 3),
        (10, 4),
        (5, 0),
        (5, 5),
        (7, 3),
    ]

    print("=== Testes de Combinações C(m, n) ===")
    for m, n in testes:
        resultado = combinacao(m, n)
        resultado_pascal = combinacao_recursiva_pascal(m, n)
        print(
            f"C({m:>2}, {n:>2}) = {resultado:>4}  (Pascal recursivo: {resultado_pascal:>4})")
