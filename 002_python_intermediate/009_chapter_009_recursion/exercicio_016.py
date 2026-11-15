'''
A soma dos primeiros n números inteiros responde à fórmula:
1 + 2 + 3 + ... + n = n(n + 1)/2

Inicie o array A que contém os primeiros 50 inteiros. A média desses elementos do array é 51/2 = 25,5.
Teste a solução aplicando a função recursiva média (média (float a[], int n)).
'''


def media(a: list[float], n: int) -> float:
    """Calcula recursivamente a média dos primeiros n elementos de um array 'a'.

    Relação de recorrência:
        - Para n = 1: média = a[0]
        - Para n > 1: média(n) = [média(n - 1) * (n - 1) + a[n - 1]] / n
    """
    if n <= 0:
        raise ValueError(
            "O número de elementos 'n' deve ser maior ou igual a 1.")

    # Caso base: média de 1 único elemento é o próprio elemento
    if n == 1:
        return float(a[0])

    # Passo recursivo: reconstrói a soma dos n - 1 elementos anteriores,
    # adiciona o n-ésimo elemento a[n - 1] e divide por n.
    return (media(a, n - 1) * (n - 1) + a[n - 1]) / n


if __name__ == "__main__":
    # Inicializa o array A contendo os primeiros 50 inteiros (1 a 50)
    n = 50
    A = [float(i) for i in range(1, n + 1)]

    # Cálculo analítico teórico:
    soma_teorica = (n * (n + 1)) / 2
    media_teorica = soma_teorica / n  # (n + 1) / 2 = 51 / 2 = 25.5

    # Cálculo pela função recursiva:
    media_calculada = media(A, n)

    print("=== CÁLCULO DA MÉDIA RECURSIVA ===")
    print(f"Array A com {len(A)} elementos: {A[:5]} ... {A[-5:]}")
    print(f"Soma dos primeiros {n} inteiros: {soma_teorica:.0f}")
    print(f"Média teórica esperada (51 / 2): {media_teorica:.1f}")
    print(f"Média obtida recursivamente:     {media_calculada:.1f}")
    print(
        f"Resultado correto?               {media_calculada == media_teorica}")
