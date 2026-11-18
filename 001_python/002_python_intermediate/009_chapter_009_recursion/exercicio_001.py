'''
14.1 A soma de uma série de números consecutivos de 1 pode ser definida recursivamente como:
soma(1) = 1
soma(n) = n + soma(n-1)
Escreva a função recursiva que aceite n como um argumento e calcule a soma dos números de 1 a n.
'''


def soma(n: int) -> int:
    """Calcula a soma dos números consecutivos de 1 até n de forma recursiva."""
    if n <= 0:
        raise ValueError("n deve ser um número inteiro maior ou igual a 1.")
    if n == 1:
        return 1
    return n + soma(n - 1)


if __name__ == "__main__":
    n = 5
    print(f"soma({n}) = {soma(n)}")
