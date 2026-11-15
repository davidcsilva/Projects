'''
14.3 Reescreva a função escrita no Exercício 14.2 de maneira que se utilize um algoritmo repetitivo para calcular o
valor de x^n.
'''


def potencia(x: float | int, n: int) -> float | int:
    """Calcula x elevado a n (x^n) utilizando um algoritmo repetitivo (iterativo)."""
    expoente = abs(n)
    resultado = 1

    for _ in range(expoente):
        resultado *= x

    if n < 0:
        return 1 / resultado
    return resultado


if __name__ == "__main__":
    base = 2
    expoente = 3
    print(f"{base}^{expoente} = {potencia(base, expoente)}")

    # Testes adicionais
    print(f"5^0 = {potencia(5, 0)}")
    print(f"2^(-2) = {potencia(2, -2)}")
