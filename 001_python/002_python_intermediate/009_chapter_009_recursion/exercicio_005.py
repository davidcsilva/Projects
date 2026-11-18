'''
14.5 Explique por que a seguinte função pode produzir um valor incorreto quando é executada:

real função fatorial (E real: n)
início
  se (n = 0 ou n = 1) então
    devolver(1)
  se_não
    devolver (n * fatorial (n-1))
  fim_se
fim_função

RESPOSTA / EXPLICAÇÃO:
1. Parâmetro do tipo REAL com valores fracionários:
   Como o parâmetro 'n' é do tipo real (ponto flutuante), se a função receber um valor
   não inteiro (por exemplo, n = 3.5), o decremento sucessivo (n - 1) gerará a sequência:
   3.5 -> 2.5 -> 1.5 -> 0.5 -> -0.5 -> -1.5 ...
   O valor de n NUNCA será exatamente igual a 0 ou 1. Portanto, a condição de parada
   (caso base) jamais será atingida, resultando em recursão infinita (estouro de pilha / stack overflow).

2. Números negativos (n < 0):
   Se n for negativo (por exemplo, n = -2), subtrair 1 sucessivamente afasta ainda mais n
   de 0 e 1 (-3, -4, ...), também levando à recursão infinita. O fatorial só é definido
   para inteiros não negativos (n >= 0).

3. Imprecisão de representação de ponto flutuante:
   Comparações de igualdade exata (n == 0 ou n == 1) em números reais/float são arriscadas
   devido a erros de arredondamento inerentes à representação binária (ex: 1.0000000000000002 != 1).

4. Definição Matemática:
   O fatorial simples n! é definido exclusivamente para inteiros não negativos.
   Para números reais gerais, a extensão requer a Função Gama (Gamma function), não
   decrementos unitários repetidos.
'''


def fatorial_incorreto(n: float) -> float:
    """Implementação literal do pseudocode do exercício."""
    if n == 0 or n == 1:
        return 1.0
    return n * fatorial_incorreto(n - 1)


def fatorial_correto(n: int) -> int:
    """Versão corrigida: restringe o domínio a inteiros não negativos."""
    if not isinstance(n, int) or n < 0:
        raise ValueError(
            "O fatorial é definido apenas para números inteiros não negativos (n >= 0).")
    if n in (0, 1):
        return 1
    return n * fatorial_correto(n - 1)


if __name__ == "__main__":
    # Exemplo com valor inteiro correto
    print(f"fatorial_correto(5) = {fatorial_correto(5)}")

    # Demonstração do problema com número real não inteiro:
    import sys
    print("\nTentando calcular fatorial_incorreto(3.5)...")
    try:
        # Limitando recursão temporariamente para demonstrar sem travar
        sys.setrecursionlimit(50)
        fatorial_incorreto(3.5)
    except RecursionError as e:
        print(
            f"Erro capturado com sucesso: {type(e).__name__} (Recursão infinita / estouro de pilha)")
