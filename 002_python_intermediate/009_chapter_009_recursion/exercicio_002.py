'''
14.2 O valor de x^n pode ser definido recursivamente como:
x^0 = 1
x^n = x * x^(n-1)

Escreva uma função recursiva que calcule e retorne o valor de x^n.
'''


def potencia(x: float | int, n: int) -> float | int:
    """Calcula x elevado a n (x^n) recursivamente."""
    if n < 0:
        return 1 / potencia(x, -n)
    if n == 0:
        return 1
    return x * potencia(x, n - 1)


if __name__ == "__main__":
    base = 2
    expoente = 3
    print(f"{base}^{expoente} = {potencia(base, expoente)}")

    # Testes adicionais
    print(f"5^0 = {potencia(5, 0)}")
    print(f"2^(-2) = {potencia(2, -2)}")
