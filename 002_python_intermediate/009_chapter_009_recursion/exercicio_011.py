'''
14.10 Escreva a função recursiva
inteiro função mdc (E inteiro: a, b)
que calcule o maior divisor comum de inteiros estritamente positivos a e b.
'''


def mdc(a: int, b: int) -> int:
    """Calcula recursivamente o Maior Divisor Comum (MDC) de dois inteiros estritamente positivos.

    Utiliza o Algoritmo de Euclides:
    - Caso base: se o resto da divisão de a por b for 0, o MDC é o próprio b.
    - Passo recursivo: mdc(a, b) = mdc(b, a % b).
    """
    if a <= 0 or b <= 0:
        raise ValueError(
            "Os parâmetros a e b devem ser inteiros estritamente positivos (a > 0, b > 0).")

    resto = a % b
    if resto == 0:
        return b

    return mdc(b, resto)


if __name__ == "__main__":
    exemplos = [
        (48, 18),
        (18, 48),
        (1071, 462),
        (7, 13),
        (100, 25),
        (81, 27),
    ]

    print("=== Cálculo do MDC Recursivo (Algoritmo de Euclides) ===")
    for a, b in exemplos:
        print(f"MDC({a:>4}, {b:>4}) = {mdc(a, b)}")
