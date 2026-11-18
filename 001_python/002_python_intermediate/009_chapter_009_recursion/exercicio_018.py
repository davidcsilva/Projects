'''
14.7 / 14.18
Leia um número inteiro positivo n < 10. Calcule o desenvolvimento do polinômio (x + 1)^n.
Imprima cada potência x^i na forma x**i.

Sugestão:
(x + 1)^n = C_{n, n} x^n + C_{n, n-1} x^{n-1} + ... + C_{n, 2} x^2 + C_{n, 1} x^1 + C_{n, 0} x^0
onde C_{n, n} e C_{n, 0} são 1 para qualquer valor de n.

A relação de recorrência dos coeficientes binomiais é:
C(n, 0) = 1
C(n, n) = 1
C(n, k) = C(n - 1, k - 1) + C(n - 1, k)

Esses coeficientes constituem o famoso Triângulo de Pascal; defina a função que gera o triângulo.
'''


def coeficiente_binomial(n: int, k: int) -> int:
    """Calcula o coeficiente binomial C(n, k) utilizando a relação de recorrência de Pascal."""
    # Casos base:
    if k == 0 or k == n:
        return 1
    if k < 0 or k > n:
        return 0

    # Relação de recorrência:
    return coeficiente_binomial(n - 1, k - 1) + coeficiente_binomial(n - 1, k)


def desenvolvimento_polinomio(n: int) -> str:
    """Calcula e formata o desenvolvimento de (x + 1)^n com potências na forma x**i."""
    termos: list[str] = []
    # Coeficientes de n até 0 conforme a sugestão:
    for i in range(n, -1, -1):
        c = coeficiente_binomial(n, i)
        termos.append(f"{c}*x**{i}")

    return " + ".join(termos)


def gerar_triangulo_pascal(linhas: int) -> list[list[int]]:
    """Gera o Triângulo de Pascal até o número de linhas especificado."""
    triangulo: list[list[int]] = []
    for i in range(linhas):
        linha = [coeficiente_binomial(i, k) for k in range(i + 1)]
        triangulo.append(linha)
    return triangulo


def imprimir_triangulo_pascal(triangulo: list[list[int]]) -> None:
    """Imprime o Triângulo de Pascal formatado."""
    for linha in triangulo:
        print("  ".join(f"{num:>3}" for num in linha))


def main() -> None:
    # Permite entrada interativa com valor padrão para testes automáticos
    try:
        entrada = input(
            "Digite um número inteiro positivo n < 10 (pressione Enter para padrão 4): ").strip()
        n = int(entrada) if entrada else 4
    except (ValueError, EOFError):
        n = 4

    if not (0 < n < 10):
        print("Aviso: n deve ser positivo e menor que 10. Ajustando n para 4.")
        n = 4

    print(f"\n1. Desenvolvimento do polinômio (x + 1)^{n}:")
    polinomio = desenvolvimento_polinomio(n)
    print(f"(x + 1)^{n} = {polinomio}")

    print(f"\n2. Triângulo de Pascal até n = {n} (linhas 0 a {n}):")
    triangulo = gerar_triangulo_pascal(n + 1)
    imprimir_triangulo_pascal(triangulo)


if __name__ == "__main__":
    main()
